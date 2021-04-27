# plot_regressor



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L122-L153)




Generates all sklearn regressor plots supported by W&B.

<pre><code>plot_regressor(
    model, X_train, X_test, y_train, y_test, model_name=&#x27;Regressor&#x27;
)</code></pre>



    The following plots are generated:
    learning curve, summary metrics, residuals plot, outlier candidates.

Should only be called with a fitted regressor (otherwise an error is thrown).

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
model (regressor): Takes in a fitted regressor.
X_train (arr): Training set features.
y_train (arr): Training set labels.
X_test (arr): Test set features.
y_test (arr): Test set labels.
model_name (str): Model name. Defaults to 'Regressor'
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

wandb.sklearn.plot_regressor(reg, X_train, X_test, y_train, y_test, 'Ridge')
