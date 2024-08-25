class Solution(object):
    def binarySearchFirstOccurance(self, x, low, arr):
        """
        :type n: int
        :rtype: int
        """
        self.arr = arr
        self.x = x
        self.low = low
        
        high = len(arr) - 1
        index = -1
        arr.sort()
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == x:
                index = mid
                high = mid - 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return index
        
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
            
        startArr.sort()
        endArr.sort()
        low = 0
        
        for i in startArr:
            index = self.binarySearchFirstOccurance(i, low, endArr)
            if index != -1:
                intersection.append(endArr[index])
                low = index + 1
            
        return intersection