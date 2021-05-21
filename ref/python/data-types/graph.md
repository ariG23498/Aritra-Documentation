# Graph



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L1217-L1377)



Wandb class for graphs

```python
Graph(
    format="keras"
)
```




This class is typically used for saving and diplaying neural net models.  It
represents the graph as an array of nodes and edges.  The nodes can have
labels that can be visualized by wandb.

#### Examples:

Import a keras model:
```
    Graph.from_keras(keras_model)
```



## Methods

<h3 id="add_edge"><code>add_edge</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L1303-L1307)

```python
add_edge(
    from_node, to_node
)
```




<h3 id="add_node"><code>add_node</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L1289-L1301)

```python
add_node(
    node=None, **node_kwargs
)
```




<h3 id="from_keras"><code>from_keras</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L1309-L1338)

```python
@classmethod
from_keras(
    model
)
```




<h3 id="pprint"><code>pprint</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L1283-L1287)

```python
pprint()
```




<h3 id="__getitem__"><code>__getitem__</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L1280-L1281)

```python
__getitem__(
    nid
)
```






