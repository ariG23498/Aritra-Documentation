# confusion_matrix



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L423-L503)




Computes the confusion matrix to evaluate the accuracy of a classification.

<pre><code>confusion_matrix(
    y_true=None, y_pred=None, labels=None, true_labels=None, pred_labels=None,
    title=None, normalize=(False), hide_zeros=(False), hide_counts=(False)
)</code></pre>




Called by plot_confusion_matrix to visualize roc curves. Please use the function
plot_confusion_matrix() if you wish to visualize your confusion matrix.