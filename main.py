from maze import Maze
from window import Window

def main():
    win = Window(500, 500)

    maze = Maze(10, 10, 10, 10, 30, 30, win)
    res = maze.solve()
    print("Path exists" if res else "Path doesn't exist")

    win.wait_for_close()

if __name__ == '__main__':
    main()
