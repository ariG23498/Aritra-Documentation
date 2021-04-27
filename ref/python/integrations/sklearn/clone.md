# clone







Constructs a new unfitted estimator with the same parameters.

<pre><code>clone(
    estimator, *, safe=(True)
)</code></pre>




Clone does a deep copy of the model in an estimator
without actually copying attached data. It yields a new estimator
with the same parameters that has not been fitted on any data.

If the estimator's <code>random_state</code> parameter is an integer (or if the
estimator doesn't have a <code>random_state</code> parameter), an *exact clone* is
returned: the clone and the original estimator will give the exact same
results. Otherwise, *statistical clone* is returned: the clone might
yield different results from the original estimator. More details can be
found in :ref:<code>randomness</code>.

Parameters
----------
estimator : {list, tuple, set} of estimator instance or a single             estimator instance
    The estimator or group of estimators to be cloned.

safe : bool, default=True
    If safe is False, clone will fall back to a deep copy on objects
    that are not estimators.