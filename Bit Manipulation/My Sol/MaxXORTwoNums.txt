class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        self.nums = nums
        maxXor = 0
        
        if len(nums) <= 1:
           return 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                findXor = nums[i] ^ nums[j]
                if findXor > maxXor:
                    maxXor = findXor

        return maxXor

mySolution = Solution()
nums = [14,70,53,83,49,91,36,80,92,51,66,70]
ans = mySolution.findMaximumXOR(nums)

print("#####", ans)