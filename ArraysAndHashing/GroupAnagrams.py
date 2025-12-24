# Leetcode Question #49

# Time Complexity: O(n * m)
# Space Complexity: O(n)

from collections import defaultdict

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    # Defining a dictionary with values as a list
    res = defaultdict(list) # Key, Value -> charCount, list of Anagrams

    for string in strs:
        count = [0] * 26 # One bucket of 0 for each char in the alphabet

        for char in string:
            # Using the ASCII values to map each char to it's respective bucket
            # Ex. 'a' is index 0, 'z' is index 25, and adding 1
            count[ord(char) - ord("a")] += 1

            # Lists can't be keys in Python, so we must convert count to a tuple
            res[tuple(count)].append(string)

    return res.values() # returning the list of anagrams (the values of res)

if __name__ == "__main__":
    # Test Case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Test Case 1 Output:", groupAnagrams(strs1))
    # Expected (order may vary):
    # [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    # Test Case 2
    strs2 = [""]
    print("Test Case 2 Output:", groupAnagrams(strs2))
    # Expected: [[""]]

    # Test Case 3
    strs3 = ["a"]
    print("Test Case 3 Output:", groupAnagrams(strs3))
    # Expected: [["a"]]

    # Additional Edge Case
    strs4 = ["", "b", ""]
    print("Test Case 4 Output:", groupAnagrams(strs4))
    # Expected: [["", ""], ["b"]]
