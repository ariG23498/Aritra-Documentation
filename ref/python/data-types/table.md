# Table



[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L147-L785)



This is a table designed to display sets of records.

```python
Table(
    columns=None, data=None, rows=None, dataframe=None, dtype=None, optional=(True),
    allow_mixed_types=(False)
)
```





| Arguments |  |
| :--- | :--- |
|  `columns` |  ([str]) Names of the columns in the table. Defaults to ["Input", "Output", "Expected"]. |
|  `data` |  (array) 2D Array of values that will be displayed as strings. |
|  `dataframe` |  (pandas.DataFrame) DataFrame object used to create the table. When set, the other arguments are ignored. optional (Union[bool,List[bool]]): If None values are allowed. Singular bool applies to all columns. A list of bool values applies to each respective column. Default to True. allow_mixed_types (bool): Determines if columns are allowed to have mixed types (disables type validation). Defaults to False |



## Methods

<h3 id="add_column"><code>add_column</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L683-L722)

```python
add_column(
    name, data, optional=(False)
)
```

Add a column of data to the table.

Arguments
    name: (str) - the unique name of the column
    data: (list | np.array) - a column of homogenous data
    optional: (bool) - if null-like values are permitted

<h3 id="add_computed_columns"><code>add_computed_columns</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L765-L785)

```python
add_computed_columns(
    fn
)
```

Adds one or more computed columns based on existing data


| Args |  |
| :--- | :--- |
|  fn (function): A function which accepts one or two paramters: ndx (int) and row (dict) which is expected to return a dict representing new columns for that row, keyed by the new column names. - `ndx` is an integer representing the index of the row. Only included if `include_ndx` is set to true - `row` is a dictionary keyed by existing columns |



<h3 id="add_data"><code>add_data</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L367-L397)

```python
add_data(
    *data
)
```

Add a row of data to the table. Argument length should match column length


<h3 id="add_row"><code>add_row</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L363-L365)

```python
add_row(
    *row
)
```




<h3 id="cast"><code>cast</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L262-L316)

```python
cast(
    col_name, dtype, optional=(False)
)
```

Casts a column to a specific type


| Arguments |  |
| :--- | :--- |
|  `col_name` |  (str) - name of the column to cast |
|  `dtype` |  (class, wandb.wandb_sdk.interface._dtypes.Type, any) - the target dtype. Can be one of normal python class, internal WB type, or an example object (eg. an instance of wandb.Image or wandb.Classes) |
|  `optional` |  (bool) - if the column should allow Nones |



<h3 id="get_column"><code>get_column</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L724-L747)

```python
get_column(
    name, convert_to=None
)
```

Retrieves a column of data from the table

Arguments
    name: (str) - the name of the column
    convert_to: (str, optional)
        - "numpy": will convert the underlying data to numpy object

<h3 id="get_index"><code>get_index</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L749-L756)

```python
get_index()
```

Returns an array of row indexes which can be used in other tables to create links


<h3 id="index_ref"><code>index_ref</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L758-L763)

```python
index_ref(
    index
)
```

Get a reference to a particular row index in the table


<h3 id="iterrows"><code>iterrows</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L562-L575)

```python
iterrows()
```

Iterate over rows as (ndx, row)
Yields
------
index : int
    The index of the row. Using this value in other WandB tables
    will automatically build a relationship between the tables
row : List[any]
    The data of the row

<h3 id="set_fk"><code>set_fk</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L582-L586)

```python
set_fk(
    col_name, table, table_col
)
```




<h3 id="set_pk"><code>set_pk</code></h3>

[View source](https://www.github.com/wandb/client/tree/v0.10.31.dev1/wandb/data_types.py#L577-L580)

```python
set_pk(
    col_name
)
```








| Class Variables |  |
| :--- | :--- |
|  MAX_ARTIFACT_ROWS<a id="MAX_ARTIFACT_ROWS"></a> |  `200000` |
|  MAX_ROWS<a id="MAX_ROWS"></a> |  `10000` |

