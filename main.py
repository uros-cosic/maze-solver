from cell import Cell
from point import Point
from window import Window

def main():
    win = Window(500, 500)

    cell_one = Cell(Point(10, 10), Point(100, 100), win)
    cell_one.draw()

    cell_two = Cell(Point(100, 10), Point(200, 100), win)
    cell_two.draw()

    cell_one.draw_move(cell_two)

    win.wait_for_close()

if __name__ == '__main__':
    main()
