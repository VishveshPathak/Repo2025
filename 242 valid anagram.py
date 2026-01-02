"""
Given two strings s and t, return true if t is an
of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
"""
#solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] = hashmap[s[i]]+1
            else:
                hashmap[s[i]] = 1
        for i in range(len(t)):
            if t[i] in hashmap:
                hashmap[t[i]] = hashmap[t[i]] -1
            else:
                return False
        for i in hashmap:
            if hashmap[i] != 0:
                return False
        return True