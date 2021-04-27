# summary_metrics



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L192-L270)




Calculates summary metrics (like mse, mae, r2 score) for both regression and

<pre><code>summary_metrics(
    model=None, X=None, y=None, X_test=None, y_test=None
)</code></pre>



classification algorithms.

Called by plot_summary_metrics to visualize metrics. Please use the function
plot_summary_metric() if you wish to visualize your summary metrics.