import pytest
from algorithms.recursion.lc509_fibonacci_number.solution import fib

class TestLC509Fibonacci:
    # @pytest.mark.skip
    def test_valid_input_returns_correct_output(self):
        # Arrange
        n = 5
        # Act
        result = fib(n)
        # Assert
        assert result == 5

    # @pytest.mark.skip
    def test_valid_input_returns_correct_output2(self):
        # Arrange
        n = 8
        # Act
        result = fib(n)
        # Assert
        assert result == 21
    
    # @pytest.mark.skip
    def test_valid_input_returns_correct_output3(self):
        # Arrange
        n = 12
        # Act
        result = fib(n)
        # Assert
        assert result == 144


    # @pytest.mark.skip
    def test_exceptional_function(self):
        with pytest.raises(ValueError):
            fib(-5)


    # @pytest.mark.skip
    def test_exceptional_function2(self):
        with pytest.raises(ValueError):
            fib("5")


if __name__ == "__main__":
    pytest.main()