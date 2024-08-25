class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        self.num = num
        res = [0] * 4
        i = 0
        while num > 0:
            remainder = num % 10
            num = num // 10
            res[i] = remainder
            i += 1
        res.sort()
        print(res)
        return res[0]*10 + res[2] + res[1]*10 + res[3]