# 217. Contains Duplicate

# A. First Solution (Easy)
# Using brute force method, we traverse the list to check each number if its appearing twice . 
# Time Complexity = O(n**2) as we are traversing the list of size n, n times for each integer.
# Space Complexity = O(1) as we are not storing anything.
	
# B. Second Solution (Medium)
# Using the sorting option to sort the list first. The check the two integers next to each other if they are same. 
# Time Complexity = O(nlogn) as sorting takes nlogn time. 
# Space Complexity = O(1) ignoring any space used for sorting the list.
	
# C. Third Solution (Hard)
# Using Hashset (Set) and storing each integer to check if any other integer exists which already is present in Hashset. The operations to check element in Hashset has time complexity of O(1)
# Time Complexity = O(n) because we are doing the check operation for all n elements in list (at max)
# Space Complexity = O(n) because we are storing the elements in the hashset for all n elements (at max)

# Refer the details on Sets from https://www.geeksforgeeks.org/sets-in-python/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for value in nums:
            if value in hashset:
                return True
            hashset.add(value)
        return False

