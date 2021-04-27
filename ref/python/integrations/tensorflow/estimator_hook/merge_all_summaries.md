# merge_all_summaries







Merges all summaries collected in the default graph.

<pre><code>merge_all_summaries(
    key=tf.GraphKeys.SUMMARIES, scope=None, name=None
)</code></pre>





<!-- Tabular view -->
<table>
<tr><th>Args</th></tr>

<tr>
<td>
<code>key</code>
</td>
<td>
<code>GraphKey</code> used to collect the summaries.  Defaults to
<code>GraphKeys.SUMMARIES</code>.
</td>
</tr><tr>
<td>
<code>scope</code>
</td>
<td>
Optional scope used to filter the summary ops, using <code>re.match</code>
</td>
</tr>
</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
If no summaries were collected, returns None.  Otherwise returns a scalar
<code>Tensor</code> of type <code>string</code> containing the serialized <code>Summary</code> protocol
buffer resulting from the merging.
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Raises</th></tr>

<tr>
<td>
<code>RuntimeError</code>
</td>
<td>
If called with eager execution enabled.
</td>
</tr>
</table>


@compatibility(eager)
Not compatible with eager execution. To write TensorBoard
summaries under eager execution, use <code>tf.contrib.summary</code> instead.
@end_compatibility