# 1. Two Sum

# A. First Solution (Easy)
# Using two for loops for traversing the list twice and then adding the elements which result in target.
# Time Complexity = O(n**2) since we are checking the list twice.
# Space Complexity = O(1) since we are not storing any value.

# B. Second Solution (Medium)
# Using dictionaries and checking the indexes traversed.
# Time Complexity = O(n) as we traverse only once in the list and to check in dictionary is O(1)
# Space Complexity = O(n) as we are storing data in a dictionary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dict1.keys():
                return [dict1.get(target - nums[i]),i]
            dict1[nums[i]] = i
