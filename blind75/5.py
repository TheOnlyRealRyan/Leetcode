class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        # search through the count portion and pull the k largest numbers
        # sort? max query? 
        # Below is getting too complicated to be solution
        maxarray=[]
        for key in hash:
            if len(maxarray)<k:
                maxarray.append(key)
            elif hash[key] > max(maxarray):
                maxarray.remove(hash[key])
                maxarray.append(key)
        
        # search through max values and look in hash map and return key
        
nums = [1,2,2,3,3,3]
k = 2  
Solution().topKFrequent(nums, k)