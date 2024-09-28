class Solution:
	def minSwaps(self, nums):
	    self.nums = nums
	    
	    currentArr = nums[:]
	    nums.sort()
	    count = 0
	    
	    for i in range(len(currentArr)):
	        if currentArr[i] != nums[i]:
	            count += 1
	            
	    if count != 0:
	        return (count - 1)
	        
	    return count
	    
mySol = Solution()
sample_array = [2, 8, 5, 4]
MS = mySol.minSwaps(sample_array)
print(MS)