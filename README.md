#Conways Game of life
The Game of Life is a cellular automaton created by John H. Conway in 1970. The game is a zero-player game in which an initially configured 2D grid of cells evolves according to the Game of Life [ruleset](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

Built using Python 3.14.0, this implementation of Conway's Game of Life allows the user to easily run the Game of Life using a 2D grid of choosen number of rows and columns in either a MacOS or Windows terminal/console.

This project is licensed under the terms of the MIT license.

#Ruleset
Using the following ruleset the 2D grid of cells will evolve from generation to generation until it reaches a static state of either all dead cells or a mix of still, oscillating, or moving (spaceship) cells.

1. Underpopulation - If a live cell has is surrounded by less than two surrounding neighbours it dies and does not make it to the next generation.
2. quilibrium - If a live cell is surrounded by two or three living neighbors the cell stays alive and makes it to the next generation.
3. Overpopulation - If a live cell is surrounded by more than three living neighbors the cell dies and does not make it to the next generation.
4. Reproduction - If a dead cell is surrounded by three living neighbors the cell stays alive and makes it to the next generation.
