# Leetcode Question #121

# Time Complexity: O(n)
# Space Complexity: O(1)

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    Left, Right = 0, 1  # Left & Right pointers
    maxProfitVal = 0    # Initialize max profit to 0

    # Continue looping through our array until we reach the end
    while Right < len(prices):  # <-- FIX: was <=
        # Does the current indices of prices result in a profit?
        if prices[Right] > prices[Left]:
            profit = prices[Right] - prices[Left]
            maxProfitVal = max(maxProfitVal, profit)
        # If not, update the left pointer
        else:
            Left = Right
        Right += 1

    return maxProfitVal

if __name__ == "__main__":
    tests = [
        # LeetCode examples
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),

        # Extra useful tests
        ([1], 0),                 # single day
        ([2, 1], 0),              # decreasing
        ([1, 2], 1),              # increasing
        ([2, 4, 1], 2),           # classic: buy 2 sell 4
        ([3, 3, 3, 3], 0),        # flat
        ([4, 1, 5, 2, 7], 6),      # from discussion example
        ([0, 0, 0, 1], 1),         # zeros then rise
    ]

    for i, (prices, expected) in enumerate(tests, 1):
        got = maxProfit(prices)
        print(f"Test {i}: prices={prices}")
        print(f"  Output:   {got}")
        print(f"  Expected: {expected}")
        print(f"  Pass:     {got == expected}\n")
