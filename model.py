"""
An MVC model representing two numbers.

The numbers in the model and be modifed externally, and the diff
and sum between the two are available as functions.
"""


class Model:
    """Manages two numbers, a and b."""

    def __init__(self):
        """Set initial values to zero."""
        self.number_a = 0
        self.number_b = 0

    def get_sum(self):
        """Calculate the sum of a and b."""
        return self.number_a + self.number_b

    def get_diff(self):
        """Calculate the difference between a and b."""
        return self.number_a - self.number_b

    def __str__(self):
        """Convert the models' values to a string."""
        return "%i %i" % (self.number_a, self.number_b)
