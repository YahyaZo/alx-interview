# UTF-8 Validation

This project is about validating whether a given dataset represents a valid UTF-8 encoding.

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS

## Usage

To use the `validUTF8` function, import it from the `0-validate_utf8` module and pass a list of integers representing the bytes:

```python
from 0-validate_utf8 import validUTF8

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False
