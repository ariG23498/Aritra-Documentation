# wandb.finish

[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/sdk/wandb_run.py#L2434-L2442)

Marks a run as finished, and finishes uploading all data.

```text
finish(
    exit_code: int = None
) -> None
```

This is used when creating multiple runs in the same process. We automatically call this method when your script exits.

