import subprocess
import re

PATTERN = re.compile(r'(.*?\w) +(.*)')
KEYWORDS = ["Options:", "Commands:"]
TEMPLATE = """
{}

{}

{}

{}

{}
""".strip()

def process(document):
    summary = []
    keyword = None
    parsed_dict = {}

    for line in document.split('\n'):
        line = line.strip() #strip off the whitespace
        if line == '':
            # Check for no line
            continue
        if line in KEYWORDS:
            parsed_dict[line] = []
            keyword = line
            continue
        if keyword is None:
            summary.append(line)
        else:
            extract = PATTERN.findall(line)
            if extract:
                parsed_dict[keyword].append([extract[0][0], extract[0][1]])
    if len(summary) == 0:
        return '', '', parsed_dict
    elif len(summary) == 1:
        return summary[0], '', parsed_dict
    else:
        usage = summary[0]
        summary = '\n'.join(summary[1:])
        return usage, summary, parsed_dict
        

def cli_process(rw='w',param=''):
    wandb = subprocess.run(
        'wandb {} --help'.format(param),
        shell=True,
        capture_output=True,
        text=True).stdout
    usage, summary, parsed_dict = process(wandb)
    if usage:
        usage = usage.split(':')
        usage=f"## Usage\n`{usage[1]}`"
    if summary:
        summary=f"## Summary\n {summary}"
    options = ''
    commands = ''
    op = True
    co = True
    for k,v in parsed_dict.items():
        for element in v:
            if k == "Options:":
                options += """|{}|{}|\n""".format(element[0],element[1]) 
            elif k == "Commands:":
                commands += """|{}|{}|\n""".format(element[0],element[1])
        if options and op:
            options = """| **Options** | **Description** |\n|:--|:--|\n""" + options
            op = False
        if commands and co:
            commands = """| **Commands** | **Description** |\n|:--|:--|\n""" + commands
    with open("cli.md", rw) as fp:
        fp.write(
            TEMPLATE.format(
                f"# {param}", # Heading
                usage, # Usage
                summary,
                options, # Options
                commands  # Commands
            )
        )
    return parsed_dict

parsed_dict = cli_process()
for k,v in parsed_dict.items():
    if k == 'Commands:':
        for element in v:
            cli_process(rw='a',param=element[0])
        