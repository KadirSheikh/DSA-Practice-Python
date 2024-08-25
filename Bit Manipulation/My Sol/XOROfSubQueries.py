class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        self.arr = arr
        self.queries = queries
        
        XORAns = []
        
        for i in queries:
            left = i[0]
            right = i[1]
            xor = arr[left]
            for j in range(left + 1, right + 1):
                xor = xor ^ arr[j]
            XORAns.append(xor)
            
        return XORAns
                
        

mySolution = Solution()
arr = [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]
ans = mySolution.xorQueries(arr, queries)

print("#####", ans)