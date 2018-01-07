# You're now a baseball game point recorder.

# Given a list of strings, each string can be one of the 4 following types:

# Integer (one round's score): Directly represents the number of points you get in this round.
# "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
# "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
# "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
# Each round's operation is permanent and could have an impact on the round before and the round after.

# You need to return the sum of the points you could get in all the rounds.


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        def isInt(stringOp):
            try:
                int(stringOp)
                return True
            except ValueError:
                return False
        
        sumStack = []
        for op in ops:
                if isInt(op):
                    sumStack.append(int(op))
                elif op == "+":
                    try:
                        sumStack.append(sumStack[-1] + sumStack[-2])
                    except IndexError:
                        continue
                elif op == "D":
                    sumStack.append(2 * sumStack[-1])
                elif op == "C":
                    sumStack.pop()
        return sum(sumStack)
