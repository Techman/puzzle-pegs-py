#!/usr/bin/env python
"""Performance profiling for Puzzle Pegs"""

import cProfile
import pstats
from puzzle_pegs import PuzzlePegs


def solvable_profile():
    """Performance profile for an instance of the puzzle known to be solvable"""
    with cProfile.Profile() as prof:
        PuzzlePegs(13, 13).solve()

    stats = pstats.Stats(prof)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()


def unsolvable_profile():
    """Performance profile for an instance of the puzzle known to be unsolvable"""
    with cProfile.Profile() as prof:
        PuzzlePegs(13, 14).solve()

    stats = pstats.Stats(prof)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()


def main():
    """Main function"""
    # Run the solvable profile
    print("*** Running solvable profile...")
    solvable_profile()
    print("*** Profile done")

    # Run the unsolvable profile
    print("*** Running unsolvable profile...")
    unsolvable_profile()
    print("*** Profile done")


if __name__ == "__main__":
    main()
