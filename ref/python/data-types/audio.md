# Audio



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L877-L1021)



Wandb class for audio clips.

```python
Audio(
    data_or_path, sample_rate=None, caption=None
)
```





| Arguments |  |
| :--- | :--- |
|  `data_or_path` |  (string or numpy array) A path to an audio file or a numpy array of audio data. |
|  `sample_rate` |  (int) Sample rate, required when passing in raw numpy array of audio data. |
|  `caption` |  (string) Caption to display with audio. |



## Methods

<h3 id="durations"><code>durations</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L979-L981)

```python
@classmethod
durations(
    audio_list
)
```




<h3 id="path_is_reference"><code>path_is_reference</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L922-L924)

```python
@classmethod
path_is_reference(
    path
)
```




<h3 id="resolve_ref"><code>resolve_ref</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L995-L1007)

```python
resolve_ref()
```




<h3 id="sample_rates"><code>sample_rates</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L983-L985)

```python
@classmethod
sample_rates(
    audio_list
)
```






