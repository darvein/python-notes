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

## Notes from Tutorial
### An Informal Introduction to Python
Simplier math operations, variables definition and strings manipulation. Also a little bit of lists. Here an example :link: [01.lab01.py](01.lab01.py)
### More Control Flow Tools
Conditionals, Loops, Match/Case, Functions (positional arguments and keywords) and Lambdas.
### Data Structures
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

### Modules
### Input and Output
### Errors and Exceptions
### Classes
### Brief Tour of the Standard Library
### Brief Tour of the Standard Library — Part II
### Virtual Environments and Packages
### What Now?
### Interactive Input Editing and History Substitution
### Floating Point Arithmetic: Issues and Limitations
### Appendix

## Some notes
Creator of this language is Guido Van Rossum, his main intention (besides a hobby project), was to create a programming language for everybody, literally that was his motivation and vision. I think he made it!.

From wikipedia:
> In 1999, Van Rossum submitted a funding proposal to DARPA called "Computer Programming for Everybody", in which he further defined his goals for Python.

### Python 2 vs Python 3! :boxing_glove:
This was done mainly to get a better maintenability of the code, lots of redundancies removed, code improved. But also breaks compatability.

Visibible from user developer perspective (?):
- No parenthesis for prints
- Float numbers for integer division
- All is Unicode
- Improved iterators (`range()`, `dict.keys()`)
- Standard libraries reorganized
- Error handling refactoring
