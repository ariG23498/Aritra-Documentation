# CalibratedClassifierCV







Probability calibration with isotonic regression or logistic regression.

<pre><code>CalibratedClassifierCV(
    base_estimator=None, *, method=&#x27;sigmoid&#x27;, cv=None, n_jobs=None,
    ensemble=(True)
)</code></pre>




This class uses cross-validation to both estimate the parameters of a
classifier and subsequently calibrate a classifier. With default
<code>ensemble=True</code>, for each cv split it
fits a copy of the base estimator to the training subset, and calibrates it
using the testing subset. For prediction, predicted probabilities are
averaged across these individual calibrated classifiers. When
<code>ensemble=False</code>, cross-validation is used to obtain unbiased predictions,
via :func:`~sklearn.model_selection.cross_val_predict`, which are then
used for calibration. For prediction, the base estimator, trained using all
the data, is used. This is the method implemented when <code>probabilities=True</code>
for :mod:<code>sklearn.svm</code> estimators.

Already fitted classifiers can be calibrated via the parameter
`cv="prefit"`. In this case, no cross-validation is used and all provided
data is used for calibration. The user has to take care manually that data
for model fitting and calibration are disjoint.

The calibration is based on the :term:<code>decision_function</code> method of the
<code>base_estimator</code> if it exists, else on :term:<code>predict_proba</code>.

Read more in the :ref:`User Guide <calibration>`.

Parameters
----------
base_estimator : estimator instance, default=None
    The classifier whose output need to be calibrated to provide more
    accurate <code>predict_proba</code> outputs. The default classifier is
    a :class:`~sklearn.svm.LinearSVC`.

method : {'sigmoid', 'isotonic'}, default='sigmoid'
    The method to use for calibration. Can be 'sigmoid' which
    corresponds to Platt's method (i.e. a logistic regression model) or
    'isotonic' which is a non-parametric approach. It is not advised to
    use isotonic calibration with too few calibration samples
    ``(<<1000)`` since it tends to overfit.

cv : int, cross-validation generator, iterable or "prefit",             default=None
    Determines the cross-validation splitting strategy.
    Possible inputs for cv are:

    - None, to use the default 5-fold cross-validation,
    - integer, to specify the number of folds.
    - :term:<code>CV splitter</code>,
    - An iterable yielding (train, test) splits as arrays of indices.

    For integer/None inputs, if `<code>y</code>` is binary or multiclass,
    :class:`~sklearn.model_selection.StratifiedKFold<code> is used. If </code><code>y</code>` is
    neither binary nor multiclass, :class:`~sklearn.model_selection.KFold`
    is used.

    Refer to the :ref:`User Guide <cross_validation>` for the various
    cross-validation strategies that can be used here.

    If "prefit" is passed, it is assumed that <code>base_estimator</code> has been
    fitted already and all data is used for calibration.

    .. versionchanged:: 0.22
        `<code>cv</code>` default value if None changed from 3-fold to 5-fold.

n_jobs : int, default=None
    Number of jobs to run in parallel.
    `<code>None</code>` means 1 unless in a :obj:<code>joblib.parallel_backend</code> context.
    ``-1`` means using all processors.

    Base estimator clones are fitted in parallel across cross-validation
    iterations. Therefore parallelism happens only when `cv != "prefit"`.

    See :term:`Glossary <n_jobs>` for more details.

    .. versionadded:: 0.24

ensemble : bool, default=True
    Determines how the calibrator is fitted when <code>cv</code> is not `'prefit'`.
    Ignored if `cv='prefit'`.

    If <code>True</code>, the <code>base_estimator</code> is fitted using training data and
    calibrated using testing data, for each <code>cv</code> fold. The final estimator
    is an ensemble of <code>n_cv</code> fitted classifer and calibrator pairs, where
    <code>n_cv</code> is the number of cross-validation folds. The output is the
    average predicted probabilities of all pairs.

    If <code>False</code>, <code>cv</code> is used to compute unbiased predictions, via
    :func:`~sklearn.model_selection.cross_val_predict`, which are then
    used for calibration. At prediction time, the classifier used is the
    <code>base_estimator</code> trained on all the data.
    Note that this method is also internally implemented  in
    :mod:<code>sklearn.svm</code> estimators with the <code>probabilities=True</code> parameter.

    .. versionadded:: 0.24

Attributes
----------
classes_ : ndarray of shape (n_classes,)
    The class labels.

calibrated_classifiers_ : list (len() equal to cv or 1 if `cv="prefit"<code>             or </code>ensemble=False`)
    The list of classifier and calibrator pairs.

    - When `cv="prefit"<code>, the fitted </code>base_estimator` and fitted
      calibrator.
    - When <code>cv</code> is not "prefit" and <code>ensemble=True</code>, <code>n_cv</code> fitted
      <code>base_estimator</code> and calibrator pairs. <code>n_cv</code> is the number of
      cross-validation folds.
    - When <code>cv</code> is not "prefit" and <code>ensemble=False</code>, the <code>base_estimator</code>,
      fitted on all the data, and fitted calibrator.

    .. versionchanged:: 0.24
        Single calibrated classifier case when <code>ensemble=False</code>.

