class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        self.num1 = nums1
        self.num2 = nums2
        
        startArr = nums1
        endArr = nums2
        
        intersection = []
        
        if len(nums1) > len(nums2):
            startArr = nums2
            endArr = nums1
            
        for i in range(len(startArr)):
            for j in range(len(endArr)):
                if startArr[i] == endArr[j]:
                    intersection.append(startArr[i])
                    endArr[j] = float('-inf')
                    break
        
        return intersection