import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import *

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_subtract():
    assert subtract(5, 6) == -1

def test_subtract2():
    assert subtract(5, 6) != 10

def test_multiply():
    assert multiply(5, 6) == 30

def test_multiply2():
    assert multiply(5, 6) != 10

def test_divide():
    assert divide(1, 2) == 0.5

def test_divide2():
    assert divide(1, 2) != 10

def test_log():
    assert log(1) == 0

def test_log2():
    assert log(2, 2) == 1

def test_log3():
    assert log(5, 6) != 10

def test_square():
    assert square(5) == 25

def test_square2():
    assert square(5) != 10

def test_sin():
    assert sin(0) == 0

def test_sin2():
    assert sin(0) != 1

def test_cos():
    assert cos(0) == 1

def test_cos2():
    assert cos(0) != 0

def test_square_root():
    assert square_root(4) == 2

def test_square_root2():
    assert square_root(4) != 10

def test_square_root3():
    assert square_root(4**2) == 4

def test_percentage():
    assert percentage(5, 50) == 10

def test_percentage2():
    assert percentage(5, 50) != 11

def test_percentage3():
    assert percentage(5) == 5