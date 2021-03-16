"""A tool to generate api_docs for wandb

```
python generate.py --output_dir=docs
```

Requires a local installation of `tensorflow_docs`:

```
pip install git+https://github.com/tensorflow/docs
```
"""
from os import path, walk, getcwd, remove, rename

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import generate_lib
import wandb

from docgen_cli import cli_gen


def build_docs(name_pair, output_dir, code_url_prefix, search_hints, gen_report):
    """Build api docs for W&B.

    Args:
        name_pair: Name of the pymodule
        output_dir: A string path, where to put the files.
        code_url_prefix: prefix for "Defined in" links.
        search_hints: Bool. Include meta-data search hints at the top of each file.
        gen_report: Bool. Generates an API report containing the health of the
            docstrings of the public API.
    """
    # This is to help not document the parent class methods
    for cls in [
        wandb.data_types.WBValue,
        wandb.data_types.Media,
        wandb.data_types.BatchableMedia,
        wandb.apis.public.Paginator,
    ]:
        doc_controls.decorate_all_class_attributes(
            decorator=doc_controls.do_not_doc_in_subclasses, cls=cls, skip=["__init__"]
        )

    doc_generator = generate_lib.DocGenerator(
        root_title="W&B",
        py_modules=[name_pair],
        base_dir=path.dirname(wandb.__file__),
        search_hints=search_hints,
        code_url_prefix=code_url_prefix,
        site_path="",
        gen_report=gen_report,
        yaml_toc=False,
    )

    doc_generator.build(output_dir)


def populate_summary(folder: str) -> None:
    """Populates the `SUMMARY.md` with generated filne names.

    GitBook uses the `SUMMARY.md` file to handle what we see in
    the site. With automated docs, we need to generate the file names
    and insert the names into the `SUMMARY.md` file.

    Args:
        folder: Str. The root folder that contains
            the generated docs.
    """
    with open("_SUMMARY.md", "r") as f:
        doc_structure = f.read()
    lines = []
    indent = 0
    for root, dirs, files in walk(folder):
        if "/" in root:
            short_root = root.split("/")
            indent = len(short_root)
            short_root = short_root[-1]
        else:
            short_root = root
        lines.append(" " * indent + f"* [{short_root}]({root}/README.md)")
        for file_name in files:
            if file_name != "README.md":
                short_name = file_name.split(".")[0]
                lines.append(" " * indent + f"  * [{short_name}]({root}/{file_name})")
    lines = "\n".join(lines)
    doc_structure = doc_structure.format(autodoc=lines)

    with open("SUMMARY.md", "w") as f:
        f.write(doc_structure)


if __name__ == "__main__":
    # GitHash: 3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c
    git_hash = "3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c"
    CODE_URL_PREFIX = f"https://www.github.com/wandb/client/tree/{git_hash}/wandb"

    # For library
    wandb.Run = wandb.sdk.wandb_run.Run
    wandb_classes = [
        "Artifact",
        "config",
        "summary",
        "init",
        "login",
        "Run",
    ]
    wandb.__all__ = wandb_classes
    wandb.__doc__ = """
    """
    try:
        doc_controls.do_not_generate_docs(wandb.Run.__exit__)
    except AttributeError:
        pass
    try:
        doc_controls.do_not_generate_docs(wandb.Run.__enter__)
    except AttributeError:
        pass
    build_docs(
        name_pair=("library", wandb),
        output_dir=".",
        code_url_prefix=CODE_URL_PREFIX,
        search_hints=False,
        gen_report=False,
    )

    # For library
    wandb_datatypes = [
        "Image",
        "Plotly",
        "Video",
        "Audio",
        "Table",
        "Html",
        "Object3D",
        "Molecule",
        "Histogram",
    ]
    wandb.__all__ = wandb_datatypes
    wandb.__doc__ = """
    """
    build_docs(
        name_pair=("data-types", wandb),
        output_dir="./library",
        code_url_prefix=CODE_URL_PREFIX,
        search_hints=False,
        gen_report=False,
    )

    # For library
    wandb.Api = wandb.apis.public.Api
    wandb.Projects = wandb.apis.public.Projects
    wandb.Project = wandb.apis.public.Project
    wandb.Runs = wandb.apis.public.Runs
    wandb.Run = wandb.apis.public.Run
    wandb.Sweep = wandb.apis.public.Sweep
    wandb.Files = wandb.apis.public.Files
    wandb.File = wandb.apis.public.File
    wandb.Artifact = wandb.apis.public.Artifact
    wandb_api_doc = [
        "Api",
        "Projects",
        "Project",
        "Runs",
        "Run",
        "Sweep",
        "Files",
        "File",
        "Artifact",
    ]
    wandb.__all__ = wandb_api_doc
    wandb.__doc__ = """
    Use the Public API to export or update data that you have saved to W&B.
    Before using this API, you'll want to log data from your script — check the [Quickstart](../quickstart.md) for more details.

    **Use Cases for the Public API**

    * **Export Data**: Pull down a dataframe for custom analysis in a Jupyter Notebook. Once you have explored the data, you can sync your findings by creating a new analysis run and logging results, for example: `wandb.init(job_type="analysis")`
    * **Update Existing Runs**: You can update the data logged in association with a W&B run. For example, you might want to update the config of a set of runs to include additional information, like the architecture or a hyperparameter that wasn't originally logged.

    See the [Generated Reference Docs](../ref/public-api/) for details on available functions.
    """
    build_docs(
        name_pair=("public-api", wandb),
        output_dir="./library",
        code_url_prefix=CODE_URL_PREFIX,
        search_hints=False,
        gen_report=False,
    )

    # Remove the unwanted files
    # all_symbols and _api.cache.md
    directory = getcwd()
    for root, folder, file_names in walk("."):
        if "all_symbols.md" in file_names:
            remove(f"{root}/all_symbols.md")
        if "_api_cache.json" in file_names:
            remove(f"{root}/_api_cache.json")

    # Moving all the folder md to respective folders
    rename(f"{directory}/library.md", f"{directory}/library/README.md")
    # rename(f"{directory}/library/run.md", f"{directory}/library/run/README.md")
    rename(
        f"{directory}/library/data-types.md",
        f"{directory}/library/data-types/README.md",
    )
    rename(
        f"{directory}/library/public-api.md",
        f"{directory}/library/public-api/README.md",
    )

    # Convert everything to lowercase
    for root, folder, file_names in walk("library"):
        for name in file_names:
            if name == "README.md":
                short_name = name
            else:
                short_name = name.replace(" ", "-").lower()
            rename(f"{directory}/{root}/{name}", f"{directory}/{root}/{short_name}")

    # Create the CLI docs
    cli_gen()

    # SUMMARY.md magic
    populate_summary("library")
