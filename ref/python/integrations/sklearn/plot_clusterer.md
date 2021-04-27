# plot_clusterer



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L156-L189)




Generates all sklearn clusterer plots supported by W&B.

<pre><code>plot_clusterer(
    model, X_train, cluster_labels, labels=None, model_name=&#x27;Clusterer&#x27;
)</code></pre>



    The following plots are generated:
    elbow curve, silhouette plot.

Should only be called with a fitted clusterer (otherwise an error is thrown).

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
model (clusterer): Takes in a fitted clusterer.
X_train (arr): Training set features.
cluster_labels (list): Names for cluster labels. Makes plots easier to read
by replacing cluster indexes with corresponding names.
labels (list): Named labels for target varible (y). Makes plots easier to
read by replacing target values with corresponding index.
For example labels= ['dog', 'cat', 'owl'] all 0s are
replaced by 'dog', 1s by 'cat'.
model_name (str): Model name. Defaults to 'Clusterer'
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

wandb.sklearn.plot_clusterer(kmeans, X, cluster_labels, labels, 'KMeans')
