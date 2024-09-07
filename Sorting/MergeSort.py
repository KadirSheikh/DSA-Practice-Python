class Solution(object):
    def mergeTwoSortedArr(self, firstArr, secondArr):
        self.firstArr = firstArr
        self.secondArr = secondArr
        
        n = len(firstArr)
        m = len(secondArr)
        resArr = []
        i = j = 0
        
        while(i < n and j < m):
            if firstArr[i] < secondArr[j]:
                resArr.append(firstArr[i])
                i += 1
            else:
                resArr.append(secondArr[j])
                j += 1
    
        while i < n:
            resArr.append(firstArr[i])
            i += 1
        
        while j < m:
            resArr.append(secondArr[j])
            j += 1
            
        return resArr
        
    def mergeSort(self, arr, low, high):
        self.arr = arr
        
        if low == high:
            baseArr = []
            baseArr.append(arr[low])
            return baseArr
        
        mid = (low + high) // 2
        firstHalf = self.mergeSort(arr, low, mid)
        secondHalf = self.mergeSort(arr, mid + 1, high)
        return self.mergeTwoSortedArr(firstHalf, secondHalf)

mySol = Solution()
sample_array = [4, 7, 2, 9, 1, 5, 3, 8, 6, 0]
low = 0
high = len(sample_array) - 1
MS = mySol.mergeSort(sample_array, low, high)

print(MS)