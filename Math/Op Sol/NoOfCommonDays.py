class Solution(object):
    
    def getTotalDays(self, date):
        total = 0
        yearDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        month = date.split("-")[0]
        days = date.split("-")[1]
        
        for i in range(int(month) - 1):
            print(i)
            total += yearDays[i]
            
        total += int(days)
        return total
        
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        self.arriveAlice = arriveAlice
        self.leaveAlice = leaveAlice
        self.arriveBob = arriveBob
        self.leaveBob = leaveBob
        
        
        a = self.getTotalDays(arriveAlice)
        b = self.getTotalDays(leaveAlice)
        c = self.getTotalDays(arriveBob)
        d = self.getTotalDays(leaveBob)

        if b < c or d < a:
            return 0
        
        data = abs(max(a, c) - min(b, d))
    
        return data + 1
        

mySol = Solution()

arriveAlice = "08-15"
leaveAlice = "08-20"
arriveBob = "08-16"
leaveBob = "08-19"

commonDays = mySol.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
print(commonDays)