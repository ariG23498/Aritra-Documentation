# plot_class_proportions



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L973-L1047)




Plots the distribution of target classses in training and test sets.

<pre><code>plot_class_proportions(
    y_train=None, y_test=None, labels=None
)</code></pre>



    Useful for detecting imbalanced classes.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
y_train (arr): Training set labels.
y_test (arr): Test set labels.
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

wandb.sklearn.plot_class_proportions(y_train, y_test, ['dog', 'cat', 'owl'])
