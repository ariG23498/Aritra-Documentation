# Run

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L810-L1317)




A single run associated with an entity and project.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>Api.Run(
    client, entity, project, run_id, attrs={}
)
</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
<table>
<tr><th>Attributes</th></tr>

<tr>
<td>
<code>entity</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>id</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>json_config</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>lastHistoryStep</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>name</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>path</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>storage_id</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>summary</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>url</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>username</code>
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="create"><code>create</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L892-L932">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>create(
    api, run_id=None, project=None, entity=None
)
</code></pre>

Create a run for the given project


<h3 id="file"><code>file</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1087-L1096">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>file(
    name
)
</code></pre>

Arguments:
    name (str): name of requested file.

<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
A `File` matching the name argument.
</td>
</tr>

</table>



<h3 id="files"><code>files</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1075-L1085">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>files(
    names=[], per_page=50
)
</code></pre>

Arguments:
    names (list): names of the requested files, if empty returns all files
    per_page (int): number of results per page

<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
A `Files` object, which is an iterator over `File` obejcts.
</td>
</tr>

</table>



<h3 id="history"><code>history</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1121-L1153">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>history(
    samples=500, keys=None, x_axis=&#x27;_step&#x27;, pandas=True,
    stream=&#x27;default&#x27;
)
</code></pre>

Returns sampled history metrics for a run.  This is simpler and faster if you are ok with
the history records being sampled.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
samples (int, optional): The number of samples to return
pandas (bool, optional): Return a pandas dataframe
keys (list, optional): Only return metrics for specific keys
x_axis (str, optional): Use this metric as the xAxis defaults to _step
stream (str, optional): "default" for metrics, "system" for machine metrics
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
If pandas=True returns a `pandas.DataFrame` of history metrics.
If pandas=False returns a list of dicts of history metrics.
</td>
</tr>

</table>



<h3 id="load"><code>load</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L934-L996">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>load(
    force=False
)
</code></pre>




<h3 id="log_artifact"><code>log_artifact</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1239-L1271">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>log_artifact(
    artifact, aliases=None
)
</code></pre>

Declare an artifact as output of a run.


<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
artifact (`Artifact`): An artifact returned from
`wandb.Api().artifact(name)`
aliases (list, optional): Aliases to apply to this artifact
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
A `Artifact` object.
</td>
</tr>

</table>



<h3 id="logged_artifacts"><code>logged_artifacts</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1204-L1206">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>logged_artifacts(
    per_page=100
)
</code></pre>




<h3 id="save"><code>save</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1027-L1028">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>save()
</code></pre>




<h3 id="scan_history"><code>scan_history</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1155-L1202">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>scan_history(
    keys=None, page_size=1000, min_step=None, max_step=None
)
</code></pre>

Returns an iterable collection of all history records for a run.


#### Example:

Export all the loss values for an example run

```python
run = api.run("l2k2/examples-numpy-boston/i0wt6xua")
history = run.scan_history(keys=["Loss"])
losses = [row["Loss"] for row in history]
```




<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
keys ([str], optional): only fetch these keys, and only fetch rows that have all of keys defined.
page_size (int, optional): size of pages to fetch from the api
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
An iterable collection over history records (dict).
</td>
</tr>

</table>



<h3 id="snake_to_camel"><code>snake_to_camel</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L528-L530">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>snake_to_camel(
    string
)
</code></pre>




<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L998-L1025">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update()
</code></pre>

Persists changes to the run object to the wandb backend.


<h3 id="upload_file"><code>upload_file</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1098-L1119">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>upload_file(
    path, root=&#x27;.&#x27;
)
</code></pre>

Arguments:
    path (str): name of file to upload.
    root (str): the root path to save the file relative to.  i.e.
        If you want to have the file saved in the run as "my_dir/file.txt"
        and you're currently in "my_dir" you would set root to "../"

<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
A `File` matching the name argument.
</td>
</tr>

</table>



<h3 id="use_artifact"><code>use_artifact</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1212-L1237">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>use_artifact(
    artifact
)
</code></pre>

Declare an artifact as an input to a run.


<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
artifact (`Artifact`): An artifact returned from
`wandb.Api().artifact(name)`
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
A `Artifact` object.
</td>
</tr>

</table>



<h3 id="used_artifacts"><code>used_artifacts</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1208-L1210">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>used_artifacts(
    per_page=100
)
</code></pre>





