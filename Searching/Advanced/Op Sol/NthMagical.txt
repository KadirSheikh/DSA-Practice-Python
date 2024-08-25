class Solution(object):
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        lcm = a * b // self.gcd(a, b)
        
        low = min(a, b)
        high = n * min(a, b)
        MOD = 10**9 + 7
        ans = a
        
        while low <= high:
            mid = (low + high) // 2
            mul = (mid // a) + (mid // b) - (mid // lcm)
            if mul == n:
                ans = mid
                high = mid - 1
            if mul < n:
                low = mid + 1
            else:
                high = mid - 1
        
        return ans % MOD

        

mySolution = Solution()
n = 1000000000
a = 40000
b = 40000
ans = mySolution.nthMagicalNumber(n, a, b)
print("#####", ans)