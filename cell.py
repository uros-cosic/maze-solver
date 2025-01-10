from line import Line
from point import Point

class Cell:
    def __init__(self, start, end, win):
        self.start = start
        self.end = end
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win

    def _draw_line(self, line):
        self._win.draw_line(line, "black")

    def draw(self):
        if self.has_left_wall:
            self._draw_line(Line(self.start, Point(self.start.x, self.end.y)))
        if self.has_right_wall:
            self._draw_line(Line(Point(self.end.x, self.start.y), self.end))
        if self.has_top_wall:
            self._draw_line(Line(self.start, Point(self.end.x, self.start.y)))
        if self.has_bottom_wall:
            self._draw_line(Line(Point(self.start.x, self.end.y), self.end))
