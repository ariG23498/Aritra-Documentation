# lightgbm

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/integration/lightgbm/__init__.py)




W&B callback for lightgbm


Really simple callback to get logging for each tree

#### Example usage:



param_list = [("eta", 0.08), ("max_depth", 6), ("subsample", 0.8), ("colsample_bytree", 0.8), ("alpha", 8), ("num_class", 10)]
config.update(dict(param_list))
lgb = lgb.train(param_list, d_train, callbacks=[wandb_callback()])

## Functions

[`wandb_callback(...)`](./wandb_callback.md)

