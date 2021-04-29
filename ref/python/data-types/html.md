# Html



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.28/wandb/sdk/data_types.py#L875-L965)




Wandb class for arbitrary html

```python
Html(
    data: Union[str, 'TextIO'],
    inject: bool = (True)
) -> None
```





<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>data</code>
</td>
<td>
(string or io object) HTML to display in wandb
</td>
</tr><tr>
<td>
<code>inject</code>
</td>
<td>
(boolean) Add a stylesheet to the HTML object.  If set
to False the HTML will pass through unchanged.
</td>
</tr>
</table>



## Methods

<h3 id="inject_head"><code>inject_head</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/v0.10.28/wandb/sdk/data_types.py#L917-L932">View source</a>

```python
inject_head() -> None
```






