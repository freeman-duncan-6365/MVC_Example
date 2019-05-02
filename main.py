"""A simple GUI program that displays sums and differences from user input."""


from tkinter import *
from model import Model
from view import View
from controller import Controller


def main():
    """Create the UI and begin the main loop."""
    root_window = Tk()
    root_window.title = "Sum example"
    root_window.tk.call('tk', 'scaling', 1.2)

    model = Model()
    view = View(root_window)
    controller = Controller(view, model)
    root_window.mainloop()


main()
