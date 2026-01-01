"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
"""

#solution:

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for i in range(len(magazine)):
            if magazine[i] in hashmap:
                hashmap[magazine[i]] = hashmap[magazine[i]] + 1
            else:
                hashmap[magazine[i]] = 1

        for i in range(len(ransomNote)):
            if ransomNote[i] in hashmap:
                hashmap[ransomNote[i]] = hashmap[ransomNote[i]] - 1
                if hashmap[ransomNote[i]] < 0:
                    return False
            else:
                return False
        return True