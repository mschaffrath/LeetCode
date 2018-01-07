# Given an integer array with even length
# where different numbers in this array represent different kinds of candies.
# Each number means one candy of the corresponding kind.
# You need to distribute these candies equally in number to brother and sister.
# Return the maximum number of kinds of candies the sister could gain.

# NOTE:
# The length of the given array is in range [2, 10,000], and will be even.
# The number in given array is in range [-100,000, 100,000].


from collections import Counter
class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candyDict = Counter(candies)        #make a dict by counting instances
        inst = sum(candyDict.values()) / 2  #find how many to distribute to sis
        sis = 0                             #to count sis candy types
        for candy in candyDict:             #iter all candies in dict
            sis += 1                        #add a candy type given to sis
            candyDict[candy] -= 1           #remove 1 candy inst from the dict of current type
            inst -= 1                       #remove 1 inst from total candies to be given to sis
            if inst <= 0:                   #check if sis has all her candies
                break                           #if so, stop
        return sis                          #return types of candies sis has
    
        # fast solution:
        #a = len( set(candies) )
        #b = int( len(candies) / 2 )
        #return min(a, b)
