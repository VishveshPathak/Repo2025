"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
"""

#solution:
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        str1 = []
        if numRows == 1:
            return s
        for i in range(numRows):
            str1.append('')
        index = 0
        arraycounter = 0
        flag = True
        while index<len(s):
            str1[arraycounter] = str1[arraycounter] + s[index]
            if arraycounter == numRows-1:
                flag = False
            elif arraycounter == 0:
                flag = True
            if flag == True:
                arraycounter = arraycounter + 1
            else:
                arraycounter = arraycounter - 1
            index = index+1
        answer = ''
        for i in range(len(str1)):
            answer = answer + str1[i]
        return answer