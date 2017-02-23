# Artificial Intelligence Nanodegree ## Introductory Project: Diagonal Sudoku
Solver

# Question 1 (Naked Twins) 

Q: How do we use constraint propagation to solve the naked twins problem?  

A: 

Solving puzzles can be accomplished using a brute force approach.  That is,
simply try all possibilities available.  In the case of a sudoku puzzle this
produces a very large set of possibilities that would take a considerable amount
of time to solve.  In order to overcome this, constraint propagation is used.
Constraint propogation is simply a process by which the number of possibilities
that need to be explored can be reduced.  In the case of sudoku the very rules
upon which the game is designed offer guidance as to how to write code that
exploits these constraints.

For instance, each row in a sudoku puzzle must have all numbers from 1 to 9
represented once in any order.  Using this knowledge any row in a sudoku puzzle
with a single digit automatically allows one to remove all representations of
that number from all other points in the row, excluding the original cell with
the single digit.  This approach can also be applied to columns and grids, the
3x3 clusters in the puzzle.  In fact all approaches such as this one will be
applied to rows, columns, and 3x3 clusters so that solving the puzzle can become
more efficient and effective.

Once several constraint formulae are conceived they can be used together
iteratively to search the solution space, a tree, in a depth first manner.  If a
particular attempt is found to be unusable, the next branch in the tree is
explored until, in the worst case, all possible branches have been evaluated.

Naked Twins is an example of using the knowledge of sudoku's rules towards
constraint propogation.  Whenever a unit (row, column, or 3x3 grid) contains two
cells that have the same pairs of numbers, any other cells in the unit can no
longer contains that pair.  This is simply because a sudoku puzzle requires
uniqueness in the numbers 1 to 9 so each of the two cells must have a number.
Naked Twins is applicable to all sudoku puzzles.

# Question 2 (Diagonal Sudoku) 

Q: How do we use constraint propagation to solve the diagonal sudoku problem?  

A: 

As with the Naked Twins problem, a diagonal sudoku scenario limits the scope of
possible values present in the diagonal boxes.  Specifically each diagonal must
have the numbers 1 to 9 represented once in any order.   While this doesn't
produce a new formula for evaluating the branches in the search tree of
solutions, this does create a new relationship, or unit, between the different
cells in the sudoku puzzle, which further constrains the possible solutions.
This isn't applicable to a typical sudoku puzzle.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a
pre-packaged Python distribution that contains all of the necessary libraries
and software for this project.  Please try using the environment we provided in
the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization.
If you've followed our instructions for setting up our conda environment, you
should be all set.

If not, please see how to download pygame
[here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running
  `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your
  solution.
* `visualize.py` - Do not modify this. This is code for visualizing your
  solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using
the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
