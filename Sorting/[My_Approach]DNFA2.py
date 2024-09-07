class Solution(object):
    def dutchNatFlag(self, arr):
        self.arr = arr
        
        n = len(arr)
        i = j = 0
        numZeros = 0
        
        while(i < n):
            if arr[i] == 0:
                numZeros += 1
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            else:
                i+=1
                
        z = numZeros
        
        while(numZeros < n):
            if arr[numZeros] == 1:
                arr[numZeros], arr[z] = arr[z], arr[numZeros]
                numZeros += 1
                z += 1
            else:
                numZeros+=1
            
        
        return arr

mySol = Solution()
sample_array = [0, 1, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 1, 0, 2]
DNFA = mySol.dutchNatFlag(sample_array)
print(DNFA)