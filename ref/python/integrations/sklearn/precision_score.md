# precision_score







Compute the precision.

<pre><code>precision_score(
    y_true, y_pred, *, labels=None, pos_label=1, average=&#x27;binary&#x27;,
    sample_weight=None, zero_division=&#x27;warn&#x27;
)</code></pre>




The precision is the ratio ``tp / (tp + fp)`<code> where </code><code>tp</code>` is the number of
true positives and `<code>fp</code>` the number of false positives. The precision is
intuitively the ability of the classifier not to label as positive a sample
that is negative.

The best value is 1 and the worst value is 0.

Read more in the :ref:`User Guide <precision_recall_f_measure_metrics>`.

Parameters
----------
y_true : 1d array-like, or label indicator array / sparse matrix
    Ground truth (correct) target values.

y_pred : 1d array-like, or label indicator array / sparse matrix
    Estimated targets as returned by a classifier.

labels : array-like, default=None
    The set of labels to include when ``average != 'binary'``, and their
    order if `<code>average is None</code>`. Labels present in the data can be
    excluded, for example to calculate a multiclass average ignoring a
    majority negative class, while labels not present in the data will
    result in 0 components in a macro average. For multilabel targets,
    labels are column indices. By default, all labels in `<code>y_true</code>` and
    `<code>y_pred</code>` are used in sorted order.

    .. versionchanged:: 0.17
       Parameter <code>labels</code> improved for multiclass problem.

pos_label : str or int, default=1
    The class to report if ``average='binary'`` and the data is binary.
    If the data are multiclass or multilabel, this will be ignored;
    setting `<code>labels=[pos_label]</code><code> and </code>`average != 'binary'`` will report
    scores for that label only.

average : {'micro', 'macro', 'samples', 'weighted', 'binary'}             default='binary'
    This parameter is required for multiclass/multilabel targets.
    If `<code>None</code>`, the scores for each class are returned. Otherwise, this
    determines the type of averaging performed on the data:

    ``'binary'``:
        Only report results for the class specified by `<code>pos_label</code>`.
        This is applicable only if targets (`<code>y_{true,pred}</code>`) are binary.
    ``'micro'``:
        Calculate metrics globally by counting the total true positives,
        false negatives and false positives.
    ``'macro'``:
        Calculate metrics for each label, and find their unweighted
        mean.  This does not take label imbalance into account.
    ``'weighted'``:
        Calculate metrics for each label, and find their average weighted
        by support (the number of true instances for each label). This
        alters 'macro' to account for label imbalance; it can result in an
        F-score that is not between precision and recall.
    ``'samples'``:
        Calculate metrics for each instance, and find their average (only
        meaningful for multilabel classification where this differs from
        :func:<code>accuracy_score</code>).

sample_weight : array-like of shape (n_samples,), default=None
    Sample weights.

zero_division : "warn", 0 or 1, default="warn"
    Sets the value to return when there is a zero division. If set to
    "warn", this acts as 0, but warnings are also raised.

Returns
-------
precision : float (if average is not None) or array of float of shape
    (n_unique_labels,)
    Precision of the positive class in binary classification or weighted
    average of the precision of each class for the multiclass task.

See Also
--------
precision_recall_fscore_support, multilabel_confusion_matrix

Notes
-----
When ``true positive + false positive == 0``, precision returns 0 and
raises `<code>UndefinedMetricWarning</code>`. This behavior can be
modified with `<code>zero_division</code>`.

Examples
--------
```
>>> from sklearn.metrics import precision_score
>>> y_true = [0, 1, 2, 0, 1, 2]
>>> y_pred = [0, 2, 1, 0, 0, 1]
>>> precision_score(y_true, y_pred, average='macro')
0.22...
>>> precision_score(y_true, y_pred, average='micro')
0.33...
>>> precision_score(y_true, y_pred, average='weighted')
0.22...
>>> precision_score(y_true, y_pred, average=None)
array([0.66..., 0.        , 0.        ])
>>> y_pred = [0, 0, 0, 0, 0, 0]
>>> precision_score(y_true, y_pred, average=None)
array([0.33..., 0.        , 0.        ])
>>> precision_score(y_true, y_pred, average=None, zero_division=1)
array([0.33..., 1.        , 1.        ])
```