assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
	values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
	the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
	grid(string) - A grid in string form.
    Returns:
	A grid in dictionary form
	    Keys: The boxes, e.g., 'A1'
	    Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    return dict(zip(boxes, [g.replace('.', '123456789') for g in list(grid)]))

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rowNames:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                for c in colNames))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
	values: Sudoku in dictionary form.
    Returns:
	Resulting Sudoku in dictionary form after eliminating values.
    """
    for box in values:
        value = values[box]
        if len(value) == 1:
            for peer in peers[box]:
                values[peer] = values[peer].replace(value, "")
    return values

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        usedIntegers = dict((i, []) for i in '123456789')
        for box in unit:
            integers = list(values[box])
            for integer in integers:
                usedIntegers[integer].append(box)
        for integer in usedIntegers:
            if len(usedIntegers[integer]) == 1:
                box = usedIntegers[integer][0]
                values[box] = integer
    return values

def reduce_puzzle(values):
    """Receive an unsolved sudoku puzzle.

    Attempt to solve the puzzle using constraint propogation

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form with reduced box values.
    """
    stalled = False
    while not stalled:
	# Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

	# Your code here: Use the Eliminate Strategy
        values = eliminate(values)

	# Your code here: Use the Only Choice Strategy
        values = only_choice(values)

	# Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])

	# If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after

	# Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    """Receive an unsolved sudoku puzzle.

    Continually apply a constraint propogation strategy to generate a tree of possibilities,
    moving over them depth first until a solution is found if one exists.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form with reduced box values.
    """
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values == False:
        return False

    if all(len(values[s]) == 1 for s in boxes): 
        return values

    # Choose one of the unfilled squares with the fewest possibilities
    box = ""
    val = ""
    MAX = 10
    for b in values:
        if len(values[b]) < MAX and len(values[b]) > 1:
            box = b
            val = values[box]
            MAX = len(values[box])

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for integer in val:
        v = values.copy()
        v[box] = integer
        r = search(v)
        if r:
            return r

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
	grid(string): a string representing a sudoku grid.
	    Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
	The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    solved = search(values)
    return solved

"""
Global values that describe the layout of the sudoku board and 
relationships between individual points on the board (aka 'boxes')
and their peers.
"""
rowNames = "ABCDEFGHI"
colNames = "123456789"
boxes    = cross(rowNames, colNames)
rows     = [cross(i, colNames) for i in rowNames]
cols     = [cross(rowNames, i) for i in colNames]
squares  = [cross(row, column) for column in ["123", "456", "789"] for row in ["ABC", "DEF", "GHI"]]
unitlist = rows + cols + squares
units    = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers    = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

if __name__ == '__main__':
    #diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    #display(solve(diag_sudoku_grid))

    # test solvability of a basic puzzle
    sudoku_puzzle = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    print("483921657967345821251876493548132976729564138136798245372689514814253769695417382")

    solved = solve(sudoku_puzzle)
    for s in solved:
        print(solved[s], end='')
    print("")

    #display(solve(sudoku_puzzle))

"""
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
"""
