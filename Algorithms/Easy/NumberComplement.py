# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binNumStr = str(bin(num))
        binNumStr = binNumStr[2:]
        binNumStr = binNumStr.replace("0", "2")
        binNumStr = binNumStr.replace("1", "0")
        binNumStr = binNumStr.replace("2", "1")
        return int(binNumStr, 2)
       
