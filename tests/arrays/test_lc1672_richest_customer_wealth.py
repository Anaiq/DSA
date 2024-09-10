import pytest
from datastructures.arrays.lc1672_richest_customer_wealth.solution import maximum_wealth


class TestLC1672RichestCustomerWealth:
    # @pytest.mark.skip
    def test_no_accounts_returns_zero(self):
        # Arrange
        accounts = [[]]

        # Act
        result = maximum_wealth(accounts)
        # Assert
        assert result == 0


    # @pytest.mark.skip
    def test_correct_account_is_returned_1(self):
        # Arrange
        accounts = [[1,2,3],[3,2,1]]

        # Act
        result = maximum_wealth(accounts)
        # Assert
        assert result == 6


    # @pytest.mark.skip
    def test_correct_account_is_returned_2(self):
        # Arrange
        accounts = [[1,5],[7,3],[3,5]]

        # Act
        result = maximum_wealth(accounts)
        # Assert
        assert result == 10

    # @pytest.mark.skip
    def test_correct_account_is_returned_3(self):
        # Arrange
        accounts = [[2,8,7],[7,1,3],[1,9,5]]

        # Act
        result = maximum_wealth(accounts)
        # Assert
        assert result == 17


if __name__ == "__main__":
    pytest.main()