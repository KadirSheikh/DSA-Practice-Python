class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        totalXor = 0
        calculateXor = 1
        xornum = nums[0]
        firstNum = nums[0]

        
        for i in nums:
            calculateXor = calculateXor ^ i
            totalXor += calculateXor
            
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i >= j:
                    continue
                corrXor = nums[i] ^ nums[j]
                totalXor += corrXor
        
        if len(nums) > 2:
            for i in nums[1:len(nums)]:
                xornum = xornum ^ i

        return totalXor+xornum
        
mySol = Solution()
nums = [3,4,5,6,7,8]
isPower = mySol.subsetXORSum(nums)

print(isPower)