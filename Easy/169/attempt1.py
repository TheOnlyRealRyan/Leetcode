# Wrong Answer 23 / 52 testcases passed
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # what if number is less than majority (question states wont happen)
        nums.sort() # O(logN)
        print(nums)
        max_num = 0
        new_num = 0
        stored_value = nums[0]
        output = nums[0]
        if len(nums) == 1:
            return nums[0]

        for char in nums:
            if char == stored_value:
                max_num += 1
            elif max_num >= new_num:
                print(char, max_num, new_num)
                output = char
                new_num = max_num
                max_num = 0
        
        return output