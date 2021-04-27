# plot_outlier_candidates



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L1212-L1309)




Measures a datapoint's influence on regression model via cook's distance.

<pre><code>plot_outlier_candidates(
    regressor=None, X=None, y=None
)</code></pre>



    Instances with heavily skewed influences could potentially be
    outliers. Useful for outlier detection.

Should only be called with a fitted regressor (otherwise an error is thrown).
Please note this function fits the model on the training set when called.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
model (regressor): Takes in a fitted regressor.
X (arr): Training set features.
y (arr): Training set labels.
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

wandb.sklearn.plot_outlier_candidates(model, X, y)
