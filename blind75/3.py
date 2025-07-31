class Solution:
    def twoSum(self, nums, target: int):
        hash = {}
        for i, n in enumerate(nums):
            hash[n] = i
        for i, n in enumerate(nums):
            diff = target-n
            if diff in hash and hash[diff]!= i:
                return [i, hash[diff]]
        return [-1, -1]
    
nums = [5,5]
target = 10

print(Solution().twoSum(nums, target))