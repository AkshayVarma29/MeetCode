class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dict1 = {}
        N = len(nums)
        for list1 in nums:
            for value in list1:
                dict1[value] = 1 + dict1.get(value,0)
        
        result = []
        for key, value in dict1.items():
            if value == N:
                result.append(key)
        return sorted(result)