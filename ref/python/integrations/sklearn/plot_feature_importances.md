# plot_feature_importances



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L582-L667)




Evaluates & plots the importance of each feature for the classification task.

<pre><code>plot_feature_importances(
    model=None, feature_names=None, title=&#x27;Feature Importance&#x27;,
    max_num_features=50
)</code></pre>




Should only be called with a fitted classifer (otherwise an error is thrown).
Only works with classifiers that have a feature_importances_ attribute, like trees.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
model (clf): Takes in a fitted classifier.
feature_names (list): Names for features. Makes plots easier to read by
replacing feature indexes with corresponding names.
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

wandb.sklearn.plot_feature_importances(model, ['width', 'height, 'length'])
