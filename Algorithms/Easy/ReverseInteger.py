# 7. Reverse Integer

# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

# Note:
# The input is assumed to be a 32-bit signed integer.
# Your function should return 0 when the reversed integer overflows.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        if (x > 0):
            ans = int(str(x)[::-1])
        elif (x < 0):
            x = x*-1
            ans = int(str(x)[::-1])
            ans = ans*-1
        
        if(ans > 2147483647 or ans < -2147483648):
            return 0
        else:
            return ans