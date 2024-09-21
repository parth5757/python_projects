def func(x):
    return x + 1

def test_func():
    # Test case 1: Positive integer
    assert func(3) == 4, "Test case 1 failed"
    
    # Test case 2: Zero
    assert func(0) == 1, "Test case 2 failed"
    
    # Test case 3: Negative integer
    assert func(-1) == 0, "Test case 3 failed"
    
    # Test case 4: Large positive integer
    assert func(1000) == 1001, "Test case 4 failed"
    
    # Test case 5: Large negative integer
    assert func(-1000) == -999, "Test case 5 failed"