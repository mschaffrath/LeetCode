# 13. Roman to Integer

# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        lastval = 0
        for i in range(0, len(s)):
            if(s[i] == "M"):
                num = num + 1000
                if lastval < 1000:
                    num = num - lastval*2
                lastval = 1000
            elif(s[i] == "D"):    
                num = num + 500
                if lastval < 500:
                    num = num - lastval*2
                lastval = 500
            elif(s[i] == "C"):
                num = num + 100
                if lastval < 100:
                    num = num - lastval*2
                lastval = 100
            elif(s[i] == "L"):
                num = num + 50
                if lastval < 50:
                    num = num - lastval*2
                lastval = 50
            elif(s[i] == "X"):
                num = num + 10
                if lastval < 10:
                    num = num - lastval*2
                lastval = 10
            elif(s[i] == "V"):
                num = num + 5
                if lastval < 5:
                    num = num - lastval*2
                lastval = 5
            elif(s[i] == "I"):
                num = num + 1
                if lastval < 1:
                    num = num - lastval*2
                lastval = 1
        return num



    ### ADD TESTING