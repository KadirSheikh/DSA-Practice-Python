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

        for i in s:
            s = s[1:len(s)] + s[:1]
            if s == goal:
                return True
                
        return False
        