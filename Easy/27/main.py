class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count=0
        while count <= len(nums)-1:
            if nums[count] == val:
                nums.remove(nums[count])
                count -= 1             
            count+=1
        return len(nums)  
        

nums = [0,1,2,2,3,0,4,2]
val = 2 
print(Solution.removeElement(Solution, nums, val))