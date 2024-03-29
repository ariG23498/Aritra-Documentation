# Html



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/sdk/data_types.py#L876-L966)



Wandb class for arbitrary html

```python
Html(
    data: Union[str, 'TextIO'],
    inject: bool = (True)
) -> None
```





| Arguments |  |
| :--- | :--- |
|  `data` |  (string or io object) HTML to display in wandb |
|  `inject` |  (boolean) Add a stylesheet to the HTML object. If set to False the HTML will pass through unchanged. |



## Methods

<h3 id="inject_head"><code>inject_head</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/sdk/data_types.py#L918-L933)

```python
inject_head() -> None
```






