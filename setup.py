from setuptools import setup

from my_pip_package import __version__

setup(
    name='dpackage',
    version=__version__,

    url='https://github.com/ukfirst/dpackage',
    author='UK',
    author_email='larsen@bk.ru',

    py_modules=['my_pip_package'],
)