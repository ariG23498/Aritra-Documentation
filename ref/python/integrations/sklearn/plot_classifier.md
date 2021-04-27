# plot_classifier



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L52-L116)




Generates all sklearn classifier plots supported by W&B.

<pre><code>plot_classifier(
    model, X_train, X_test, y_train, y_test, y_pred, y_probas, labels,
    is_binary=(False), model_name=&#x27;Classifier&#x27;, feature_names=None
)</code></pre>



    The following plots are generated:
    feature importances, learning curve, confusion matrix, summary metrics,
    class balance plot, calibration curve, roc curve & precision recall curve.

Should only be called with a fitted classifer (otherwise an error is thrown).

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
model (classifier): Takes in a fitted classifier.
X_train (arr): Training set features.
y_train (arr): Training set labels.
X_test (arr): Test set features.
y_test (arr): Test set labels.
y_pred (arr): Test set predictions by the model passed.
y_probas (arr): Test set predicted probabilities by the model passed.
labels (list): Named labels for target varible (y). Makes plots easier to
read by replacing target values with corresponding index.
For example labels= ['dog', 'cat', 'owl'] all 0s are
replaced by 'dog', 1s by 'cat'.
is_binary (bool): Is the model passed a binary classifier? Defaults to False
model_name (str): Model name. Defaults to 'Classifier'
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

wandb.sklearn.plot_classifier(model, X_train, X_test, y_train, y_test,
                y_pred, y_probas, ['cat', 'dog'], False,
                'RandomForest', ['barks', 'drools, 'plays_fetch', 'breed'])
