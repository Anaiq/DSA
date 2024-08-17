"""
9. Palindrome Number

Understand the Question:
I am given a integer number, if it is a palindrome, return True, if not return False.

Clarifying questions:
1. Could I be given a negative number?
2. How large could the number be? Will it fit in memory?
3. Can I use built-in methods? 

Examples
82 -> False
28482 -> True
-902101209 -> False

Brainstorm ideas:
1.  Convert the number to a string, reverse it using reversed(), check if new string[0] is '-'
if yes, then return false,  if not check if string == new string, if yes return True
2. Convert to string and use 2 pointers with 1 at start and end or string, loop through string checking
if the char at l pointer  == char at r pointer, if not return False  (no need to check further)
if y, continue checking until all chars are compared and return True if all match
3. No conversion, use modulo, creating new list - O(n)memory. create a empty, 
use modulo to get last digit and add to list, compare the reversed array
4.  no string conversion - constant O(1) memory - create a variable to hold result
use loop while still have digits and modulo to get last digit add to result
compare original number and result number, True if ==, False if not.
"""

# # sol.1
def is_palindrome(x: int) -> bool:
    str_x = convert_int_to_str(x)
    reversed_str_x = "".join(reversed(str_x))

    if reversed_str_x.isdigit() and x == int(reversed_str_x):
        return True
    return False

# Time: O(n)
# Space: O(n) 

# sol.2
# def is_palindrome(x: int) -> bool:
#     str_x = convert_int_to_str(x)
#     l = 0
#     r = len(str_x) -1

#     while l < r:
#         if str_x[l] != str_x[r]:
#             return False
#         l += 1
#         r -=1
#     return True

# Time: O(n/2) -> O(n)
# Space: O(n) 

# sol.3
# def is_palindrome(x: int) -> bool:
#     if is_negative(x):
#         return False
#     x_list = []
#     while x > 0:
#         remainder = x % 10
#         x_list.append(remainder)
#         x = x // 10

#     return x_list == x_list[::-1]

# Time: O(n) -> where n is number of decimal places
# Space: O(n) 

# # sol.4
# def is_palindrome(x: int) -> bool:
#     if is_negative(x):
#         return False
    
#     result_num = 0
#     num = x

#     while num > 0:
#         print(num)
#         result_num = (result_num * 10) + (num % 10)
#         print(result_num)
#         num //= 10

#     return result_num == x

# Time: O(n)
# Space: O(1) 

def convert_int_to_str(x:int) -> str:
    return str(x)

def is_negative(x):
    return x < 0

def main():
    assert is_palindrome(82) == False
    assert is_palindrome(28482) == True
    assert is_palindrome(-902101209) == False
    assert is_palindrome(1000550001) == True

    print("assertion tests passed!")


if __name__ == "__main__":
    main()


