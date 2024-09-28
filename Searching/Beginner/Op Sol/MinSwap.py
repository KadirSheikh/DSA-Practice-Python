class Solution:
	def minSwaps(self, nums):
	    self.nums = nums
	    sorted_nums = sorted(nums)
	    ans = 0
	    left = 0
	    hash_map = {
	       sorted_nums[i]:i for i in range(len(sorted_nums))
	    }
	    print(hash_map)
	    while left < len(nums):
	        if left == hash_map[nums[left]]:
	            left += 1
	        else:
	            print("nums[hash_map[nums[left]]]", nums[hash_map[nums[left]]])
	            print("nums[left]", nums[left])
	            nums[hash_map[nums[left]]], nums[left] = nums[left], nums[hash_map[nums[left]]]
	            ans += 1
	            
	    return ans
	    
mySol = Solution()
sample_array = [2, 8, 5, 4]
MS = mySol.minSwaps(sample_array)
print(MS)