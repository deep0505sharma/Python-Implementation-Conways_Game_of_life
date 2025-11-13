import curses
from time import sleep
import sys

from rplife.grid import LifeGrid

__all__ = ["CursesView", "TextView"]


class CursesView:
    def __init__(self, pattern, gen=10, frame_rate=7, bbox=(0, 0, 40, 20)):
        self.pattern = pattern
        self.gen = gen
        self.frame_rate = frame_rate
        self.bbox = bbox

    def show(self):
        curses.wrapper(self._draw)

    def _draw(self, screen):
        current_grid = LifeGrid(self.pattern)
        curses.curs_set(0)
        screen.clear()

        try:
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
        except curses.error:
            raise ValueError(
                f"Error: terminal too small for pattern '{self.pattern.name}'"
            )

        for _ in range(self.gen):
            current_grid.evolve()
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
            screen.refresh()
            sleep(1 / self.frame_rate)


# A simple text-based view that works in notebooks and non-tty environments.
try:
    # IPython's clear_output gives a nicer animation in notebooks
    from IPython.display import clear_output as _clear_output
    _HAS_IPY = True
except Exception:
    _HAS_IPY = False


class TextView:
    """Text-based view for environments without a controlling terminal.

    It will use IPython.display.clear_output when available (Jupyter),
    otherwise it falls back to ANSI screen-clearing for a terminal.
    """

    def __init__(self, pattern, gen=10, frame_rate=7, bbox=(0, 0, 40, 20)):
        self.pattern = pattern
        self.gen = gen
        self.frame_rate = frame_rate
        self.bbox = bbox

    def show(self):
        current_grid = LifeGrid(self.pattern)

        for _ in range(self.gen):
            if _HAS_IPY:
                _clear_output(wait=True)
                print(current_grid.as_string(self.bbox))
            else:
                # ANSI clear screen and move cursor to home
                sys.stdout.write("\x1b[2J\x1b[H")
                sys.stdout.write(current_grid.as_string(self.bbox) + "\n")
                sys.stdout.flush()

            sleep(1 / self.frame_rate)
            current_grid.evolve()
