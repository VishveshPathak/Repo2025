"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

#solution: 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlength = 201
        for i in strs:
            if minlength>len(i):
                minlength = len(i)
        common = ''
        current = ''
        for i in range(minlength):
            current = strs[0][i]
            add = True
            for j in range(len(strs)):
                if current!=strs[j][i]:
                    add = False
                    break
            if add == True:
                common = common+current
            else:
                break
        return common