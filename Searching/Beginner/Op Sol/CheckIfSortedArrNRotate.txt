class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_decreasing_points = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                count_decreasing_points += 1
            if count_decreasing_points > 1:
                return False
        return True