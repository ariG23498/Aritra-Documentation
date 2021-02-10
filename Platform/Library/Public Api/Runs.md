# Runs

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L705-L807)




An iterable collection of runs associated with a project and optional filter.

<pre><code>Runs(
    client, entity, project, filters={}, order=None, per_page=50
)</code></pre>



<!-- Placeholder for "Used in" -->
This is generally used indirectly via the `Api`.runs method



<!-- Tabular view -->
<table>
<tr><th>Attributes</th></tr>

<tr>
<td>
<code>cursor</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>length</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>more</code>
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="convert_objects"><code>convert_objects</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L770-L804">View source</a>

<pre><code>convert_objects()</code></pre>




<h3 id="next"><code>next</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L605-L612">View source</a>

<pre><code>next()</code></pre>




<h3 id="update_variables"><code>update_variables</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L586-L587">View source</a>

<pre><code>update_variables()</code></pre>




<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L599-L603">View source</a>

<pre><code>__getitem__(
    index
)</code></pre>




<h3 id="__iter__"><code>__iter__</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L560-L562">View source</a>

<pre><code>__iter__()</code></pre>




<h3 id="__len__"><code>__len__</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L564-L569">View source</a>

<pre><code>__len__()</code></pre>








<!-- Tabular view -->
<table>
<tr><th>Class Variables</th></tr>

<tr>
<td>
QUERY<a id="QUERY"></a>
</td>
<td>

</td>
</tr>
</table>
