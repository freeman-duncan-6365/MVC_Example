
"""An MVC controller for a simple example program."""

from model import Model
from view import View


class Controller:
    """Handles view-to-model interoperation."""

    def __init__(self, view, model):
        """Initialize variables and set callbacks."""
        self.view = view
        self.model = model
        self.view.entry_a_listener = self.entry_a_modified
        self.view.entry_b_listener = self.entry_b_modified
        self.show_calculations()

    def entry_a_modified(self, content):
        """Text entry A was called from view."""
        if content.isdigit():
            self.model.number_a = int(content)
            self.show_calculations()

    def entry_b_modified(self, content):
        """Text entry B was called from view."""
        if content.isdigit():
            self.model.number_b = int(content)
            self.show_calculations()

    def show_calculations(self):
        """Calculate sums and diffs on the model and update the view."""
        self.view.set_sum(self.model.get_sum())
        self.view.set_diff(self.model.get_diff())
