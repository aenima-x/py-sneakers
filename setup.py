from setuptools import setup
setup(
    name="py-sneakers",
    version="1.0",
    url="https://github.com/aenima-x/py-sneakers",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license="MIT",
    author="Aenima-x",
    python_requires=">3.7.0",
    author_email="nicolas.rebagliati@aenima-x.com.ar",
    description="Python library to emulate the Sneakers effect",
    include_package_data=True,
    entry_points={
        "console_scripts": ["py-sneakers=py_sneakers:main"],
    },
)
