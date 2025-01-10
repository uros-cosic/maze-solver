import time
from cell import Cell
from point import Point


class Maze:
    def __init__(self, x, y, rows, cols, size_x, size_y, win):
        self._cells = [[Cell(0, 0, win)] * rows] * cols
        self._x = x
        self._y = y
        self._size_x = size_x
        self._size_y = size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                start_point = Point(self._x + j * self._size_x, self._y + i * self._size_y)
                end_point = Point(self._x + self._size_x + j * self._size_x, self._y + self._size_y + i * self._size_y)
                self._cells[i][j] = Cell(start_point, end_point, self._win)
                self._cells[i][j].draw()
                self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.033)

