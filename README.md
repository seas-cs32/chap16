This directory contains everything needed for
**Chapter 16 (Catch Them Early)** in
[*Computational Thinking and Problem Solving (CTPS)*](https://profsmith89.github.io/ctps/ctps.html)
by Michael D. Smith.

`bookshelf1-anno.py`: A copy of `bookshelf1.py` from Chapter 3
with the addition of type hints, which demonstrates that difficulty
of using type hints and data abstraction. The problem is that
not all sequence types in Python support concatenation. Enable
mypy to see the type errors.

`dbzero.py`: A simple script containing an obvious
divide-by-zero error.

`dbzero1.py`: A slightly more complicated script containing a
divide-by-zero error.

`dbzero2.py`: A script that sometimes raises a divide-by-zero
runtime error.

`dyntype.py`: A simple example of dynamic typing and how easy
it is to not know statically the type of the object in a name.

`emdash.py`: A script that allows a user to indicate which
parenthetical phrase should be offset with em dashes rather
than commas. It contains a silly coding bug.

`emdash-anno.py`: The `emdash.py` script with type hints that
allow mypy to find the type error.

`emdash-fixed.py`: The `emdash.py` script with the type error
corrected. Don't peek!

`equal.py`: A short script showing that two objects with the
same value expressed as bits are not considered equal by Python.

`equal.c`: A C-language-version of `equal.py` showing that C
doesn't consider type information at runtime.

`equal2.c`: Another version of `equal.c` with the variable
declaration separated from the variable initialization.

`fun.c`: A simple C program used to demonstrate compiling
to an executable.

`txts/debugging.txt`: Input used in `emdash.py` example.
