# Advent of Code
Advent of Code Puzzle Solutions https://adventofcode.com/

A collection of solutions to the Advent of Code puzzles I've created.

**If you haven't done a puzzle, browsing the code may give away the solution.**

# Setup

I tried to standardize my puzzle code so it's repeatable.

The `puzzle.input.txt` contains the actual input.
The `puzzle.test.txt` contains the test input.
The `puzzle.py` contains the code to execute. This one is templetized so I can copy and paste it and just modify the code and run it.

# Execution

There's several flags that can be used to run the real or test input or puzzle 1 or 2.

`-t`    - This will run the test input. Omitting this flag uses the real input.  
`-p1`   - This runs the first puzzle.  
`-p2`   - This runs the second puzzle.  

`python puzzle.py -t -p1`   - This will run the test input for the first puzzle  
`python puzzle.py -p1 -p2`  - This will run both puzzles using the real input.