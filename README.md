py-sneakers
======

Port to python of the [libnms](https://github.com/bartobri/libnms) C library

To recreate the famous data decryption effect shown in the 1992 film Sneakers.

![Demo](https://github.com/aenima-x/py-sneakers/raw/main/demo.gif)

Install
-----
```
git clone https://github.com/aenima-x/py-sneakers
cd py-sneakers
pip install .
```

Usage
-----

**As a command**
```
echo "Text" | py-sneakers

echo "Text" |python -m py_sneakers
```

**As a lib**
```python
from py_sneakers.py_sneakers import Sneakers

Sneakers("Some text").decrypt()
```


License
-------

This program is free software; you can redistribute it and/or modify it under the terms of the the
MIT License (MIT). See [LICENSE](LICENSE) for more details.