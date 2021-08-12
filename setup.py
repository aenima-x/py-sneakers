from setuptools import setup

setup(
    name='py-sneakers',
    version='1.0',
    packages=[''],
    url='https://github.com/aenima-x/py-sneakers',
    license='MIT',
    author='Nicolas Rebagliati',
    author_email='nicolas.rebagliati@aenima-x.com.ar',
    description='Python library to emulate the Sneakers effect',
    entry_points={
        "console_scripts": ["py-sneakers=py_sneakers:main"],
    },
)
