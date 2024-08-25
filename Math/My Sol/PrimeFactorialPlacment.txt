class Solution(object):
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
        
    def factorial(self, num):
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact
    
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        
        primes = 0
        non_primes = 0

        for i in range(1, n+1):
            if self.is_prime(i):
                primes += 1
            else:
                non_primes += 1
                    
        return (self.factorial(primes) * self.factorial(non_primes)) % (10**9 + 7)