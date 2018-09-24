import numpy as np
import pandas as pd
from time import sleep

NUMROWS = 0
NUMCOLS = 0
PATH = []


def search(board, numRows, numCols):
    """ Main function to solve jewel puzzle
    INPUTS:
        board - string composed of any combination of the letters 'e', 'r', or 'd' of length equal to numRows x numCols
        numRows - number of rows you want your puzzle to have
        numCols - number of columns you want your puzzle to have
    OUTPUTS:
        list of instructions on how to change your board into one composed of all 'e's, 'r's, or 'd's
        """
    global NUMROWS
    global NUMCOLS
    global PATH
    NUMROWS= numRows
    NUMCOLS = numCols
    board = np.reshape(list(board.lower()), (NUMROWS, NUMCOLS))
    solution = iterative_deepening_search(board)
    PATH = PATH[::-1]
    print("In the following solution, a jewel's number is the number it would be given if it were on a numberpad. \
    For a 3x3 grid, for example, each jewel's number is as follows:")
    print(pd.DataFrame(np.arange(9).reshape((3, 3))).to_string(index=False, header=False))
    print("===============")
    print("\nGiven:")
    for item in PATH:
        print(pd.DataFrame(item[1]).to_string(index=False, header=False))
        print("\nSwitch jewel " + str(item[0]) + " to get:")
    print(pd.DataFrame(solution).to_string(index=False, header=False))
    sleep(1.5)  # for comedic timing
    print("\n\nTa Da!")



def cycle_jewel(jewelType):
    """ Returns the cycled jewel type (d to r, r to e, and e to d)
    INPUTS:
        jewelType - either 'd', 'e', or 'r'
    OUTPUTS:
        string that corresponds whatever the input string should cycle to"""
    if jewelType == 'd':
        return 'r'
    elif jewelType == 'r':
        return 'e'
    else:
        return 'd'


def check_goal(board):
    """ Returns True if board is all of one jewel, False otherwise """
    allEmeralds = np.empty((NUMROWS, NUMCOLS), dtype=str)
    allDiamonds = np.empty((NUMROWS, NUMCOLS), dtype=str)
    allRubies = np.empty((NUMROWS, NUMCOLS), dtype=str)

    allEmeralds[:] = 'e'
    allDiamonds[:] = 'd'
    allRubies[:] = 'r'

    if np.array_equal(board, allEmeralds):
        return True
    if np.array_equal(board, allDiamonds):
        return True
    if np.array_equal(board, allRubies):
        return True
    return False


def generate_children(board):
    """ Returns list of numpy arrays, each of which is a child of the given board """
    children = []
    for i in range(0, NUMROWS):
        for j in range(0, NUMCOLS):
            newBoard = np.copy(board)
            # flip middle jewel
            newBoard[i][j] = cycle_jewel(board[i][j])
            # try to flip north jewel
            if i - 1 >= 0:
                newBoard[i - 1][j] = cycle_jewel(board[i - 1][j])
            # try to flip east jewel
            if j + 1 <= NUMCOLS - 1:
                newBoard[i][j + 1] = cycle_jewel(board[i][j + 1])
            # try to flip west jewel
            if j - 1 >= 0:
                newBoard[i][j - 1] = cycle_jewel(board[i][j - 1])
            # try to flip south jewel
            if i + 1 <= NUMROWS - 1:
                newBoard[i + 1][j] = cycle_jewel(board[i + 1][j])
            children.append(newBoard)
    return children


# Iterative Depth Limiting Search
def iterative_deepening_search(root):
    """ First part of iterative_deepening_search"""
    path = [root]
    depth = 0
    cutoff = 18  # since every board should be solvable in 18 moves
    while depth < cutoff:
        print("Searching Depth %d..." % (depth))
        if depth > 7:
            print("This could take a while, sorry.\n")
        solution = depth_limited_search(root, depth)
        # return what we found if we found the solution
        if solution is not None:
            return solution
        depth += 1


def depth_limited_search(node, depth):
    """ Second part of iterative_deepening_search"""
    # check if root node is solution
    if depth == 0:
        if check_goal(node):
            return node
        else:
            return None
    elif depth > 0:
        children = generate_children(node)
        for child in range(len(children) - 1):
            # add child to PATH dictionary so we know where it came from
            solution = depth_limited_search(children[child], depth - 1)
            if solution is not None:
                global PATH
                PATH.append([child, node])
                return solution
        return None


search('dedeeeded', 3,3)
