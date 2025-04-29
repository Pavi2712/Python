import pytest
import time
def some_slow_function():
    # Simulate a long process
    time.sleep(2)
    return "completed"
@pytest.mark.slow
def test_heavy_data_processing():
    expected_result = "completed"
    result = some_slow_function()
    assert result == expected_result