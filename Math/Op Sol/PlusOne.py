class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self.digits = digits
        n = len(digits) - 1
        for i in range(n, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        if digits[0] == 0:
            return [1] + digits

        return digits