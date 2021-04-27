# plot_silhouette



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L757-L970)




Measures & plots a measure of how close each point in one cluster is to points

<pre><code>plot_silhouette(
    clusterer=None, X=None, cluster_labels=None, labels=None,
    metric=&#x27;euclidean&#x27;, kmeans=(True)
)</code></pre>



    in the neighboring clusters. Silhouette coefficients near +1 indicate that
    the sample is far away from the neighboring clusters. A value of 0 indicates
     that the sample is on or very close to the decision boundary between two
     neighboring clusters and negative values indicate that those samples might
     have been assigned to the wrong cluster.

Should only be called with a fitted clusterer (otherwise an error is thrown).
Please note this function fits the model on the training set when called.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
model (clusterer): Takes in a fitted clusterer.
X (arr): Training set features.
cluster_labels (list): Names for cluster labels. Makes plots easier to read
by replacing cluster indexes with corresponding names.
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

wandb.sklearn.plot_silhouette(model, X_train, ['spam', 'not spam'])
