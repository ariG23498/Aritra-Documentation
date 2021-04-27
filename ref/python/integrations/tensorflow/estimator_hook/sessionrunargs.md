# SessionRunArgs







Represents arguments to be added to a <code>Session.run()</code> call.

<pre><code>SessionRunArgs(
    fetches, feed_dict=None, options=None
)</code></pre>





<!-- Tabular view -->
<table>
<tr><th>Args</th></tr>

<tr>
<td>
<code>fetches</code>
</td>
<td>
Exactly like the 'fetches' argument to Session.Run().
Can be a single tensor or op, a list of 'fetches' or a dictionary
of fetches.  For example:
fetches = global_step_tensor
fetches = [train_op, summary_op, global_step_tensor]
fetches = {'step': global_step_tensor, 'summ': summary_op}
Note that this can recurse as expected:
fetches = {'step': global_step_tensor,
'ops': [train_op, check_nan_op]}
</td>
</tr><tr>
<td>
<code>feed_dict</code>
</td>
<td>
Exactly like the <code>feed_dict</code> argument to <code>Session.Run()</code>
</td>
</tr><tr>
<td>
<code>options</code>
</td>
<td>
Exactly like the <code>options</code> argument to <code>Session.run()</code>, i.e., a
config_pb2.RunOptions proto.
</td>
</tr>
</table>





<!-- Tabular view -->
<table>
<tr><th>Attributes</th></tr>


</table>





<!-- Tabular view -->
<table>
<tr><th>Class Variables</th></tr>

<tr>
<td>
feed_dict<a id="feed_dict"></a>
</td>
<td>

</td>
</tr><tr>
<td>
fetches<a id="fetches"></a>
</td>
<td>

</td>
</tr><tr>
<td>
options<a id="options"></a>
</td>
<td>

</td>
</tr>
</table>

