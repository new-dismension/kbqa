import os
from setuptools import setup

# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "kbqa",
    version = "0.0",
)
