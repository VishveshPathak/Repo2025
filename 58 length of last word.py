"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
consisting of non-space characters only.
"""

#solution:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ''
        while s[-1] == ' ':
            s = s[:-1]
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                break
            word = s[i] + word
        return len(word)