class Solution(object):
    def pSort(self, arr, pivot, low, high):
        i = j = low  
        k = high  

        while j <= k:
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            elif arr[j] > pivot:
                arr[j], arr[k] = arr[k], arr[j]
                k -= 1
            else:  
                j += 1

        return k  
    
    def quickSort(self, arr, low, high):
        self.arr = arr
        self.low = low
        self.high = high
        if low > high:
            return
        pivot = arr[high]
        pIndx = self.pSort(arr, pivot, low, high)
        self.quickSort(arr, low, pIndx - 1)
        self.quickSort(arr, pIndx + 1, high)
        return arr
        

mySol = Solution()
sample_array = [0, 2, 13, 40, 19, 90, -9, 87, 12, 1, -10]
low = 0
high = len(sample_array) - 1
QS = mySol.quickSort(sample_array, low, high)
print(QS)