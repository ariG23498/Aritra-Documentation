# type_of_target







Determine the type of data indicated by the target.

<pre><code>type_of_target(
    y
)</code></pre>




Note that this type is the most specific type that can be inferred.
For example:

    * `<code>binary</code><code> is more specific but compatible with </code><code>multiclass</code>`.
    * `<code>multiclass</code>` of integers is more specific but compatible with
      `<code>continuous</code>`.
    * ``multilabel-indicator`` is more specific but compatible with
      ``multiclass-multioutput``.

Parameters
----------
y : array-like

Returns
-------
target_type : str
    One of:

    * 'continuous': <code>y</code> is an array-like of floats that are not all
      integers, and is 1d or a column vector.
    * 'continuous-multioutput': <code>y</code> is a 2d array of floats that are
      not all integers, and both dimensions are of size > 1.
    * 'binary': <code>y</code> contains <= 2 discrete values and is 1d or a column
      vector.
    * 'multiclass': <code>y</code> contains more than two discrete values, is not a
      sequence of sequences, and is 1d or a column vector.
    * 'multiclass-multioutput': <code>y</code> is a 2d array that contains more
      than two discrete values, is not a sequence of sequences, and both
      dimensions are of size > 1.
    * 'multilabel-indicator': <code>y</code> is a label indicator matrix, an array
      of two dimensions with at least two columns, and at most 2 unique
      values.
    * 'unknown': <code>y</code> is array-like but none of the above, such as a 3d
      array, sequence of sequences, or an array of non-sequence objects.

Examples
--------
```
>>> import numpy as np
>>> type_of_target([0.1, 0.6])
'continuous'
>>> type_of_target([1, -1, -1, 1])
'binary'
>>> type_of_target(['a', 'b', 'a'])
'binary'
>>> type_of_target([1.0, 2.0])
'binary'
>>> type_of_target([1, 0, 2])
'multiclass'
>>> type_of_target([1.0, 0.0, 3.0])
'multiclass'
>>> type_of_target(['a', 'b', 'c'])
'multiclass'
>>> type_of_target(np.array([[1, 2], [3, 1]]))
'multiclass-multioutput'
>>> type_of_target([[1, 2]])
'multilabel-indicator'
>>> type_of_target(np.array([[1.5, 2.0], [3.0, 1.6]]))
'continuous-multioutput'
>>> type_of_target(np.array([[0, 1], [1, 1]]))
'multilabel-indicator'
```