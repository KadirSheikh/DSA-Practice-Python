class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        add = 0
        product = 1

        while(n != 0):
            last = n % 10
            add += last
            product *= last
            n = n / 10
        
        return product - add
        