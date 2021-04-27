# WandbHook



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/integration/tensorflow/estimator_hook.py#L25-L46)




Hook to extend calls to MonitoredSession.run().

Inherits From: [`SessionRunHook`](../../integrations/tensorflow/estimator_hook/SessionRunHook.md)

<pre><code>WandbHook(
    summary_op=None, steps_per_log=1000, history=None
)</code></pre>





## Methods

<h3 id="after_create_session"><code>after_create_session</code></h3>

<pre><code>after_create_session(
    session, coord
)</code></pre>

Called when new TensorFlow session is created.

This is called to signal the hooks that a new session has been created. This
has two essential differences with the situation in which <code>begin</code> is called:

* When this is called, the graph is finalized and ops can no longer be added
    to the graph.
* This method will also be called as a result of recovering a wrapped
    session, not only at the beginning of the overall session.

<!-- Tabular view -->
<table>
<tr><th>Args</th></tr>

<tr>
<td>
<code>session</code>
</td>
<td>
A TensorFlow Session that has been created.
</td>
</tr><tr>
<td>
<code>coord</code>
</td>
<td>
A Coordinator object which keeps track of all threads.
</td>
</tr>
</table>



<h3 id="after_run"><code>after_run</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/v0.10.27/wandb/integration/tensorflow/estimator_hook.py#L41-L46">View source</a>

<pre><code>after_run(
    run_context, run_values
)</code></pre>

Called after each call to run().

The <code>run_values</code> argument contains results of requested ops/tensors by
<code>before_run()</code>.

The <code>run_context</code> argument is the same one send to <code>before_run</code> call.
<code>run_context.request_stop()</code> can be called to stop the iteration.

If <code>session.run()</code> raises any exceptions then <code>after_run()</code> is not called.

<!-- Tabular view -->
<table>
<tr><th>Args</th></tr>

<tr>
<td>
<code>run_context</code>
</td>
<td>
A <code>SessionRunContext</code> object.
</td>
</tr><tr>
<td>
<code>run_values</code>
</td>
<td>
A SessionRunValues object.
</td>
</tr>
</table>



<h3 id="before_run"><code>before_run</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/v0.10.27/wandb/integration/tensorflow/estimator_hook.py#L36-L39">View source</a>

<pre><code>before_run(
    run_context
)</code></pre>

Called before each call to run().

You can return from this call a <code>SessionRunArgs</code> object indicating ops or
tensors to add to the upcoming <code>run()</code> call.  These ops/tensors will be run
together with the ops/tensors originally passed to the original run() call.
The run args you return can also contain feeds to be added to the run()
call.

The <code>run_context</code> argument is a <code>SessionRunContext</code> that provides
information about the upcoming <code>run()</code> call: the originally requested
op/tensors, the TensorFlow Session.

At this point graph is finalized and you can not add ops.

<!-- Tabular view -->
<table>
<tr><th>Args</th></tr>

<tr>
<td>
<code>run_context</code>
</td>
<td>
A <code>SessionRunContext</code> object.
</td>
</tr>
</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
None or a <code>SessionRunArgs</code> object.
</td>
</tr>

</table>



<h3 id="begin"><code>begin</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/v0.10.27/wandb/integration/tensorflow/estimator_hook.py#L31-L34">View source</a>

<pre><code>begin()</code></pre>

Called once before using the session.

When called, the default graph is the one that will be launched in the
session.  The hook can modify the graph by adding new operations to it.
After the <code>begin()</code> call the graph will be finalized and the other callbacks
can not modify the graph anymore. Second call of <code>begin()</code> on the same
graph, should not change the graph.

<h3 id="end"><code>end</code></h3>

<pre><code>end(
    session
)</code></pre>

Called at the end of session.

The <code>session</code> argument can be used in case the hook wants to run final ops,
such as saving a last checkpoint.

If <code>session.run()</code> raises exception other than OutOfRangeError or
StopIteration then <code>end()</code> is not called.
Note the difference between <code>end()</code> and <code>after_run()</code> behavior when
<code>session.run()</code> raises OutOfRangeError or StopIteration. In that case
<code>end()</code> is called but <code>after_run()</code> is not called.

<!-- Tabular view -->
<table>
<tr><th>Args</th></tr>

<tr>
<td>
<code>session</code>
</td>
<td>
A TensorFlow Session that will be soon closed.
</td>
</tr>
</table>





