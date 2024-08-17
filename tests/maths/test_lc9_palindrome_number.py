import pytest
from maths.lc9_palindrome_number.solution import is_palindrome


class TestLC9PalindromeNumber:
    # @pytest.mark.skip
    def test_return_true_if_palindrome(self):
        # Arrange
        x = 2884882
        # Act
        result = is_palindrome(x)
        # Assert
        assert result == True


    # @pytest.mark.skip
    def test_return_false_if_negative_number(self):
        # Arrange
        x = -902101209
        # Act
        result = is_palindrome(x)
        # Assert
        assert result == False


    # @pytest.mark.skip
    def test_return_false_if_not_palindrome(self):
        # Arrange
        x = 82
        x2 = 9847299947
        # Act
        result = is_palindrome(x)
        result2 = is_palindrome(x2)
        # Assert
        assert result == False
        assert result2 == False


if __name__ == "__main__":
    pytest.main()