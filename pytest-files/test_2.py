# Function to test
def is_even(num):
    return num % 2 == 0

# Test case
def test_is_even():
    assert is_even(2) == True
    assert is_even(4) == True
    assert is_even(0) == True
    assert is_even(-6) == True
