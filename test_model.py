from model import Model


def test_sum():
    model = Model()
    model.number_a = 5
    model.number_b = 23
    assert model.get_sum() == 28


def test_diff():
    model = Model()
    model.number_a = 5
    model.number_b = 23
    assert model.get_diff() == -18
