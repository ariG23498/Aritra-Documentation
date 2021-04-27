# auc







Compute Area Under the Curve (AUC) using the trapezoidal rule.

<pre><code>auc(
    x, y
)</code></pre>




This is a general function, given points on a curve.  For computing the
area under the ROC-curve, see :func:<code>roc_auc_score</code>.  For an alternative
way to summarize a precision-recall curve, see
:func:<code>average_precision_score</code>.

Parameters
----------
x : ndarray of shape (n,)
    x coordinates. These must be either monotonic increasing or monotonic
    decreasing.
y : ndarray of shape, (n,)
    y coordinates.

Returns
-------
auc : float

See Also
--------
roc_auc_score : Compute the area under the ROC curve.
average_precision_score : Compute average precision from prediction scores.
precision_recall_curve : Compute precision-recall pairs for different
    probability thresholds.

Examples
--------
```
>>> import numpy as np
>>> from sklearn import metrics
>>> y = np.array([1, 1, 2, 2])
>>> pred = np.array([0.1, 0.4, 0.35, 0.8])
>>> fpr, tpr, thresholds = metrics.roc_curve(y, pred, pos_label=2)
>>> metrics.auc(fpr, tpr)
0.75
```