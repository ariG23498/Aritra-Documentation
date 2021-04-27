# LabelEncoder







Encode target labels with value between 0 and n_classes-1.


This transformer should be used to encode target values, *i.e.* <code>y</code>, and
not the input <code>X</code>.

Read more in the :ref:`User Guide <preprocessing_targets>`.

.. versionadded:: 0.12

Attributes
----------
classes_ : ndarray of shape (n_classes,)
    Holds the label for each class.

Examples
--------
<code>LabelEncoder</code> can be used to normalize labels.

```
>>> from sklearn import preprocessing
>>> le = preprocessing.LabelEncoder()
>>> le.fit([1, 2, 2, 6])
LabelEncoder()
>>> le.classes_
array([1, 2, 6])
>>> le.transform([1, 1, 2, 6])
array([0, 0, 1, 2]...)
>>> le.inverse_transform([0, 0, 1, 2])
array([1, 1, 2, 6])
```

It can also be used to transform non-numerical labels (as long as they are
hashable and comparable) to numerical labels.

```
>>> le = preprocessing.LabelEncoder()
>>> le.fit(["paris", "paris", "tokyo", "amsterdam"])
LabelEncoder()
>>> list(le.classes_)
['amsterdam', 'paris', 'tokyo']
>>> le.transform(["tokyo", "tokyo", "paris"])
array([2, 2, 1]...)
>>> list(le.inverse_transform([2, 2, 1]))
['tokyo', 'tokyo', 'paris']
```

See Also
--------
OrdinalEncoder : Encode categorical features using an ordinal encoding
    scheme.
OneHotEncoder : Encode categorical features as a one-hot numeric array.

## Methods

<h3 id="fit"><code>fit</code></h3>

<pre><code>fit(
    y
)</code></pre>

Fit label encoder.

Parameters
----------
y : array-like of shape (n_samples,)
    Target values.

Returns
-------
self : returns an instance of self.

<h3 id="fit_transform"><code>fit_transform</code></h3>

<pre><code>fit_transform(
    y
)</code></pre>

Fit label encoder and return encoded labels.

Parameters
----------
y : array-like of shape (n_samples,)
    Target values.

Returns
-------
y : array-like of shape (n_samples,)

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

<h3 id="inverse_transform"><code>inverse_transform</code></h3>

<pre><code>inverse_transform(
    y
)</code></pre>

Transform labels back to original encoding.

Parameters
----------
y : ndarray of shape (n_samples,)
    Target values.

Returns
-------
y : ndarray of shape (n_samples,)

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

<h3 id="transform"><code>transform</code></h3>

<pre><code>transform(
    y
)</code></pre>

Transform labels to normalized encoding.

Parameters
----------
y : array-like of shape (n_samples,)
    Target values.

Returns
-------
y : array-like of shape (n_samples,)



