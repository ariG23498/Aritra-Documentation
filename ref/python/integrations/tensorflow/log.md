# log



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/integration/tensorboard/log.py#L246-L297)




Logs a tfsummary to wandb

<pre><code>log(
    tf_summary_str_or_pb, history=None, step=0, namespace=&#x27;&#x27;, **kwargs
)</code></pre>




Can accept a tf summary string or parsed event.  Will use wandb.run.history unless a
history object is passed.  Can optionally namespace events.  Results are commited
when step increases for this namespace.

NOTE: This assumes that events being passed in are in chronological order