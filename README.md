# RegisterIt

Register it: A more flexible register for the DeepLearning project.

The registry that provides name -> object mapping, to support classes and functions.

## Install

```shell
pip install register_it
```

## Usage

To create a registry (e.g. a class registry and a function registry):

```python
DATASETS = Registry(name="dataset")
EVALUATE = Registry(name="evaluate")
```

To register an object:

```python
@DATASETS.register(name='mymodule')
class MyModule(*args, **kwargs):
    ...

@EVALUATE.register(name='myfunc')
def my_func(*args, **kwargs):
    ...
```

Or:

```python
DATASETS.register(name='mymodule', obj=MyModule)

EVALUATE.register(name='myfunc', obj=my_func)
```

To construct an object of the class or the function:

```python
DATASETS = Registry(name="dataset")
# The callers of the DATASETS are from the module data, we need to manually import it.
DATASETS.import_module_from_module_names(["data"])

EVALUATE = Registry(name="evaluate")
# The callers of the EVALUATE are from the module evaluate, we need to manually import it.
EVALUATE.import_module_from_module_names(["evaluate"])
```

## Thanks

- [fvcore](https://github.com/facebookresearch/fvcore)
