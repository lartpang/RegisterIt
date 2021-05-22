# -*- coding: utf-8 -*-
# @Time    : 2021/5/22
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang

from register_it.register_it import Registry


def my_func(*args, **kwargs):
    print(*args, **kwargs)
    print(f"I am in the function {my_func.__name__}")


MYFUNCS = Registry(name="myfuncs")
MYFUNCS.register(name="myfunc", obj=my_func)

if __name__ == "__main__":
    print(MYFUNCS)

    # three way to get the obj using the corresponding name
    my_func = MYFUNCS.get("myfunc")
    my_func("Hello!")

    my_func = MYFUNCS["myfunc"]
    my_func("Hello!")

    my_func = MYFUNCS.myfunc
    my_func("Hello!")
