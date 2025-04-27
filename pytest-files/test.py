# pytest-files/test.py

n = 5

def test_comparison():
    print("Running test_comparison")  # Log to see if this test is executed
    assert n == 6

def test_odd():
    print("Running test_odd")  # Log to see if this test is executed
    if n % 2 == 0:
        assert False, "Got even number"
    else:
        assert True
