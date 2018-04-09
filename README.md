# runpy_relative

python3 module runner for relative import.
run script with fix relative import path.

how to use
------------------------------

```
$ python3 runpy_relative.py path/to/script.py
ok
```

technical note
--------------------------------------
standard module `runpy` is not work with filename args.

```
$ python3 -m runpy path.to.script
ok

$ python -m runpy path/to/script.py
/usr/bin/python: Import by filename is not supported.
```

