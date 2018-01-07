# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero.
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

# Note:
# The boundaries of each input argument are 1 <= left <= right <= 10000.


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        #Helper function
        def isSelfDiv(num):
            sNum = str(num)
            for n in sNum:
                if num % int(n) != 0:
                    return False
            return True
        
        #Driver
        ans = []
        for i in range (left, right+1):
            checkForZero = str(i)
            if checkForZero.count('0') > 0:
                continue
            else:
                if isSelfDiv(i):
                    ans.append(i)
        return ans
