class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        add = 0
        
        arr = []
        for i in str(n):
            arr.append(i)
            
        for i in range(1, len(arr) + 1):
            if i % 2 == 1:
                add = add + int(arr[i-1])
            else:
                add = add - int(arr[i-1])
            
        return add
                
mySol = Solution()

altSum = mySol.alternateDigitSum(521)
print(altSum)