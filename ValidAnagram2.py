# Leetcode Question #242

# Time Complexity: O(s + t)
# Space Complexity: O(s + t)

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    # Base case if the strings aren't the same length, it can't be an anagram
    if len(s) != len(t):
        return False
    

    countS, countT = {}, {} # Key, Value -> char, count of char

    for i in range(len(s)):
        # Adding each char of s & t into their respective maps
        # and adding 1 to the count of each char
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS:
        # If the count of a char is not the same between countS & countT
        # return False
        if countS[c] != countT.get(c, 0): # Must use .get() to avoid error
            return False
    
    return True

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s,t)) # Expected: True

    s = "rat"
    t = "car"
    print(isAnagram(s, t)) # Expected: False