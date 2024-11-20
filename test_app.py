from app import add, subtract

def test_add():
    assert add(3, 5) == 8
    assert add(-2, 1) == -1
    

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
