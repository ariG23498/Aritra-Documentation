# plot_calibration_curve



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L1050-L1209)




Plots how well calibrated the predicted probabilities of a classifier are and

<pre><code>plot_calibration_curve(
    clf=None, X=None, y=None, clf_name=&#x27;Classifier&#x27;
)</code></pre>



    how to calibrate an uncalibrated classifier. Compares estimated predicted
    probabilities by a baseline logistic regression model, the model passed as
    an argument, and by both its isotonic calibration and sigmoid calibrations.
    The closer the calibration curves are to a diagonal the better.
    A sine wave like curve represents an overfitted classifier, while a cosine
    wave like curve represents an underfitted classifier.
    By training isotonic and sigmoid calibrations of the model and comparing
    their curves we can figure out whether the model is over or underfitting and
    if so which calibration (sigmoid or isotonic) might help fix this.
    For more details, see https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html.

Should only be called with a fitted classifer (otherwise an error is thrown).
Please note this function fits variations of the model on the training set when called.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
model (clf): Takes in a fitted classifier.
X (arr): Training set features.
y (arr): Training set labels.
model_name (str): Model name. Defaults to 'Classifier'
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

wandb.sklearn.plot_calibration_curve(clf, X, y, 'RandomForestClassifier')
