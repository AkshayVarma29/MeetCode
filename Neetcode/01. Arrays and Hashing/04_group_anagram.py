# 49. Group Anagrams

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list) # mapping the charcount to list of anagrams
        
        for s in strs:
            count = [0]*26 # a - z
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            res[tuple(count)].append(s)
        return res.values()
            
strs = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
result = obj.groupAnagrams(strs)
print(result)