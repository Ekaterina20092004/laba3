from main import add


def test_add_1():
    result = add(3, 4)
    assert result == 7


def test_add_2():
    assert -1 == add(-4, 3)


def test_add_3():
    assert 0 == add(-4, 4)
