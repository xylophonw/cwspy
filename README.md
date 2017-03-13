# CWSpy
A simple API wrapper for [ConWorkShop](http://conworkshop.info/), written in Python.
## Dependencies
- [requests](http://docs.python-requests.org/en/master/)
  - install with `$ pip install requests`

## Installation
i should work out how to register this on the package index

when this is working it should just be
```pip install cwspy
```

## Usage
```python
import cwspy

foo = cwspy.api.API()

foo.get_user("name") # get user information
foo.get_lang("name") # get language information
```
~~when i actually get this working~~
## Contributing
i have no idea how github works but go for it
## Credits
Literally just a translation of [unleashy](https://github.com/unleashy)'s [Ruby wrapper](https://github.com/unleashy/cwsrb).
## License
Available under the terms of the [MIT license](http://opensource.org/licenses/MIT).
