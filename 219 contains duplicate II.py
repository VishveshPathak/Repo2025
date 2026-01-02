"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
"""

#solution:

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]] = []
                hashmap[nums[i]].append(i)
        print(hashmap)
        for i in hashmap:
            if len(hashmap[i]) >= 2:
                for j in range(len(hashmap[i])):
                    for l in range(j+1, len(hashmap[i])):
                        if abs(hashmap[i][l]-hashmap[i][j])<=k:
                            return True
        return False
        