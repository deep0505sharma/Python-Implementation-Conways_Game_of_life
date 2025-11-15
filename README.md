# 📝 Description
The Game of Life is a cellular automaton created by John H. Conway in 1970. The game is a zero-player game in which an initially configured 2D grid of cells evolves according to the Game of Life [ruleset](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

Built using Python 3.14.0, this implementation of Conway's Game of Life allows the user to easily run the Game of Life using a 2D grid of chosen number of rows and columns in either a MacOS or Windows terminal/console.

![Demo Animation](example.gif)

This project is licensed under the terms of the MIT license.

# 📜 Ruleset
Using the following ruleset the 2D grid of cells will evolve from generation to generation until it reaches a static state of either all dead cells or a mix of still, oscillating, or moving (spaceship) cells.

1. **Underpopulation** - If a live cell is surrounded by fewer than two surrounding neighbours, it dies and does not make it to the next generation.
2. **Equilibrium** - If a live cell is surrounded by two or three living neighbors, the cell stays alive and makes it to the next generation.
3. **Overpopulation** - If a live cell is surrounded by more than three living neighbors, the cell dies and does not make it to the next generation.
4. **Reproduction** - If a dead cell is surrounded by three living neighbor,s the cell stays alive and makes it to the next generation.

# 🛠️ Dependancies
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


# 📑 Project Structure

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
├── example.gif                      # Demo animation for README
└── pyproject.toml                   # Project metadata & build configuration

```

# 📦 How to Run
This project is built using Python 3.14.0 and requires that the user has at least Python 3 installed in order to run the program. Python 3+ can be installed [here](https://www.python.org/downloads/).

```bash
cd "Path to directory where you want to clone the repo"
git clone https://github.com/deep0505sharma/Python-Implementation-Conways_Game_of_life.git
cd Python-Implementation-Conways_Game_of_life
python3 -m rplife -a
```
The project has a user-friendly command-line interface that allows you to run it with different options. You can run the game/project with a single pattern, with all the available patterns, and more. Before doing this, you need to setup the virtual python environment in your system and have pyproject.toml file present in the project folder to run the project using single commands.

## 🖥️ Virtual Environment Set-up

```bash
python3 -m venv myvenv
source myvenv/bin/activate
python3 -m pip install -e .
```

**Running the project as a stand-alone CLI application.**

----------
```bash
Python-Implementation-Conways_Game_of_life --all #will show all available patterns in a sequence
Python-Implementation-Conways_Game_of_life -p "Beacon" -g 10 #will show next 10 gens of Beacon pattern
Python-Implementation-Conways_Game_of_life --version #will show the program's version number and name
```
----------

## 🚀 On Jupyter Notebook

-------
```bash
from rplife import grid, patterns
blinker = patterns.Pattern("Hearts", {(3, 1), (4, 2), (2, 2),(3,2),(3,3)})
grid = grid.LifeGrid(blinker)
print(grid.as_string((0, 0, 5, 5)))
```
-------
```bash
from rplife.views import CursesView, TextView
from rplife.patterns import get_pattern
TextView(get_pattern("Glider Gun"), gen=100).show()
```
-------
![Output](https://github.com/user-attachments/assets/fcb58ac3-4ad4-4132-8571-d7a15e37dffa)

**To implement and evolve any other random pattern of your choice**

-------
```bash
from rplife import grid, patterns
blinker = patterns.Pattern("Hearts", {(3, 1), (4, 2), (2, 2),(3,2),(3,3)})
grid = grid.LifeGrid(blinker)
print(grid.as_string((0, 0, 5, 5)))
```
-------
Output:
<img width="88" height="128" alt="Output" src="https://github.com/user-attachments/assets/59279427-7786-4056-9fab-5fedfbfbac0f" />

-------
```bash
grid.evolve()
print(grid.as_string((0, 0, 5, 5)))
```
-------
Output:
<img width="88" height="128" alt="Image" src="https://github.com/user-attachments/assets/8f146d33-c7a9-453d-9ec3-2974c30c550a" />

# 📖 Conclusion
1. Implemented Conway’s Game of Life using Python and object-oriented programming. 
2. To make the game usable, built a user-friendly command-line interface using argparse. In the process, I’ve learned how to structure and organize a CLI app and set up the application for distribution and installation.
3. Learned about TOML config files and writing them.

# 💡 Next Steps
Go a step further by implementing a few additional features. 
Here are some ideas for new features:

1. **Implement other views**: Having other views apart from the one based on curses would be a great addition to the project. For example, writing a Tkinter view where we can display the life grid in a GUI window.
2. **Add exciting new life patterns**: Adding new life patterns to patterns.toml will allow exploring other behaviors of the game.
3. **Change the rules**: So far, the project has been implemented with the traditional rules, where dead cells with three living neighbors are born, and living cells with two or three living neighbors survive. But there are several variations that use different rules to evolve to a new generation. Changing the rules allows experiencing other life-like universes.

---------
  ```javascript
  if youLiked : 
      ⭐ Star_Repository
  # Thank You! 🙏
  ```
-----------

