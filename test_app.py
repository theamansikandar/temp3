from app import add, subtract, multiply, divide

def test_add():
    assert add(4, 2) == 6

def test_subtract():
    assert subtract(4, 2) == 2

def test_multiply():
    assert multiply(4, 2) == 8

def test_divide():
    assert divide(4, 2) == 2