Examples
--------
```
>>> from sklearn.datasets import make_classification
>>> from sklearn.naive_bayes import GaussianNB
>>> from sklearn.calibration import CalibratedClassifierCV
>>> X, y = make_classification(n_samples=100, n_features=2,
...                            n_redundant=0, random_state=42)
>>> base_clf = GaussianNB()
>>> calibrated_clf = CalibratedClassifierCV(base_estimator=base_clf, cv=3)
>>> calibrated_clf.fit(X, y)
CalibratedClassifierCV(base_estimator=GaussianNB(), cv=3)
>>> len(calibrated_clf.calibrated_classifiers_)
3
>>> calibrated_clf.predict_proba(X)[:5, :]
array([[0.110..., 0.889...],
       [0.072..., 0.927...],
       [0.928..., 0.071...],
       [0.928..., 0.071...],
       [0.071..., 0.928...]])
```

```
>>> from sklearn.model_selection import train_test_split
>>> X, y = make_classification(n_samples=100, n_features=2,
...                            n_redundant=0, random_state=42)
>>> X_train, X_calib, y_train, y_calib = train_test_split(
...        X, y, random_state=42
... )
>>> base_clf = GaussianNB()
>>> base_clf.fit(X_train, y_train)
GaussianNB()
>>> calibrated_clf = CalibratedClassifierCV(
...     base_estimator=base_clf,
...     cv="prefit"
... )
>>> calibrated_clf.fit(X_calib, y_calib)
CalibratedClassifierCV(base_estimator=GaussianNB(), cv='prefit')
>>> len(calibrated_clf.calibrated_classifiers_)
1
>>> calibrated_clf.predict_proba([[-0.5, 0.5]])
array([[0.936..., 0.063...]])
```

References
----------
.. [1] Obtaining calibrated probability estimates from decision trees
       and naive Bayesian classifiers, B. Zadrozny & C. Elkan, ICML 2001

.. [2] Transforming Classifier Scores into Accurate Multiclass
       Probability Estimates, B. Zadrozny & C. Elkan, (KDD 2002)

.. [3] Probabilistic Outputs for Support Vector Machines and Comparisons to
       Regularized Likelihood Methods, J. Platt, (1999)

.. [4] Predicting Good Probabilities with Supervised Learning,
       A. Niculescu-Mizil & R. Caruana, ICML 2005

## Methods

<h3 id="fit"><code>fit</code></h3>

<pre><code>fit(
    X, y, sample_weight=None
)</code></pre>

Fit the calibrated model.

Parameters
----------
X : array-like of shape (n_samples, n_features)
    Training data.

y : array-like of shape (n_samples,)
    Target values.

sample_weight : array-like of shape (n_samples,), default=None
    Sample weights. If None, then samples are equally weighted.

Returns
-------
self : object
    Returns an instance of self.

<h3 id="get_params"><code>get_params</code></h3>

<pre><code>get_params(
    deep=(True)
)</code></pre>

Get parameters for this estimator.

Parameters
----------
deep : bool, default=True
    If True, will return the parameters for this estimator and
    contained subobjects that are estimators.

Returns
-------
params : dict
    Parameter names mapped to their values.

<h3 id="predict"><code>predict</code></h3>

<pre><code>predict(
    X
)</code></pre>

Predict the target of new samples. The predicted class is the
class that has the highest probability, and can thus be different
from the prediction of the uncalibrated classifier.

Parameters
----------
X : array-like of shape (n_samples, n_features)
    The samples.

Returns
-------
C : ndarray of shape (n_samples,)
    The predicted class.

<h3 id="predict_proba"><code>predict_proba</code></h3>

<pre><code>predict_proba(
    X
)</code></pre>

Calibrated probabilities of classification.

This function returns calibrated probabilities of classification
according to each class on an array of test vectors X.

Parameters
----------
X : array-like of shape (n_samples, n_features)
    The samples.

Returns
-------
C : ndarray of shape (n_samples, n_classes)
    The predicted probas.

<h3 id="score"><code>score</code></h3>

<pre><code>score(
    X, y, sample_weight=None
)</code></pre>

Return the mean accuracy on the given test data and labels.

In multi-label classification, this is the subset accuracy
which is a harsh metric since you require for each sample that
each label set be correctly predicted.

Parameters
----------
X : array-like of shape (n_samples, n_features)
    Test samples.

y : array-like of shape (n_samples,) or (n_samples, n_outputs)
    True labels for <code>X</code>.

sample_weight : array-like of shape (n_samples,), default=None
    Sample weights.

Returns
-------
score : float
    Mean accuracy of `<code>self.predict(X)</code><code> wrt. </code>y`.

<h3 id="set_params"><code>set_params</code></h3>

<pre><code>set_params(
    **params
)</code></pre>

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects
(such as :class:`~sklearn.pipeline.Pipeline`). The latter have
parameters of the form ``<component>__<parameter>`` so that it's
possible to update each component of a nested object.

Parameters
----------
**params : dict
    Estimator parameters.

Returns
-------
self : estimator instance
    Estimator instance.



