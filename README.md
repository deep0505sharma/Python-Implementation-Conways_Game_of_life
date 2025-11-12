# Description
The Game of Life is a cellular automaton created by John H. Conway in 1970. The game is a zero-player game in which an initially configured 2D grid of cells evolves according to the Game of Life [ruleset](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

Built using Python 3.14.0, this implementation of Conway's Game of Life allows the user to easily run the Game of Life using a 2D grid of chosen number of rows and columns in either a MacOS or Windows terminal/console.

![Demo Animation](example.gif)

This project is licensed under the terms of the MIT license.

# Ruleset
Using the following ruleset the 2D grid of cells will evolve from generation to generation until it reaches a static state of either all dead cells or a mix of still, oscillating, or moving (spaceship) cells.

1. **Underpopulation** - If a live cell is surrounded by fewer than two surrounding neighbours, it dies and does not make it to the next generation.
2. **Equilibrium** - If a live cell is surrounded by two or three living neighbors, the cell stays alive and makes it to the next generation.
3. **Overpopulation** - If a live cell is surrounded by more than three living neighbors, the cell dies and does not make it to the next generation.
4. **Reproduction** - If a dead cell is surrounded by three living neighbor,s the cell stays alive and makes it to the next generation.

# Dependancies
![GitHub tag](https://img.shields.io/github/tag/pandao/editor.md.svg)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![License](https://img.shields.io/github/license/pandao/editor.md.svg)
![PyPI](https://img.shields.io/pypi/v/packagename.svg)
![release](https://img.shields.io/github/v/release/OWNER/REPO)
![Python Version](https://img.shields.io/badge/python-3.14.0-blue.svg)
![TOML](https://img.shields.io/badge/config-TOML-blue?logo=toml&logoColor=white)

***Python***: High-level, interpreted programming language known for its simplicity, readability, and versatility across web development, data science, automation, and AI.

***TOML***: Minimal configuration file format that’s convenient to read and parse and primarily used for configuration, separating code from settings for flexibility.

***Visual Studio Code***: Primary code editor used for development.


# Project Structure

* Implement the Game of Life algorithm, including the life grid and the seeds or patterns
* Provide a way to visualize the life grid and its evolution
* Allow the user to set a pattern and run the game a given number of generations
Following these ideas, here's the directory structure for this Python Implementation of the Game of Life project:
```
Python-Implementation-Conways_Game_of_life/
├── __pycache__/                     # Compiled Python bytecode cache
│   ├── __init__.cpython-314.pyc
│   ├── __main__.cpython-314.pyc
│   ├── cli.cpython-314.pyc
│   ├── grid.cpython-314.pyc
│   ├── patterns.cpython-314.pyc
│   └── views.cpython-314.pyc
│
├── rplife/                          # Core Python package for the project
│   ├── __init__.py                  # Marks rplife as a Python package
│   ├── __main__.py                  # Entry point for running the program
│   ├── cli.py                       # Command-line interface logic
│   ├── grid.py                      # Grid implementation (core game logic)
│   ├── patterns.py                  # Predefined Conway’s Game of Life patterns
│   ├── patterns.toml                # Configuration file for patterns
│   └── views.py                     # Handles rendering or visualization
│
├── .DS_Store                        # macOS system file (can be ignored)
├── LICENSE                          # License information for the project
├── README.md                        # Project documentation
└── example.gif                      # Example animation or demo for README

```

# How to Run
This project is built using Python 3.14.0 and requires that the user has at least Python 3 installed in order to run the program. Python 3+ can be installed [here](https://www.python.org/downloads/).

```bash
cd "Path to directory where you want to clone the repo"
git clone https://github.com/deep0505sharma/Python-Implementation-Conways_Game_of_life.git
python3 -m rplife -a
```

