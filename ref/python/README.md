# python

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/7bbc4a4eac8eeb2bf37a62ce519e0de61c67eadf/wandb/__init__.py)








## Classes

[`class Artifact`](./artifact.md): Dataset versioning, model versioning, pipeline tracking with flexible and lightweight building block.

[`class Run`](./run.md): The run object corresponds to a single execution of your script, typically this is an ML experiment.

## Functions

[`agent(...)`](./agent.md): Generic agent entrypoint, used for CLI or jupyter.

[`config(...)`](./config.md): Config object

[`init(...)`](./init.md): Start a new tracked run with <code>wandb.init()</code>.

[`join(...)`](./join.md): Marks a run as finished, and finishes uploading all data.

[`log(...)`](./log.md): Log a dict to the global run's history.

[`save(...)`](./save.md): Ensure all files matching *glob_str* are synced to wandb with the policy specified.

[`setup(...)`](./setup.md)

[`summary(...)`](./summary.md): Summary tracks single values for each run. By default, summary is set to the last value of History.

[`sweep(...)`](./sweep.md)



<!-- Tabular view -->
<table>
<tr><th>Other Members</th></tr>

<tr>
<td>
__version__<a id="__version__"></a>
</td>
<td>
`'0.10.26.dev1'`
</td>
</tr>
</table>

