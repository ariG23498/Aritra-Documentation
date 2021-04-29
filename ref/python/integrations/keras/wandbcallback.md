# wandb.integration.wandbcallback

[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L214-L885)

WandbCallback automatically integrates keras with wandb.

```text
WandbCallback(
    monitor='val_loss', verbose=0, mode='auto',
    save_weights_only=(False), log_weights=(False), log_gradients=(False),
    save_model=(True), training_data=None, validation_data=None, labels=[],
    data_type=None, predictions=36, generator=None, input_type=None,
    output_type=None, log_evaluation=(False), validation_steps=None,
    class_colors=None, log_batch_frequency=None, log_best_prefix='best_',
    save_graph=(True), validation_indexes=None, validation_row_processor=None,
    prediction_row_processor=None, infer_missing_processors=(True)
)
```

#### Example:

```text
model.fit(X_train, y_train,  validation_data=(X_test, y_test),
    callbacks=[WandbCallback()])
```

WandbCallback will automatically log history data from any metrics collected by keras: loss and anything passed into keras\_model.compile\(\)

WandbCallback will set summary metrics for the run associated with the "best" training step, where "best" is defined by the `monitor` and `mode` attribues. This defaults to the epoch with the minimum val\_loss. WandbCallback will by default save the model associated with the best epoch..

WandbCallback can optionally log gradient and parameter histograms.

WandbCallback can optionally save training and validation data for wandb to visualize.

| Arguments |  |
| :--- | :--- |
|  monitor \(str\): name of metric to monitor. Defaults to val\_loss. mode \(str\): one of {"auto", "min", "max"}. "min" - save model when monitor is minimized "max" - save model when monitor is maximized "auto" - try to guess when to save the model \(default\). |  |
|  `save_model` |  True - save a model when monitor beats all previous epochs False - don't save models |
|  `save_graph` |  \(boolean\): if True save model graph to wandb \(default: True\). save\_weights\_only \(boolean\): if True, then only the model's weights will be saved \(`model.save_weights(filepath)`\), else the full model is saved \(`model.save(filepath)`\). |
|  `log_weights` |  \(boolean\) if True save histograms of the model's layer's weights. |
|  `log_gradients` |  \(boolean\) if True log histograms of the training gradients |
|  `training_data` |  \(tuple\) Same format \(X,y\) as passed to model.fit. This is needed for calculating gradients - this is mandatory if `log_gradients` is `True`. |
|  `validate_data` |  \(tuple\) Same format \(X,y\) as passed to model.fit. A set of data for wandb to visualize. If this is set, every epoch, wandb will make a small number of predictions and save the results for later visualization. generator \(generator\): a generator that returns validation data for wandb to visualize. This generator should return tuples \(X,y\). Either validate\_data or generator should be set for wandb to visualize specific data examples. validation\_steps \(int\): if `validation_data` is a generator, how many steps to run the generator for the full validation set. labels \(list\): If you are visualizing your data with wandb this list of labels will convert numeric output to understandable string if you are building a multiclass classifier. If you are making a binary classifier you can pass in a list of two labels \["label for false", "label for true"\]. If validate\_data and generator are both false, this won't do anything. predictions \(int\): the number of predictions to make for visualization each epoch, max is 100. input\_type \(string\): type of the model input to help visualization. can be one of: \("image", "images", "segmentation\_mask"\). output\_type \(string\): type of the model output to help visualziation. can be one of: \("image", "images", "segmentation\_mask"\). log\_evaluation \(boolean\): if True, save a Table containing validation data and the model's preditions at each epoch. See `validation_indexes`, `validation_row_processor`, and `output_row_processor` for additional details. class\_colors \(\[float, float, float\]\): if the input or output is a segmentation mask, an array containing an rgb tuple \(range 0-1\) for each class. log\_batch\_frequency \(integer\): if None, callback will log every epoch. If set to integer, callback will log training metrics every log\_batch\_frequency batches. log\_best\_prefix \(string\): if None, no extra summary metrics will be saved. If set to a string, the monitored metric and epoch will be prepended with this value and stored as summary metrics. validation\_indexes \(\[wandb.data\_types.\_TableLinkMixin\]\): an ordered list of index keys to associate with each validation example. If log\_evaluation is True and `validation_indexes` is provided, then a Table of validation data will not be created and instead each prediction will be associated with the row represented by the TableLinkMixin. The most common way to obtain such keys are is use Table.get\_index\(\) which will return a list of row keys. validation\_row\_processor \(Callable\): a function to apply to the validation data, commonly used to visualize the data. The function will receive an ndx \(int\) and a row \(dict\). If your model has a single input, then row\["input"\] will be the input data for the row. Else, it will be keyed based on the name of the input slot. If your fit function takes a single target, then row\["target"\] will be the target data for the row. Else, it will be keyed based on the name of the output slots. For example, if your input data is a single ndarray, but you wish to visualize the data as an Image, then you can provide \`lambda ndx, row: {"img": wandb.Image\(row\["input"\]\)}\` as the processor. Ignored if log\_evaluation is False or `validation_indexes` are present. output\_row\_processor \(Callable\): same as validation\_row\_processor, but applied to the model's output. \`row\["output"\]\` will contain the results of the model output. infer\_missing\_processors \(bool\): Determines if validation\_row\_processor and output\_row\_processor should be inferred if missing. Defaults to True. If `labels` are provided, we will attempt to infer classification-type processors where appropriate. |

## Methods

### `on_batch_begin` <a id="on_batch_begin"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L511-L512)

```text
on_batch_begin(
    batch, logs=None
)
```

A backwards compatibility alias for `on_train_batch_begin`.

### `on_batch_end` <a id="on_batch_end"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L515-L522)

```text
on_batch_end(
    batch, logs=None
)
```

A backwards compatibility alias for `on_train_batch_end`.

### `on_epoch_begin` <a id="on_epoch_begin"></a>

```text
on_epoch_begin(
    epoch, logs=None
)
```

Called at the start of an epoch.

Subclasses should override for any actions to run. This function should only be called during TRAIN mode.

| Arguments |  |
| :--- | :--- |
|  `epoch` |  Integer, index of epoch. |
|  `logs` |  Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_epoch_end` <a id="on_epoch_end"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L454-L508)

