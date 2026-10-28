from app import add, subtract

def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5