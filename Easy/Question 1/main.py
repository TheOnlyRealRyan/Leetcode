def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))