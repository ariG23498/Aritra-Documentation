# roc



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/plots/roc.py#L13-L103)




Calculates receiver operating characteristic scores and visualizes them as the

<pre><code>roc(
    y_true=None, y_probas=None, labels=None, plot_micro=(True), plot_macro=(True),
    classes_to_plot=None
)</code></pre>



 ROC curve.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
y_true (arr): Test set labels.
y_probas (arr): Test set predicted probabilities.
labels (list): Named labels for target varible (y). Makes plots easier to
read by replacing target values with corresponding index.
For example labels= ['dog', 'cat', 'owl'] all 0s are
replaced by 'dog', 1s by 'cat'.
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
Nothing. To see plots, go to your W&B run page then expand the 'media' tab
under 'auto visualizations'.
</td>
</tr>

</table>



#### Example:

wandb.log({'roc': wandb.plots.ROC(y_true, y_probas, labels)})