```text
on_epoch_end(
    epoch, logs={}
)
```

Called at the end of an epoch.

Subclasses should override for any actions to run. This function should only be called during TRAIN mode.

| Arguments |  |
| :--- | :--- |
|  `epoch` |  Integer, index of epoch. |
|  `logs` |  Dict, metric results for this training epoch, and for the validation epoch if validation is performed. Validation result keys are prefixed with `val_`. For training epoch, the values of the `Model`'s metrics are returned. Example : \`{'loss': 0.2, 'acc': 0.7}\`. |

### `on_predict_batch_begin` <a id="on_predict_batch_begin"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L613-L614)

```text
on_predict_batch_begin(
    batch, logs=None
)
```

Called at the beginning of a batch in `predict` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `tf.keras.Model` is set to `N`, this method will only be called every `N` batches.

| Arguments |  |
| :--- | :--- |
|  `batch` |  Integer, index of batch within the current epoch. |
|  `logs` |  Dict, contains the return value of `model.predict_step`, it typically returns a dict with a key 'outputs' containing the model's outputs. |

### `on_predict_batch_end` <a id="on_predict_batch_end"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L616-L617)

```text
on_predict_batch_end(
    batch, logs=None
)
```

Called at the end of a batch in `predict` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `tf.keras.Model` is set to `N`, this method will only be called every `N` batches.

| Arguments |  |
| :--- | :--- |
|  `batch` |  Integer, index of batch within the current epoch. |
|  `logs` |  Dict. Aggregated metric results up until this batch. |

### `on_predict_begin` <a id="on_predict_begin"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L607-L608)

```text
on_predict_begin(
    logs=None
)
```

Called at the beginning of prediction.

Subclasses should override for any actions to run.

