"""1672. Richest Customer Wealth

Clarifying questions:
1. will data be clean? always have ints or need to format?
2. will n always be the same for each person?
3. could you have a person with no wealth?
4. can I use the built-in sum function? or have to calculate myself?


Examples
Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17

Brainstorm ideas:
1. have a variable to hold the wealthiest number, loop through the matrix for 
each account, sum each account, check if the current sum is the wealthiest,
when finish return the wealthiest.
2. use two pointers so only have to loop through 1x?

"""
def maximum_wealth(accounts: list[list]) -> int:
    if not accounts:
        return 0
    
    wealthiest = 0

    for account in accounts:
        current_wealthiest = sum(account)
        wealthiest = max(wealthiest, current_wealthiest)

    return wealthiest




def main():
    assert(maximum_wealth([[1,2,3],[3,2,1]])) == 6
    assert(maximum_wealth([[1,5],[7,3],[3,5]])) == 10
    assert(maximum_wealth([[2,8,7],[7,1,3],[1,9,5]])) == 17
    print("All tests passed!")

if __name__ == "__main__":
    main()
