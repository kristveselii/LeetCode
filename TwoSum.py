# LeetCode Question #1

# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    seen = {} # Mapping value's to indexes
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index

if __name__ == "__main__":
    # Test Case 1
    nums = [2, 7, 11, 15]
    target = 9
    print("Test 1 Output:", twoSum(nums, target))  # Expected: [0, 1]

    # Test Case 2
    nums = [3, 2, 4]
    target = 6
    print("Test 2 Output:", twoSum(nums, target))  # Expected: [1, 2]

    # Test Case 3
    nums = [3, 3]
    target = 6
    print("Test 3 Output:", twoSum(nums, target))  # Expected: [0, 1]