import pytest
from algorithms.sliding_window.lc_3_longest_substring_without_repeating_chars.solution import length_of_longest_substring


class TestLC3LongestSubstringWithoutRepeatingChars:
    # @pytest.mark.skip
    def test_no_duplicates_returns_length_of_list(self):
        # Arrange
        string = "dvcf"
        # Act
        result = length_of_longest_substring(string)
        # Assert
        assert result == 4


    # @pytest.mark.skip
    def test_empty_string_returns_zero(self):
        # Arrange
        string = ""
        # Act
        result = length_of_longest_substring(string)
        # Assert
        assert result == 0


    # @pytest.mark.skip
    def test_string_length_one_return_one(self):
        # Arrange
        string = "d"
        # Act
        result = length_of_longest_substring(string)
        # Assert
        assert result == 1


    # @pytest.mark.skip
    def test_one_space_returns_one(self):
        # Arrange
        string = " "
        # Act
        result = length_of_longest_substring(string)
        # Assert
        assert result == 1


    # @pytest.mark.skip
    def test_finds_correct_length_with_duplicate(self):
        # Arrange
        string = "abcabcbb"
        # Act
        result = length_of_longest_substring(string)
        # Assert
        assert result == 3


if __name__ == "__main__":
    pytest.main()