# wandb sync

**Usage**

` wandb sync [OPTIONS] [PATH]...`

**Summary**

Upload an offline training directory to W&B


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--id|The run you want to upload to.|
|-p, --project|The project you want to upload to.|
|-e, --entity|The entity to scope to.|
|--include-globs|Comma seperated list of globs to include.|
|--exclude-globs|Comma seperated list of globs to exclude.|
|--sync-all|Sync all runs|
|--clean|Delete synced runs|
|--clean-old-hours|Delete runs created before this many hours.|
|--clean-force|Clean without confirmation prompt.|
|--show|Number of runs to show|
|--help|Show this message and exit.|


