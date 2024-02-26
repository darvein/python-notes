# Python Tutorial
Resource: https://docs.python.org/3/tutorial/index.html

## Overview
At first glance this teaches about:
- Basics: variables, operators and data types. Math, numbers, strings and lists
- Flow structures: if, for, while loops. break/continue
- Functions
- Data structures: lists, dicts, sets, tuples
- Modules, Packages and Classes
- Most popular libs: `math`, `random`, `datetime`, `statistics`, 
- Exceptions: `try`, `except`, `finally`
- Others: List comprehension, function decorators 

## An Informal Introduction to Python
Simplier math operations, variables definition and strings manipulation. Also a little bit of lists. Here an example :link: [01.lab01.py](01.lab01.py)

## More Control Flow Tools
Conditionals, Loops, Match/Case, Functions (positional arguments and keywords) and Lambdas.

## Data Structures
Basics:
- Lists: its common functions: count, sort, sort, reverse, copy, extend, insert, remove, pop, clear, index
- Stacks: A list can be treated as stac by using its functions like `list.append()` or `list.pop()`
    - Remember a stack is FIFO
- Queues: By usage of `deque` from `collections`
    - Remember a queue is LIFO
- List comprenhensions: Done by `[]` with a for loop (the so called list comprehensions) and `lambda`s
- Tuples: Immutable items on a list
- Sets: Unique items on a list
- Dictionaries: key:value pair of items

## Modules
A single file becomes a module, for example foobar.py becomes a module called `foobar`.

The default modules loaded in python are:
- `builtins`
- `os` and `sys` but partially, not all its functions/features

:exclamation: Important to keep in mind that if a single py file is executed directly it becomes `__name__ = __main__` but if it is being called from another py file then `__name__` becomes the name of the py file (see lab04 py scripts on this repo).

Modules are loaded from `sys.builtin_module_names` or `sys.path` (PYTHONPATH, current directory or site-packages dir).

The `dir()` function lists all available properties and functions of a given module, e.g.: `dir(sys)` or `dir(builtins)`

**Packages** :package: are sub-directories of a module for example this package `sounds.effects.echo` has this path directory: `./sounds/effects/echo.py` we can import it like `from sounds.effects import *` or relatively load the module `from ..sounds.effects import *`.

## Input and Output
What python can offer are basically ways to output data say strings or numbers to output resources like the terminal itself also read-write to files.

Formatting:
- `f'Results of the {year} {event}'`
- `'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)`
- Usage of `repr()` and `str()`
- `f'The value of pi is approximately {math.pi:.3f}.'`
- `print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))`
- `'12'.zfill(5)` for numbers

Files:
- `with open('workfile', encoding="utf-8") as f:...` by default mode is `r`
- `import json`, `json.load(f)`, `json.dump(object_structured, f)`

## Errors and Exceptions
- Common exceptions: OSError, ValueError, Exception, KeyboardInterrupt
- `finally` block is processed regardless if try/execpt blocks were processed
- `else` block is processed only when the `try` block was successful
## Classes
- By default all variables are defaulted to `local` scope.
    - A `del foobar` removes the binding from the namespace referenced by the local scope
    - `global`: is a variable defined inside a function that can be modified externally, globally
    - `nonlocal`: is a variable that belongs in the nearest eclosing scope and its not global, but can be modified on any inner function
- A class has to be initiated with function `__init__(self, foo, bar):`
- Classes support Inheritance and Multiple Inheritance
## Brief Tour of the Standard Library
Popular standard py libraries: os shutil glob sys argparse re math random statistics urllib date
## Brief Tour of the Standard Library — Part II
Popular standard libs: reprlib, pprint, textwrap, locale, Template, struct, threading, logging, array
## Virtual Environments and Packages

# Some notes
Creator of this language is Guido Van Rossum, his main intention (besides a hobby project), was to create a programming language for everybody, literally that was his motivation and vision. I think he made it!.

From wikipedia:
> In 1999, Van Rossum submitted a funding proposal to DARPA called "Computer Programming for Everybody", in which he further defined his goals for Python.

## Python 2 vs Python 3! :boxing_glove:
This was done mainly to get a better maintenability of the code, lots of redundancies removed, code improved. But also breaks compatability.

Visibible from user developer perspective (?):
- No parenthesis for prints
- Float numbers for integer division
- All is Unicode
- Improved iterators (`range()`, `dict.keys()`)
- Standard libraries reorganized
- Error handling refactoring
