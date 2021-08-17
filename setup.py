import pathlib
from setuptools import setup
from re import search

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

with open(HERE / "py_sneakers" / "__init__.py", "rt", encoding="utf8") as f:
    VERSION = search(r"__version__ = \"(.*?)\"", f.read()).group(1)

setup(
    name='py-sneakers',
    version=VERSION,
    packages=['py_sneakers'],
    url='https://github.com/aenima-x/py-sneakers',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    author='Nicolas Rebagliati',
    author_email='nicolas.rebagliati@aenima-x.com.ar',
    description='Python library to emulate the Sneakers effect',
    long_description=README,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": ["py-sneakers=py_sneakers.__main__:main"],
    },
)
