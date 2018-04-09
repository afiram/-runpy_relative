import os
import runpy
import sys


def execute():
    if len(sys.argv) < 2:
        print(f"""usage:
            python {sys.argv[0]} path/to/script.py
        """)
    else:
        del sys.argv[0] # Make the requested module sys.argv[0]
        script = sys.argv[0]
        mod = '.'.join(script.replace(os.sep, '.').split('.')[:-1])
        runpy.run_module(mod, {}, "__main__", 1)


if __name__ == "__main__":
    execute()
