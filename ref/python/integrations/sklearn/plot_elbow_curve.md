# plot_elbow_curve



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L670-L754)




Measures and plots the percentage of variance explained as a function of the

<pre><code>plot_elbow_curve(
    clusterer=None, X=None, cluster_ranges=None, n_jobs=1, show_cluster_time=(True)
)</code></pre>



    number of clusters, along with training times. Useful in picking the
    optimal number of clusters.

Should only be called with a fitted clusterer (otherwise an error is thrown).
Please note this function fits the model on the training set when called.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
model (clusterer): Takes in a fitted clusterer.
X (arr): Training set features.
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

wandb.sklearn.plot_elbow_curve(model, X_train)
