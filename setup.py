from setuptools import setup, find_packages

from charts.__init__ import __version__

setup(
    name='charts',
    version=__version__,

    url='https://github.com/ukfirst/dpackage',
    author='UK',
    author_email='larsen@bk.ru',

    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ]
)