| Arguments |  |
| :--- | :--- |
|  `logs` |  Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_predict_end` <a id="on_predict_end"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L610-L611)

```text
on_predict_end(
    logs=None
)
```

Called at the end of prediction.

Subclasses should override for any actions to run.

| Arguments |  |
| :--- | :--- |
|  `logs` |  Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_test_batch_begin` <a id="on_test_batch_begin"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L601-L602)

```text
on_test_batch_begin(
    batch, logs=None
)
```

Called at the beginning of a batch in `evaluate` methods.

Also called at the beginning of a validation batch in the `fit` methods, if validation data is provided.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `tf.keras.Model` is set to `N`, this method will only be called every `N` batches.

| Arguments |  |
| :--- | :--- |
|  `batch` |  Integer, index of batch within the current epoch. |
|  `logs` |  Dict, contains the return value of `model.test_step`. Typically, the values of the `Model`'s metrics are returned. Example: \`{'loss': 0.2, 'accuracy': 0.7}\`. |

### `on_test_batch_end` <a id="on_test_batch_end"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L604-L605)

```text
on_test_batch_end(
    batch, logs=None
)
```

Called at the end of a batch in `evaluate` methods.

Also called at the end of a validation batch in the `fit` methods, if validation data is provided.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `tf.keras.Model` is set to `N`, this method will only be called every `N` batches.

| Arguments |  |
| :--- | :--- |
|  `batch` |  Integer, index of batch within the current epoch. |
|  `logs` |  Dict. Aggregated metric results up until this batch. |

### `on_test_begin` <a id="on_test_begin"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L595-L596)

```text
on_test_begin(
    logs=None
)
```

Called at the beginning of evaluation or validation.

Subclasses should override for any actions to run.

| Arguments |  |
| :--- | :--- |
|  `logs` |  Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_test_end` <a id="on_test_end"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L598-L599)

```text
on_test_end(
    logs=None
)
```

Called at the end of evaluation or validation.

Subclasses should override for any actions to run.

| Arguments |  |
| :--- | :--- |
|  `logs` |  Dict. Currently the output of the last call to `on_test_batch_end()` is passed to this argument for this method but that may change in the future. |

### `on_train_batch_begin` <a id="on_train_batch_begin"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L524-L525)

```text
on_train_batch_begin(
    batch, logs=None
)
```

Called at the beginning of a training batch in `fit` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `tf.keras.Model` is set to `N`, this method will only be called every `N` batches.

| Arguments |  |
| :--- | :--- |
|  `batch` |  Integer, index of batch within the current epoch. |
|  `logs` |  Dict, contains the return value of `model.train_step`. Typically, the values of the `Model`'s metrics are returned. Example: \`{'loss': 0.2, 'accuracy': 0.7}\`. |

### `on_train_batch_end` <a id="on_train_batch_end"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L527-L534)

```text
on_train_batch_end(
    batch, logs=None
)
```

Called at the end of a training batch in `fit` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `tf.keras.Model` is set to `N`, this method will only be called every `N` batches.

| Arguments |  |
| :--- | :--- |
|  `batch` |  Integer, index of batch within the current epoch. |
|  `logs` |  Dict. Aggregated metric results up until this batch. |

### `on_train_begin` <a id="on_train_begin"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L548-L590)

```text
on_train_begin(
    logs=None
)
```

Called at the beginning of training.

Subclasses should override for any actions to run.

| Arguments |  |
| :--- | :--- |
|  `logs` |  Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_train_end` <a id="on_train_end"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L592-L593)

```text
on_train_end(
    logs=None
)
```

Called at the end of training.

Subclasses should override for any actions to run.

| Arguments |  |
| :--- | :--- |
|  `logs` |  Dict. Currently the output of the last call to `on_epoch_end()` is passed to this argument for this method but that may change in the future. |

### `set_model` <a id="set_model"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L443-L452)

```text
set_model(
    model
)
```

### `set_params` <a id="set_params"></a>

[View source](https://www.github.com/wandb/client/tree/v0.10.28/wandb/integration/keras/keras.py#L440-L441)

```text
set_params(
    params
)
```

