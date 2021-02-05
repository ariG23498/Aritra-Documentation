# Image

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1638-L2053)




Wandb class for images.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>Data Types.Image(
    data_or_path, mode=None, caption=None, grouping=None, classes=None, boxes=None,
    masks=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>data_or_path</code>
</td>
<td>
(numpy array, string, io) Accepts numpy array of
image data, or a PIL image. The class attempts to infer
the data format and converts it.
</td>
</tr><tr>
<td>
<code>mode</code>
</td>
<td>
(string) The PIL mode for an image. Most common are "L", "RGB",
"RGBA". Full explanation at https://pillow.readthedocs.io/en/4.2.x/handbook/concepts.html#concept-modes.
</td>
</tr><tr>
<td>
<code>caption</code>
</td>
<td>
(string) Label for display of image.
</td>
</tr>
</table>



## Methods

<h3 id="all_boxes"><code>all_boxes</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L2018-L2033">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>all_boxes(
    images, run, run_key, step
)
</code></pre>




<h3 id="all_captions"><code>all_captions</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L2035-L2040">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>all_captions(
    images
)
</code></pre>




<h3 id="all_masks"><code>all_masks</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L2001-L2016">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>all_masks(
    images, run, run_key, step
)
</code></pre>




<h3 id="guess_mode"><code>guess_mode</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1903-L1917">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>guess_mode(
    data
)
</code></pre>

Guess what type of image the np.array is representing


<h3 id="to_uint8"><code>to_uint8</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1919-L1941">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>to_uint8(
    data
)
</code></pre>

Converts floating point image on the range [0,1] and integer images
on the range [0,255] to uint8, clipping if necessary.





<!-- Tabular view -->
<table>
<tr><th>Class Variables</th></tr>

<tr>
<td>
MAX_DIMENSION<a id="MAX_DIMENSION"></a>
</td>
<td>
`65500`
</td>
</tr><tr>
<td>
MAX_ITEMS<a id="MAX_ITEMS"></a>
</td>
<td>
`108`
</td>
</tr><tr>
<td>
artifact_type<a id="artifact_type"></a>
</td>
<td>
`'image-file'`
</td>
</tr>
</table>
