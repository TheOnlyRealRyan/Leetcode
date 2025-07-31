class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash = {}
        for i in nums:
            if hash[nums] not in hash:
                hash[nums] = 1
            else:
                hash[nums] += 1
        # search through the count portion and pull the k largest numbers
        # sort? max query? 

nums = [1,2,2,3,3,3]
k = 2  
Solution().topKFrequent(nums, k)