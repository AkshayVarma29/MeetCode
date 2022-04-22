# 242. Valid Anagram

# A. First Solution (Easy)
# Using dictionaries and storing the count of each letter. We can compare the length of both strings and check if count of each letter is same in both the dictionaries.
# Time Complexity = O(s+t) as we will be interating over both the strings.
# Space Complexity = O(s+t) as we will be storing two dictionaries.

# B. Second Solution (Easy)
# Using sorted strings. However, the sort operations will cost time and space.
# Time Complexity = O(n2) being worst to O(nlogn) being best.
# Space Complexity = O(n) but sometimes O(1).

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            dict1[s[i]] = 1 + dict1.get(s[i],0)
            dict2[t[i]] = 1 + dict2.get(t[i],0)

        for key, value in dict1.items():
            if key in dict2.keys() and value == dict2[key]:
                continue
            return False
        return True