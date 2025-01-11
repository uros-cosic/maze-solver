import time
import random
from cell import Cell
from point import Point


class Maze:
    def __init__(self, x, y, rows, cols, size_x, size_y, win, seed=None):
        self._cells = [[Cell(0, 0, win) for _ in range(rows)] for _ in range(cols)]
        self._x = x
        self._y = y
        self._rows = rows
        self._cols = cols
        self._size_x = size_x
        self._size_y = size_y
        self._win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls(0, 0)
        self._reset_visited()

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


    def _break_entrance_and_exit(self):
        start_cell = self._cells[0][0]
        end_cell = self._cells[self._cols - 1][self._rows - 1]

        start_cell.has_top_wall = False
        end_cell.has_bottom_wall = False

        start_cell.draw()
        end_cell.draw()

    def _get_adjacent_cells(self, i, j):
        res = []

        if i - 1 >= 0:
            top_cell = self._cells[i - 1][j]
            if not top_cell.visited:
                res.append([top_cell, "top"])
        if i + 1 < self._cols:
            bottom_cell = self._cells[i + 1][j]
            if not bottom_cell.visited:
                res.append([bottom_cell, "bot"])
        if j - 1 >= 0:
            left_cell = self._cells[i][j - 1]
            if not left_cell.visited:
                res.append([left_cell, "left"])
        if j + 1 < self._rows:
            right_cell = self._cells[i][j + 1]
            if not right_cell.visited:
                res.append([right_cell, "right"])

        return res

    def _break_walls(self, i, j):
        curr = self._cells[i][j]
        curr.visited = True

        while True:
            cells_to_visit = self._get_adjacent_cells(i, j)

            if not len(cells_to_visit):
                curr.draw()
                self._animate()
                return

            cell, pos = cells_to_visit[random.randrange(len(cells_to_visit))]
            new_i, new_j = i, j

            if pos == 'top':
                curr.has_top_wall = False
                cell.has_bottom_wall = False
                new_i, new_j = i - 1, j
            elif pos == 'bot':
                curr.has_bottom_wall = False
                cell.has_top_wall = False
                new_i, new_j = i + 1, j
            elif pos == 'left':
                curr.has_left_wall = False
                cell.has_right_wall = False
                new_i, new_j = i, j - 1
            else:
                curr.has_right_wall = False
                cell.has_left_wall = False
                new_i, new_j = i, j + 1

            self._break_walls(new_i, new_j)

    def _reset_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False


    def _solve(self, i, j):
        curr = self._cells[i][j]

        if curr == self._cells[self._cols - 1][self._rows - 1]:
            return True

        curr.visited = True

        neighbours = self._get_adjacent_cells(i, j)
        to_visit = []

        for cell, pos in neighbours:
            if pos == 'top' and not curr.has_top_wall:
                to_visit.append([cell, [i - 1, j]])
            if pos == 'bot' and not curr.has_bottom_wall:
                to_visit.append([cell, [i + 1, j]])
            if pos == 'left' and not curr.has_left_wall:
                to_visit.append([cell, [i, j - 1]])
            if pos == 'right' and not curr.has_right_wall:
                to_visit.append([cell, [i, j + 1]])

        for cell, coords in to_visit:
            curr.draw_move(cell)
            self._animate()
            res = self._solve(coords[0], coords[1])
            if res:
                return True
            else:
                curr.draw_move(cell, True) 
                self._animate()

        return False


    def solve(self):
        return self._solve(0, 0)
