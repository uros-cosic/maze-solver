from window import *
from line import *
from point import *

def main():
    win = Window(500, 500)

    start = Point(0, 0)
    end = Point(50, 50)

    line = Line(start, end)
    win.draw_line(line, "black")

    win.wait_for_close()

if __name__ == '__main__':
    main()
