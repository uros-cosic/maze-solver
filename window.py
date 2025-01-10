from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width=250, height=250):
        self.__width = width
        self.__height = height

        self.__root = Tk()
        self.__root.title = "Maze solver"

        self.__canvas = Canvas()
        self.__canvas.pack()

        self.running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()

    def close(self):
        self.running = False

