# learning_curve



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.27/wandb/sklearn/__init__.py#L296-L353)




Trains model on datasets of varying lengths and generates a plot of

<pre><code>learning_curve(
    model, X, y, cv=None, shuffle=(False), random_state=None, train_sizes=None,
    n_jobs=1, scoring=None
)</code></pre>



scores vs training sizes for both training and test sets.

Called by plot_learning_curve to visualize learning curve. Please use the function
plot_learning_curve() if you wish to visualize your learning curves.