class Solution(object):
    def insertionSort(self, arr):
        """
        :type n: int
        :rtype: int
        """
        self.arr = arr
        n = len(arr)

        for i in range(1, n):
            j = i - 1
            while j >= 0 and arr[j] > arr[j+1]:
                arr[j + 1], arr[j] = arr[j], arr[j+1]
                j -= 1
                
        print("Sorted Array", arr)        
mySol = Solution()

sample_array = [4, 7, 2, 9, 1, 5, 3, 8, 6, 0]

IS = mySol.insertionSort(sample_array)