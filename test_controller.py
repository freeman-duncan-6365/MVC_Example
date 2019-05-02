from model import Model
from controller import Controller

class ViewMock:
    def __init__(self):
        pass

    def set_diff(*args):
        pass

    def set_sum(*args):
        pass

def test_both_invalid():
    model = Model()
    view = ViewMock()
    controller = Controller(view, model)
    controller.entry_a_modified("invalid input")
    controller.entry_b_modified("invalid input")
    assert model.get_sum() == 0

def test_one_invalid():
    model = Model()
    view = ViewMock()
    controller = Controller(view, model)
    controller.entry_a_modified("invalid input")
    controller.entry_b_modified("2")
    assert model.get_sum() == 2
