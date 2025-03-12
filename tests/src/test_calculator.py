from app.src.calculator import Calculator

cal = Calculator()

def test_add():
    assert cal.add(1, 1) == 2
    assert cal.add(1, 3) == 4

def test_substract():
    assert cal.subtract(100, 1) == 99
    assert cal.subtract(10, 1) == 9


