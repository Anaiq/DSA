"""sample interview question - find_highest_weight

input: list of tuples - (brandname, food_weight (kg)), (owner, quantity)
output: name, weight (pounds)

constraints:
no duplicate dog names
multiple purchases by an owner, will be listed separately
weights and quantity are non-negative integers
"""
from collections import defaultdict


def find_highest_food_weight(food_brand_weights, owner_purchases):
    # loop through the list of owners
    # check which brand of food they bought
    # calculate the amount of food they bought
    # return the amount of food

    if not food_brand_weights or not owner_purchases:
        return None
    
    weight_dict = defaultdict(int)
    owner_weight_dict = defaultdict(int)

    for brand, amount in food_brand_weights:
        weight_dict[brand] = amount
    print(weight_dict)


    for owner, brand, amount in owner_purchases:
        print("owner:", owner)
        current_weight = convert_kg_to_pounds(weight_dict[brand] * amount)
        owner_weight_dict[owner] += current_weight
    person_with_most_food = max(zip(owner_weight_dict.values(), owner_weight_dict.keys()))#[1]
    # print(person_with_most_food)
    return person_with_most_food, owner_weight_dict[person_with_most_food]
    return None

def convert_kg_to_pounds(weight):
    KG_CONVERSION = 2.2
    return int(weight * KG_CONVERSION)


def main():
    assert find_highest_food_weight([], []) == None
    assert find_highest_food_weight([("FoodA", 3), ("FoodB", 9)], [("Barry", "FoodA", 1), ("Keisha", "FoodB", 3), ("Barry", "FoodA", 2)]) == None#("Keisha", 59)
    assert find_highest_food_weight([("FoodA", 10), ("FoodB", 20), ("FoodC", 15)], [("Ankit", "FoodA", 3), ("Bob", "FoodB", 1), ("Ankit", "FoodC", 2)]) == ("Ankit", 132)
    assert find_highest_food_weight([("FoodE", 5), ("FoodF", 8)], [("Jose", "FoodE", 1), ("Sarah", "FoodF", 3), ("Jose", "FoodE", 2)]) == ("Sarah", 52)
    print("assertion tests passed!")


if __name__ == "__main__":
    main()
