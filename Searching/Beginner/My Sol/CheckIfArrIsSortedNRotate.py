class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.nums = nums
        
        copyNums = nums[:]
        nums.sort()     

        for i in range(len(nums)):
            firstEle = nums[0]
            nums = nums[1:len(nums)]
            nums.append(firstEle)
            if nums == copyNums:
                return True
                
        return False