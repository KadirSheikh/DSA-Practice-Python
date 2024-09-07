class Solution(object):
    def selectionSort(self, arr):
        """
        :type n: int
        :rtype: int
        """
        self.arr = arr
        n = len(arr)
        
        for i in range(n):
            minEle = i
            for j in range(i+1, n):
                if arr[j] < arr[minEle]:
                    minEle = j
            arr[i], arr[minEle] = arr[minEle], arr[i]
                
        print("Sorted Array", arr)        
mySol = Solution()

sample_array = [4, 7, 2, 9, 1, 5, 3, 8, 6, 0]

SS = mySol.selectionSort(sample_array)