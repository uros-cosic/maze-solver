import sys
from maze import Maze
from window import Window

def main():
    win = Window(1000, 1000)

    args = sys.argv[1:]

    rows = 30
    cols = 30
    seed = None

    for arg in args:
        if arg.startswith("rows="):
            rows = int(arg.split("=")[1])
        if arg.startswith("cols="):
            cols = int(arg.split("=")[1])
        if arg.startswith("seed="):
            seed = int(arg.split("=")[1])

    maze = Maze(10, 10, rows, cols, 30, 30, win, seed)
    res = maze.solve()
    print("Path exists" if res else "Path doesn't exist")

    win.wait_for_close()

if __name__ == '__main__':
    main()
