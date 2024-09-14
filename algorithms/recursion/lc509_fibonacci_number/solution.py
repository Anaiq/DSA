
"""
509. Fibonacci Number

Clarifying questions:
1. Can n be 0? or starting at 1?
2. Is there a max n? will n fit in memory?
2. 

Example 1:

Input: n = 5
Output: 1
Explanation: F(5) = F(4) + F(3) = 3 + 2 = 5.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Brainstorm ideas:
1. base case = if n reaches 0 or 1 return 1, otherwise call the function on itself
for add the results of F(n-1) + F(n-2)
2.
"""

def fib(n: int) -> int:
    if n < 0 or type(n)!= int:
        raise ValueError
        
    # base case:
    if n <= 1:
        return n
    # recursive case
    return fib(n - 1) + fib(n - 2)

# Time: O(2^n)
# Space: O(n)


def main():
    assert fib(2) == 1
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(10) == 55
    print("All tests passed.")


if __name__ == "__main__":
    main()
