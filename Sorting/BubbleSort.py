class Solution(object):
    def bubbleSort(self, arr):
        """
        :type n: int
        :rtype: int
        """
        self.arr = arr
        n = len(arr)
        
        for i in range(n):
            swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
                    swapped = True
                    
            if not swapped:
                break
                
        print("Sorted Array", arr)        
mySol = Solution()

sample_array = [4, 7, 2, 9, 1, 5, 3, 8, 6, 0]

BS = mySol.bubbleSort(sample_array)


# ##################################################################################################################3

class Solution(object):
    def bubbleSort(self, arr):
        """
        :type n: int
        :rtype: int
        """
        self.arr = arr
        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j+1] , arr[j] = arr[j] , arr[j+1]
        print("Sorted Array", arr)        
mySol = Solution()
sample_array = [4, 7, 2, 9, 1, 5, 3, 8, 6, 0]
BS = mySol.bubbleSort(sample_array)