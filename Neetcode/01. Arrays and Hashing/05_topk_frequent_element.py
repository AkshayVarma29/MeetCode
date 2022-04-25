# 347. Top K Frequent Elements

# First Solution has time complexity of O(nlogn) + O(n) since we used sorting and dictionary.
# Second Solution has time complexity of O(n)as we traversed it without sorting.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        # frep = [[] for i in range(len(nums) + 1)] 
        result = []
        for num in nums:
            dict1[num] = 1 + dict1.get(num,0)
            
        values = sorted(dict1.values(),reverse=True)
        for key, value in dict1.items():
            if value in values[:k]:
                result.append(key)
        return result

        # for num, count in dict1.items:
        #     freq[count].append(num)

        # for i in range(len(freq) -1, 0, -1):
        #     for n in freq[i]:
        #         result.append(n)
        #         if len(result) == k:
        #             return result