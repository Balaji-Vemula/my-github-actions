# test_sample.py
n = 5
def test_comparison():
    assert n == 6

def test_odd():
    if n%2 == 0:
        assert False, "Got even number"
    else:
        assert True
