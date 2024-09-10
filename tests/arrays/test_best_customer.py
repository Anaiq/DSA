import pytest
from datastructures.arrays.best_customer.solution  import find_highest_food_weight


class TestBestCustomer:
    # @pytest.mark.skip
    def test_empty_food_brands_and_empty_owners_returns_none(self):
        # Arrange
        food_brand_weights = []
        owner_purchases = []

        # Act
        result = find_highest_food_weight(food_brand_weights, owner_purchases)
        # Assert
        assert result == None


    # @pytest.mark.skip
    def test_empty_food_brands_returns_none(self):
        # Arrange
        food_brand_weights = []
        owner_purchases = [("Barry", "FoodA", 1), ("Keisha", "FoodB", 3), ("Barry", "FoodA", 2)]

        # Act
        result = find_highest_food_weight(food_brand_weights, owner_purchases)
        # Assert
        assert result == None

    # @pytest.mark.skip
    def test_empty_owners_returns_none(self):
        # Arrange
        food_brand_weights = [("FoodA", 3), ("FoodB", 9)]
        owner_purchases = []

        # Act
        result = find_highest_food_weight(food_brand_weights, owner_purchases)
        # Assert
        assert result == None

    # @pytest.mark.skip
    def test_find_highest_food_weight_returns_highest1(self):
        # Arrange
        food_brand_weights = [("FoodA", 3), ("FoodB", 9)]
        owner_purchases = [("Barry", "FoodA", 1), ("Keisha", "FoodB", 3), ("Barry", "FoodA", 2)]

        # Act
        result = find_highest_food_weight(food_brand_weights, owner_purchases)
        # Assert
        assert result == ("Keisha", 59)

    # @pytest.mark.skip
    def test_find_highest_food_weight_returns_highest2(self):
        # Arrange
        food_brand_weights = [("FoodA", 10), ("FoodB", 20), ("FoodC", 15)]
        owner_purchases = [("Ankit", "FoodA", 3), ("Bob", "FoodB", 1), ("Ankit", "FoodC", 2)]

        # Act
        result = find_highest_food_weight(food_brand_weights, owner_purchases)
        # Assert
        assert result == ("Ankit", 132)

    # @pytest.mark.skip
    def test_find_highest_food_weight_returns_highest3(self):
        # Arrange
        food_brand_weights = [("FoodE", 5), ("FoodF", 8)]
        owner_purchases = [("Jose", "FoodE", 1), ("Sarah", "FoodF", 3), ("Jose", "FoodE", 2)]

        # Act
        result = find_highest_food_weight(food_brand_weights, owner_purchases)
        # Assert
        assert result == ("Sarah", 52)


if __name__ == "__main__":
    pytest.main()