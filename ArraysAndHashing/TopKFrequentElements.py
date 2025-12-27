# Leetcode Question #347

# Time Complexity : O(n)
# Space Complexity: O(n)

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    count = {} # Key, Value -> Value, Frequency

    # Buckets where index = frequency, value = list of numbers
    freq = [[] for i in range(len(nums) + 1)]

    # Populate frequency map
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # Place numbers into frequency buckets
    for n, c in count.items():
        freq[c].append(n)

    # Collect top k frequent elements starting from highest frequency
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

if __name__ == "__main__":
    # Test Case 1
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print("Test 1 Output:", topKFrequent(nums, k))  # Expected: [1, 2]

    # Test Case 2
    nums = [1]
    k = 1
    print("Test 2 Output:", topKFrequent(nums, k))  # Expected: [1]

    # Test Case 3
    nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    k = 2
    print("Test 3 Output:", topKFrequent(nums, k))  # Expected: [1, 2]