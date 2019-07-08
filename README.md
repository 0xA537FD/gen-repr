# gen-repr [![Build Status](https://travis-ci.org/Peter-Morawski/gen-repr.svg?branch=master)](https://travis-ci.org/Peter-Morawski/gen-repr)

Lightweight python library without any dependencies to automatically generate
the ``__repr__`` method for any class.

## Getting started

Install this package throught pip
```sh
$ pip install gen-repr
```

After that you can import it in your program like this

```python
from genrepr import gen_repr
```

## Example

```python
from genrepr import gen_repr

@gen_repr()
class Person(object):
    def __init__(self):
        self.first_name = u""
        self.age = 0
        self._hair = u"any color you like"

peter = Person()
peter.first_name = u"Peter"
peter.age = -1

repr(peter) # result: "<Person (first_name='Peter', age=-1)>:
```
