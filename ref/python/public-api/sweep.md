# Sweep



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.28/wandb/apis/public.py#L1403-L1586)




A set of runs associated with a sweep.

```python
Sweep(
    client, entity, project, sweep_id, attrs={}
)
```





#### Examples:

Instantiate with:
```
api = wandb.Api()
sweep = api.sweep(path/to/sweep)
```





<!-- Tabular view -->
<table>
<tr><th>Attributes</th></tr>

<tr>
<td>
<code>runs</code>
</td>
<td>
(<code>Runs</code>) list of runs
</td>
</tr><tr>
<td>
<code>id</code>
</td>
<td>
(str) sweep id
</td>
</tr><tr>
<td>
<code>project</code>
</td>
<td>
(str) name of project
</td>
</tr><tr>
<td>
<code>config</code>
</td>
<td>
(str) dictionary of sweep configuration
</td>
</tr>
</table>



## Methods

<h3 id="best_run"><code>best_run</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/v0.10.28/wandb/apis/public.py#L1494-L1517">View source</a>

```python
best_run(
    order=None
)
```

Returns the best run sorted by the metric defined in config or the order passed in


<h3 id="get"><code>get</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/v0.10.28/wandb/apis/public.py#L1533-L1583">View source</a>

```python
@classmethod
```
```python
get(
    client, entity=None, project=None, sid=None, withRuns=(True), order=None,
    query=None, **kwargs
)
```

Execute a query against the cloud backend


<h3 id="load"><code>load</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/v0.10.28/wandb/apis/public.py#L1474-L1483">View source</a>

```python
load(
    force=(False)
)
```




<h3 id="snake_to_camel"><code>snake_to_camel</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/v0.10.28/wandb/apis/public.py#L561-L563">View source</a>

```python
snake_to_camel(
    string
)
```








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

