from . import mod1
from ..other import mod2

"""
$ python runpy_relative.py path/to/script.py
script ok. spam:egg ham:egg

$ python -m runpy path.to.script
script ok. spam:egg ham:egg

$ python -m runpy path/to/script.py
python: Error while finding module specification for 'path/to/script.py' (ModuleNotFoundError: No module named 'path/to/script')

# normally, python3 `relative import` with `__main__` script filename execute is not work.
$ python path/to/script.py
Traceback (most recent call last):
  File "path/to/script.py", line 1, in <module>
    from . import mod1
ValueError: Attempted relative import in non-package
"""


if __name__ == "__main__":
    spam = mod1.spam()
    ham = mod2.ham()
    print("script ok. spam:{} ham:{}".format(spam, ham))

