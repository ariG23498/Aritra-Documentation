# RunObserver







Defines the interface for all run observers.



## Methods

<h3 id="artifact_event"><code>artifact_event</code></h3>

<pre><code>artifact_event(
    name, filename, metadata=None, content_type=None
)</code></pre>




<h3 id="completed_event"><code>completed_event</code></h3>

<pre><code>completed_event(
    stop_time, result
)</code></pre>




<h3 id="failed_event"><code>failed_event</code></h3>

<pre><code>failed_event(
    fail_time, fail_trace
)</code></pre>




<h3 id="heartbeat_event"><code>heartbeat_event</code></h3>

<pre><code>heartbeat_event(
    info, captured_out, beat_time, result
)</code></pre>




<h3 id="interrupted_event"><code>interrupted_event</code></h3>

<pre><code>interrupted_event(
    interrupt_time, status
)</code></pre>




<h3 id="join"><code>join</code></h3>

<pre><code>join()</code></pre>




<h3 id="log_metrics"><code>log_metrics</code></h3>

<pre><code>log_metrics(
    metrics_by_name, info
)</code></pre>




<h3 id="queued_event"><code>queued_event</code></h3>

<pre><code>queued_event(
    ex_info, command, host_info, queue_time, config, meta_info, _id
)</code></pre>




<h3 id="resource_event"><code>resource_event</code></h3>

<pre><code>resource_event(
    filename
)</code></pre>




<h3 id="started_event"><code>started_event</code></h3>

<pre><code>started_event(
    ex_info, command, host_info, start_time, config, meta_info, _id
)</code></pre>








<!-- Tabular view -->
<table>
<tr><th>Class Variables</th></tr>

<tr>
<td>
priority<a id="priority"></a>
</td>
<td>
<code>0</code>
</td>
</tr>
</table>

