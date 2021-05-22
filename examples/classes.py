# -*- coding: utf-8 -*-
# @Time    : 2021/5/22
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang

from register_it.register_it import Registry


class MyModule:
    def __call__(self, *args, **kwargs):
        print(*args, **kwargs)
        print(f"I am the class {self.__class__.__name__}")


MYCLASSES = Registry(name="myclasses")
MYCLASSES.register(name="mymodule", obj=MyModule)

if __name__ == "__main__":
    print(MYCLASSES)

    # three way to get the obj using the corresponding name
    My_Module = MYCLASSES.get("mymodule")
    my_module = My_Module()
    my_module("Hello!")

    My_Module = MYCLASSES["mymodule"]
    my_module = My_Module()
    my_module("Hello!")

    My_Module = MYCLASSES.mymodule
    my_module = My_Module()
    my_module("Hello!")
