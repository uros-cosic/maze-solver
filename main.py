from maze import Maze
from window import Window

def main():
    win = Window(500, 500)

    Maze(10, 10, 10, 10, 30, 30, win)

    win.wait_for_close()

if __name__ == '__main__':
    main()
