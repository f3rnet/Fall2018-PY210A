#!/usr/bin/env python

"""
Chris' solution to the grid printing Exercise.

Note that we only did the basics of loops, and you can
do all this without any loops at all, so that's what I did.

Note also that there is more than one way to skin a cat --
   or code a function
"""

# NOTE -- Going thru lessons as a well needed refresh using Solution Code!
# by Ron Tallman


def print_grid_ez():
    """
    Did anyone come up with the most trivial possible solution?
    """
    print("\nPrinting out the box using comments")
    print("""
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
""")

def print_grid(size):
    """
    print a 2x2 grid with a total size of size

    :param size: total size of grid -- it will be rounded if not one more than
        a multiple of 2
    """
    number = 2
    box_size = int((size - 1) // 2)  # size of one grid box: integer division

    print("\t\t\tOur first non-EZ Box")
    print("The Box Size will be: \t\t", box_size)
    # top row
    top = ('+ ' + '- ' * box_size) * number + '+' + '\n'
    middle = ('| ' + ' ' * 2 * box_size) * number + '|' + '\n'

    row = top + middle * box_size
    print("The Top will look like: \t", top.strip())
    print("The Middle will look like: \t", middle)

    grid = row * number + top

    print(grid)

def print_grid2(number, size):
    """
    print a number x number grid with each box of size width and height

    :param number: number of grid boxes (row and column)

    :param size: size of each grid box
    """
    print("This box will be\t{} x {} with {} columns\n".format(size,size,number))
    # top row
    top = ('+ ' + '- ' * size) * number + '+' + '\n'
    middle = ('| ' + ' ' * 2 * size) * number + '|' + '\n'

    row = top + middle * size

    grid = row * number + top

    print(grid)

def print_grid3(size):
    """
    same as print_grid, but calling print_grid2 to do the work
    """
    number = 2
    box_size = (size - 1) // 2  # size of one grid box: note integer divsion!
    print_grid2(number, box_size)

################
# Function calls
################

print_grid_ez()

print_grid(7)
print_grid2(3,3)

print_grid3(9)
print_grid3(13)
