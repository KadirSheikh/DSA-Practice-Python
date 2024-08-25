class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        self.arr = arr
        self.queries = queries
        
        xorArr = [0] * (len(arr) + 1)
        print(xorArr)
        xorAns = []

        for i in range(1, len(arr) + 1):
            print(xorArr[i - 1], arr[i - 1])
            xorArr[i] = xorArr[i - 1] ^ arr[i - 1]
            
        for left, right in queries:
            print("left", left)
            print("right", right)
            xor_result = xorArr[left] ^ xorArr[right + 1]
            xorAns.append(xor_result)
                
        print(xorAns)
        return xorAns

mySolution = Solution()
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
ans = mySolution.xorQueries(arr, queries)

print("#####", ans)