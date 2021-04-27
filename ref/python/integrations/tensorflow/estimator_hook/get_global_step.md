# get_global_step







Get the global step tensor.

<pre><code>get_global_step(
    graph=None
)</code></pre>




The global step tensor must be an integer variable. We first try to find it
in the collection <code>GLOBAL_STEP</code>, or by name `global_step:0`.

<!-- Tabular view -->
<table>
<tr><th>Args</th></tr>

<tr>
<td>
<code>graph</code>
</td>
<td>
The graph to find the global step in. If missing, use default graph.
</td>
</tr>
</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
The global step variable, or <code>None</code> if none was found.
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Raises</th></tr>

<tr>
<td>
<code>TypeError</code>
</td>
<td>
If the global step tensor has a non-integer type, or if it is not
a <code>Variable</code>.
</td>
</tr>
</table>

