# 20. Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']' ,
# determine if the input string is valid.

# The brackets must close in the correct order, 
# "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if not s:
            return True
        for i in range(len(s)):
            if ( s[i] == ("(") ):
                stack.append("(")
            elif ( s[i] == ("[") ):
                stack.append("[")
            elif ( s[i] == ("{") ):
                stack.append("{")
            elif ( s[i] == (")") ):
                if ( len(stack) == 0 or stack[-1] != "(" ):
                    return False
                stack.pop()
            elif ( s[i] == ("]") ):
                if ( len(stack) == 0 or stack[-1] != "["):
                    return False
                stack.pop()
            elif ( s[i] == ("}") ):
                if ( len(stack) == 0 or stack[-1] != "{"):
                    return False
                stack.pop()      
        if ( len(stack) == 0 ):
            return True
        return False