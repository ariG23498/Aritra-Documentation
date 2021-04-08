# wandb sync

**Usage**

` wandb sync [OPTIONS] [PATH]...`

**Summary**

Upload an offline training directory to W&B


**Options**
| **Options** | **Description** |
|:--|:--|:--|
|--id TEXT|The run you want to upload to.|
|-p, --project TEXT|The project you want to upload to.|
|-e, --entity TEXT|The entity to scope to.|
|--include-globs TEXT|Comma seperated list of globs to include.|
|--exclude-globs TEXT|Comma seperated list of globs to exclude.|
|--sync-all|Sync all runs|
|--clean|Delete synced runs|
|--clean-old-hours INTEGER|Delete runs created before this many hours.|
|--clean-force|Clean without confirmation prompt.|
|--show INTEGER|Number of runs to show|
|--help|Show this message and exit.|


