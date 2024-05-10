class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums[:] = sorted(set(nums))
        return nums
        
        """
        # This solution didnt include the step of NOT adding a new array
        new_array = []
        if len(nums) > 0:
            new_array.append(nums[0])
        for i in nums:
            if i != new_array[-1]:
                new_array.append(i)
        return new_array
        """

# nums = [1,1,2]        
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(Solution, nums))