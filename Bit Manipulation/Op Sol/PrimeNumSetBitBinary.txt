class Solution(object):
    def checkIfPrime(self, num):
        self.num = num
        
        if num < 2:
            return False
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
                
        return True
        
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        self.left = left
        self.right = right
        
        primeCount = 0
        
        for i in range(left, right + 1):
            num = i
            count = 0
            while num != 0:
                bit = num % 2
                if bit == 1:
                    count += 1
                num = num // 2
                
            if self.checkIfPrime(count):
                    primeCount += 1
                    
                
        return primeCount