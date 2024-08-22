"""
20. Valid Parentheses
Understand the Question:
given a string containing only '(', ')', '{', '}', '[' and ']', return True if 
the string is 'valid' and False otherwise. A valid string is such that all open brackets 
must be closed by same type and in the correct sequence and a closed bracket has
a same open bracket.

Clarifying questions:
1. Is there a min and max length to the string?
2. Does it fit in memory?
3. Could it be empty? No, will have at least 1 bracket

Examples
Input: s = "(((])))"
Output: False

Input: s = ")]"
Output: False

Brainstorm ideas:
1. an even number of brackets would yield a string with even length. if string
length is odd, return False, if even check for matching brackets by looping
over chars and comparing each, using two pointers? 
2. have a valid-pair dict where key is closed bracket and value is open bracket
loop through the string. 
check if each char is a dict key:True:
    check if the stack is empty OR if the last bracket in the stack is NOT the matching bracket. 
        if is True, return False
    pop the last bracket from the stack
if the bracket is not in the dic keys, append bracket to the stack
if successfully made it through the string, check if the stack length is 0: all 
pairs would have been appended and popped from stack, no pairs left in stack

"""
from collections import deque
def isValid(string:str) -> bool:
    my_stack = deque()
    valid_pair_dict = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    for bracket in string:
        if bracket in valid_pair_dict:
            if not my_stack or my_stack[-1] != valid_pair_dict[bracket]:
                return False
            my_stack.pop()
        else:
            my_stack.append(bracket)

    return len(my_stack) == 0

def main():
    assert isValid(")]") == False
    assert isValid("()[]{}") == True
    assert isValid("([)]") == False
    assert isValid("]") == False
    assert isValid("()") == True
    assert isValid("(}") == False
    print("assertion tests passed!")


if __name__ == "__main__":
    main()

