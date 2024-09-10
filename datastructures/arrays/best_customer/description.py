"""
At the local Pet Store, a variety of dog food is available, and the amount of dog 
food each owner purchased was recorded. Your task is to analyze this data to find 
out which owner bought the highest amount of dog food.

Write a function called find_highest_food_weight that takes two arguments:

food_brand_weights: a list of tuples where each tuple contains a food brand name (string) and 
the weight of the food bought (integer). The weight represents how much dog food 
(in kilograms) was purchased for that dog.

owner_purchases: a list of tuples where each tuple contains an owner's name (string), 
the name of the food brand they purchased (string), and the quantity of that dog food (integer). 
The quantity represents how many bags of that food was purchased.

The function should return the name of the owner who spent the highest amount on dog 
food and the total pounds of food they bought  (round down to nearest pound). If there are no purchases, return None.

Constraints:

The dog names are unique.
Each owner can purchase any dog food multiple times, and their purchases will be listed
as separate entries in the owner_purchases list.
The weights are positive integers, and the quantities are non-negative integers.

Example 1
Input:
food_brand_weights = [("FoodA", 10), ("FoodB", 20), ("FoodC", 15)]
owner_purchases = [("Ankit", "FoodA", 3), ("Bob", "FoodB", 1), ("Ankit", "FoodC", 2)]

Output:"Ankit", 132


Example 2:
food_brand_weights = [("FoodE", 5), ("FoodF", 8)]
owner_purchases = [("Jose", "FoodE", 1), ("Sarah", "FoodF", 3), ("Jose", "FoodE", 2)]

"Jose", 39
"""


food_brand_weights = [("FoodA", 3), ("FoodB", 9)]
owner_purchases = [("Barry", "FoodA", 1), ("Keisha", "FoodB", 3), ("Barry", "FoodA", 2)]