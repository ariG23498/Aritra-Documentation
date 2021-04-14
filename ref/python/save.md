# wandb.save

[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/7bbc4a4eac8eeb2bf37a62ce519e0de61c67eadf/wandb/sdk/wandb_run.py#L1058-L1147)

Ensure all files matching _glob\_str_ are synced to wandb with the policy specified.

```text
save(
    glob_str: Optional[str] = None,
    base_path: Optional[str] = None,
    policy: str = 'live'
) -> Union[bool, List[str]]
```

| Arguments |  |
| :--- | :--- |
|  `glob_str` |  \(string\) a relative or absolute path to a unix glob or regular path. If this isn't specified the method is a noop. |
|  `base_path` |  \(string\) the base path to run the glob relative to |
|  `policy` |  \(string\) on of `live`, `now`, or `end` - live: upload the file as it changes, overwriting the previous version - now: upload the file once now - end: only upload file when the run ends |

