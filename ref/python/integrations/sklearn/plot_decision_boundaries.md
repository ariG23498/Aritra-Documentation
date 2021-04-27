# plot_decision_boundaries



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L1437-L1533)




Visualizes decision boundaries by sampling from the feature space where the

<pre><code>plot_decision_boundaries(
    binary_clf=None, X=None, y=None
)</code></pre>



    classifier's uncertainty > 0.5 and projecting these point to 2D space.
    Useful for measuring model (decision boundary) complexity, visualizing
    regions where the model falters and determine whether any over or
    underfitting occured.

Should only be called with a fitted **binary** classifer (otherwise an error is
    thrown). Please note this function fits variations of the model on the
    training set when called.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
model (clf): Takes in a fitted binary classifier.
X_train (arr): Training set features.
y_train (arr): Training set labels.
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

wandb.sklearn.plot_decision_boundaries(binary_classifier, X, y)
