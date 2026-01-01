"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""
#solution:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m>n:
            return -1
        for i in range(0, n):
            if haystack[i] == needle[0]:
                found = True
                if i+m > n:
                    return -1
                else:
                    for j in range(m):
                        if haystack[i+j] != needle[j]:
                            found = False
                            break
                    if found == True:
                        return i
        return -1
        