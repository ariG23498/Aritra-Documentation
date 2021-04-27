# plot_residuals



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L1312-L1434)




Measures and plots the predicted target values (y-axis) vs the difference

<pre><code>plot_residuals(
    regressor=None, X=None, y=None
)</code></pre>



    between actual and predicted target values (x-axis), as well as the
    distribution of the residual error.

Should only be called with a fitted regressor (otherwise an error is thrown).
Please note this function fits variations of the model on the training set when called.

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

wandb.sklearn.plot_residuals(model, X, y)
