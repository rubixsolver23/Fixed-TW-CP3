from equations import (
    add,
    sub,
    mult,
    div
)

def test_add():
    assert add(2,10) == 12
    assert add(3,5) == 8
    assert add(4,6) == 10

def test_sub():
    assert sub(10, 2) == 8
    assert sub(5,3) == 2
    assert sub(6,4) == 2

def test_mult():
    assert mult(2,10) == 20
    assert mult(3,5) == 15
    assert mult(4,6) == 24

def test_div():
    assert div(10,2) == 5
    assert div(15,5) == 3
    assert div(6,4) == 1.5