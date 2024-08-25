class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        
        self.date = date
        
        dateData_normal = {
            "01": 0,    # January
            "02": 31,   # February
            "03": 59,   # March
            "04": 90,   # April
            "05": 120,  # May
            "06": 151,  # June
            "07": 181,  # July
            "08": 212,  # August
            "09": 243,  # September
            "10": 273,  # October
            "11": 304,  # November
            "12": 334   # December
        }
        
        dateData_leap = {
            "01": 0,    # January
            "02": 31,   # February
            "03": 60,   # March
            "04": 91,   # April
            "05": 121,  # May
            "06": 152,  # June
            "07": 182,  # July
            "08": 213,  # August
            "09": 244,  # September
            "10": 274,  # October
            "11": 305,  # November
            "12": 335   # December
        }
        
        year = int(date.split('-')[0])
        month = date.split('-')[1]
        date = date.split('-')[2]
        
        if year % 4 == 0 and year != 1900:
            return dateData_leap[month] + int(date) 
            
        return dateData_normal[month] + int(date) 

mySol = Solution()

dayOfYr = mySol.dayOfYear("1900-05-02")

print(dayOfYr)