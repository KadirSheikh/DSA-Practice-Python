class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        numDict = {}
        
        for i in nums:
            if str(i) not in numDict:  
                numDict[str(i)] = 1
            else:
                numDict[str(i)] += 1
                

        for key, value in numDict.items():
            if value == 1:
                return int(key)
                


============================================================================



class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums

        singleNum = 0
        for i in nums:
            singleNum = singleNum ^ i

        return singleNum