import pytest
from datastructures.stacks_and_queues.lc20_valid_parens.solution import is_valid


class TestLC3LongestSubstringWithoutRepeatingChars:
    # @pytest.mark.skip
    def test_valid_parens_returns_true(self):
        # Arrange
        string = "()[]{}"
        string_1 = "()"
        string_2 = "{([[]])}"
        # Act
        result = is_valid(string)
        result_1 = is_valid(string_1)
        result_2 = is_valid(string_2)
        # Assert
        assert all([result, result_1, result_2])


    # @pytest.mark.skip
    def test_empty_string_returns_false(self):
        # Arrange
        string = ""
        # Act
        result = is_valid(string)
        # Assert
        assert result == False


    # @pytest.mark.skip
    def test_string_length_one_return_false(self):
        # Arrange
        string = "]"
        # Act
        result = is_valid(string)
        # Assert
        assert result == False


    # @pytest.mark.skip
    def test_one_space_returns_False(self):
        # Arrange
        string = " "
        # Act
        result = is_valid(string)
        # Assert
        assert result == False


    # @pytest.mark.skip
    def test_not_valid_parens_returns_False(self):
        # Arrange
        strings = ["([)]", "(}", "{([(]])}"]
        # Act/Assert
        for string in strings:
            assert is_valid(string) == False
        

if __name__ == "__main__":
    pytest.main()