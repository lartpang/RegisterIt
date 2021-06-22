#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup


def get_version():
    init_py_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "register_it", "__init__.py")
    init_py = open(init_py_path, "r").readlines()
    version_line = [l.strip() for l in init_py if l.startswith("__version__")][0]
    version = version_line.split("=")[-1].strip().strip("'\"")
    return version


readme_name = "readme.md" if os.path.exists("readme.md") else "README.md"
with open(readme_name, "r") as fh:
    long_description = fh.read()

setup(
    name="register_it",
    packages=find_packages(),
    version=get_version(),
    license="MIT",
    description="Register it: A more flexible register for the DeepLearning project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="lartpang",
    author_email="lartpang@gmail.com",
    url="https://github.com/lartpang/RegisterIt",
    keywords=[
        "tools",
        "deep learning",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
