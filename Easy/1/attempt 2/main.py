
class Solution(object):
    def twoSum(self, nums, target):
        print(type(nums))
        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0,1]
        
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                if i + j == target:
                    return [i,j]

        # create new arrays with numbers smaller than target
        for i in range(len(nums))-1:
            if nums[i] < target:
                new_array.append(nums[i])

            
                

nums = [3,2,6,8]
target = 9
print(Solution.twoSum(Solution, nums, target))