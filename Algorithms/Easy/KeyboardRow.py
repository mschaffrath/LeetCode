# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard
# USE typical QWERTY layout

# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        ans = []
        for word in words:
            wordL = word.lower()
            wordSet = set(wordL)
            if row1 & wordSet == wordSet:
                ans.append(word)
            if row2 & wordSet == wordSet:
                ans.append(word)
            if row3 & wordSet == wordSet:
                ans.append(word)
        return ans
            
