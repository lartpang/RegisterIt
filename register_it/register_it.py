# -*- coding: utf-8 -*-
# @Time    : 2021/5/22
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang

import importlib
import sys
from typing import Any, Dict, Iterable, Iterator, Tuple

from register_it.utils import formatter_for_dict


class Registry(Iterable[Tuple[str, Any]]):
    """
    The registry that provides name -> object mapping, to support classes and functions.

    To create a registry (e.g. a class registry and a function registry):
    ::

        DATASETS = Registry(name="dataset")
        EVALUATE = Registry(name="evaluate")

    To register an object:
    ::

        @DATASETS.register(name='mymodule')
        class MyModule(*args, **kwargs):
            ...

        @EVALUATE.register(name='myfunc')
        def my_func(*args, **kwargs):
            ...

    Or:
    ::

        DATASETS.register(name='mymodule', obj=MyModule)

        EVALUATE.register(name='myfunc', obj=my_func)

    To construct an object of the class or the function:
    ::

        DATASETS = Registry(name="dataset")
        # The callers of the DATASETS are from the module data, we need to manually import it.
        DATASETS.import_module_from_module_names(["data"])

        EVALUATE = Registry(name="evaluate")
        # The callers of the EVALUATE are from the module evaluate, we need to manually import it.
        EVALUATE.import_module_from_module_names(["evaluate"])
    """

    def __init__(self, name: str) -> None:
        """
        Args:
            name (str): the name of this registry
        """
        self._name: str = name
        self._obj_map: Dict[str, Any] = {}

    def _do_register(self, name: str, obj: Any) -> None:
        assert (
            name not in self._obj_map
        ), f"An object named '{name}' was already registered in '{self._name}' registry!"
        self._obj_map[name] = obj

    def register(self, name: str = None, *, obj: Any = None) -> Any:
        """
        Register the given object under the the name `obj.__name__`.
        Can be used as either a decorator or not.
        See docstring of this class and the examples in the folder `examples` for usage.
        """
        if name is not None:
            assert isinstance(name, str), f"name must be a str obj, but current name is {type(name)}"

        if obj is None:
            # used as a decorator
            def deco(func_or_class: Any) -> Any:
                key = func_or_class.__name__ if name is None else name
                self._do_register(key, func_or_class)
                return func_or_class

            return deco

        # used as a function call
        name = obj.__name__ if name is None else name
        self._do_register(name, obj)

    def get(self, name: str) -> Any:
        ret = self._obj_map.get(name)
        if ret is None:
            raise KeyError(f"No object named '{name}' found in '{self._name}' registry!")
        return ret

    def __getattr__(self, name: str):
        return self.get(name=name)

    def __getitem__(self, name: str):
        return self.get(name=name)

    def __contains__(self, name: str) -> bool:
        return name in self._obj_map

    def __repr__(self) -> str:
        table_headers = ["Names", "Objects"]
        table = formatter_for_dict(self._obj_map, headers=table_headers)
        return "Registry of {}:\n".format(self._name) + table

    __str__ = __repr__

    def __iter__(self) -> Iterator[Tuple[str, Any]]:
        return iter(self._obj_map.items())

    def keys(self):
        return self._obj_map.keys()

    def values(self):
        return self._obj_map.values()

    @staticmethod
    def import_module_from_module_names(module_names, verbose=True):
        for name in module_names:
            name_splits = name.split(".")[0]

            to_import = True
            for _existing_module in sys.modules.keys():
                _existing_module_splits = _existing_module.split(".")[0]
                if _existing_module_splits == name_splits:
                    if verbose:
                        print(f"Module:{name} has been contained in sys.modules ({_existing_module}).")
                    to_import = False
                    break
            if not to_import:
                continue

            module_spec = importlib.util.find_spec(name)
            if module_spec is None:
                raise ModuleNotFoundError(f"Module :{name} not found")

            if verbose:
                print(f"Module:{name} is being imported!")

            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)

            if verbose:
                print(f"Module:{name} has been imported!")
