# join



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/7bbc4a4eac8eeb2bf37a62ce519e0de61c67eadf/wandb/sdk/wandb_run.py#L2386-L2394)




Marks a run as finished, and finishes uploading all data.

<pre><code>join(
    exit_code: int = None
) -> None</code></pre>




This is used when creating multiple runs in the same process.
We automatically call this method when your script exits.