# calibration_curve







Compute true and predicted probabilities for a calibration curve.

<pre><code>calibration_curve(
    y_true, y_prob, *, normalize=(False), n_bins=5, strategy=&#x27;uniform&#x27;
)</code></pre>




The method assumes the inputs come from a binary classifier, and
discretize the [0, 1] interval into bins.

Calibration curves may also be referred to as reliability diagrams.

Read more in the :ref:`User Guide <calibration>`.

Parameters
----------
y_true : array-like of shape (n_samples,)
    True targets.

y_prob : array-like of shape (n_samples,)
    Probabilities of the positive class.

normalize : bool, default=False
    Whether y_prob needs to be normalized into the [0, 1] interval, i.e.
    is not a proper probability. If True, the smallest value in y_prob
    is linearly mapped onto 0 and the largest one onto 1.

n_bins : int, default=5
    Number of bins to discretize the [0, 1] interval. A bigger number
    requires more data. Bins with no samples (i.e. without
    corresponding values in <code>y_prob</code>) will not be returned, thus the
    returned arrays may have less than <code>n_bins</code> values.

strategy : {'uniform', 'quantile'}, default='uniform'
    Strategy used to define the widths of the bins.

    uniform
        The bins have identical widths.
    quantile
        The bins have the same number of samples and depend on <code>y_prob</code>.

Returns
-------
prob_true : ndarray of shape (n_bins,) or smaller
    The proportion of samples whose class is the positive class, in each
    bin (fraction of positives).

prob_pred : ndarray of shape (n_bins,) or smaller
    The mean predicted probability in each bin.

References
----------
Alexandru Niculescu-Mizil and Rich Caruana (2005) Predicting Good
Probabilities With Supervised Learning, in Proceedings of the 22nd
International Conference on Machine Learning (ICML).
See section 4 (Qualitative Analysis of Predictions).

Examples
--------
```
>>> import numpy as np
>>> from sklearn.calibration import calibration_curve
>>> y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
>>> y_pred = np.array([0.1, 0.2, 0.3, 0.4, 0.65, 0.7, 0.8, 0.9,  1.])
>>> prob_true, prob_pred = calibration_curve(y_true, y_pred, n_bins=3)
>>> prob_true
array([0. , 0.5, 1. ])
>>> prob_pred
array([0.2  , 0.525, 0.85 ])
```