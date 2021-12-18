# Puzzle Pegs (Python)

This is the Python version of the [Puzzle Pegs](https://github.com/Techman/puzzle-pegs) program. Like the C++ version, it has had a few iterations, from orginally using top-level functions to now using a class to represent the entire puzzle.

To view details on the program itself, please visit the repository linked above.

## Running

You can view help information by typing `python main.py --help`.

## Lessons Learned

I decided to write a Python version of Puzzle Pegs to test the performance of an interpreted languaged compared to the original Java version. Performance of the Python version depends on the computer it is running on, but it is generally noticeably slower when given a set of starting and ending positions that are not solvable, but still very fast when given positions that are.
