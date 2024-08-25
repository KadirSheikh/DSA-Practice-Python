class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        self.s = s
        self.goal = goal
         
        if len(s) != len(goal):
            return False

        s = s + s

        if goal in s:
            return True
                
        return False
        