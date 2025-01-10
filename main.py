from cell import Cell
from point import Point
from window import Window

def main():
    win = Window(500, 500)

    cell = Cell(Point(10, 10), Point(100, 100), win)
    cell.draw()

    win.wait_for_close()

if __name__ == '__main__':
    main()
