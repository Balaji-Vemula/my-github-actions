# Function to test
def add(a, b):
    return a + b

# Test case
def test_add():
    assert add(3, 4) == 7
    assert add(0, 5) == 5
    assert add(-1, 1) == 0
    assert add(10, 20) == 30
