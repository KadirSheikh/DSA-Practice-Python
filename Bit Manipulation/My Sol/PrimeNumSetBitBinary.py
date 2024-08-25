class Solution(object):
    def convertToBinary(self, num):
        self.num = num
        binary = ""
        while num != 0:
            remainder = num % 2
            binary = str(remainder) + binary
            num = num // 2
            
        return binary
        
    def countOneInBinary(self, binary):
        self.binary = binary
        
        count = 0
        for i in binary:
            if i == "1":
                count += 1
                
        return count
            
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
            binaryVal = self.convertToBinary(i)
            countNumOfOne = self.countOneInBinary(binaryVal)
            isPrime = self.checkIfPrime(countNumOfOne)
            
            if isPrime:
                primeCount += 1
                
        return primeCount