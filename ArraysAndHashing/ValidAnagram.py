# Leetcode Question #242

# Time Complexity O(nlogn)
# Space Complexity O(1)

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    # If the sorted versions of s & t are equal, they are anagrams
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s,t)) # Expected: True

    s = "rat"
    t = "car"
    print(isAnagram(s, t)) # Expected: False