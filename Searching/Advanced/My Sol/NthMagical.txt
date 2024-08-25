class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        self.n = n
        self.a = a
        self.b = b
        
        low = min(a, b)
        high = low * n
        
        magicalNums = []
        
        if n <= 1:
            return a
            
        for i in range(low, high + 1):
            print(i)
            if i % a == 0 or i % b == 0:
                magicalNums.append(i)
        
        print(magicalNums)
        return magicalNums[n - 1]