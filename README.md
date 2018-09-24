# jewel-challenge-solver
This solver was written for my Fall 2018 Artificial Intelligence class at the University of Northern Iowa. It solves a jewel puzzle using iterative deepening depth-first search. And example of iterative deepening depth-first search here: <img src="https://github.com/awalker88/jewel-challenge-solver/blob/master/iterativeDFS.gif" width="400" height="350" />

## Getting Started

The description of the problem can be found in the problemDescription.pdf file in this repository. An interactive version of the puzzle can be found at https://scratch.mit.edu/projects/26515800/ . The solver will print out the steps necessary to take you from the initial board state to the solved board state.


## Running the Solver
This project requires Python 3 and the library NumPy.  

The main function is ```search(board, numRows, numCols)```. There are 3 types of jewels: Diamonds, Rubies, and Emeralds. Diamonds will cycle to Rubies, Rubies to Emeralds, and Emeralds to Diamonds.

Parameters of ```search()```:  
**1. board** - board state that you would like to solve, entered as one string. (ex. 'EEEDDDRRR')

**2. numRows** - the number of columns your board has

**3. numCols** - the number of columns your board has

To solve a board, first convert your board to a single string with the first letters of each jewel. Then run the ```search()``` function with the board state and it's dimensions as its parameters. Note that the length of your string needs to be equal to ```numCols``` times ```numRows```.
Examples: 
* ```search('EEEDDDRRR', 3, 3)```
* ```search('DDREEREE', 4, 2)```

## Built With
**NumPy**   
* for matrices and outputing results in grid format  

**PyCharm**  
* IDE and debugging  

## Authors
* **Solver:** Andrew Walker  
* **Assignment:** Dr. Ben Schafer  
* **Original Problem:** Dr. Douglas Shaw
