class Solution(object):
    def dutchNatFlag(self, arr):
        self.arr = arr
        
        n = len(arr) - 1
        i = j = 0
        
        while(i < n):
            if arr[i] == 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            elif arr[i] == 2:
                arr[i], arr[n] = arr[n], arr[i]
                n -= 1
            else:
                i+=1
        
        return arr

mySol = Solution()
sample_array = [0, 1, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 1, 0, 2]
DNFA = mySol.dutchNatFlag(sample_array)
print(DNFA)