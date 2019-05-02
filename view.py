"""
A simple MVC view class.

Represents user input in the form of text entry A and B,
and output in the form of sum and diff text boxes.
"""
from tkinter import *


class View:
    """Represents user interface and layout for the app."""

    def __init__(self, root_window):
        """Initialize UI elements and set callbacks."""
        self.textvariable_a = StringVar()
        self.textvariable_a.trace("w", self.entry_a_modified_callback)
        self.entry_a = Entry(root_window, textvariable=self.textvariable_a)

        self.textvariable_b = StringVar()
        self.textvariable_b.trace("w", self.entry_b_modified_callback)
        self.entry_b = Entry(root_window, textvariable=self.textvariable_b)

        self.textvariable_sum = StringVar()
        self.entry_sum = Entry(root_window, state=DISABLED,
                               textvariable=self.textvariable_sum)

        self.textvariable_diff = StringVar()
        self.entry_diff = Entry(root_window, state=DISABLED,
                                textvariable=self.textvariable_diff)

        self.entry_a_listener = lambda *args: None
        self.entry_b_listener = lambda *args: None

        self.layout()

    def layout(self):
        """Set widget positioning and responsive layout."""
        self.entry_a.grid(row=0, column=0, sticky="nw")
        self.entry_b.grid(row=1, column=0, pady=5, sticky="nw")
        self.entry_sum.grid(row=0, column=1, padx=5, sticky="w")
        self.entry_diff.grid(row=1, column=1, padx=5, sticky="w")

    def set_sum(self, number):
        """Set the 'sum' box to a number."""
        self.textvariable_sum.set(number)

    def set_diff(self, number):
        """Set the 'diff' box to a number."""
        self.textvariable_diff.set(number)

    def entry_a_modified_callback(self, *args):
        """Fire the callback for listener attached to entry A."""
        self.entry_a_listener(self.textvariable_a.get())

    def entry_b_modified_callback(self, *args):
        """Fire the callback for listener attached to entry B."""
        self.entry_b_listener(self.textvariable_b.get())
