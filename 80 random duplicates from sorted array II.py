#Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
#Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
#Return k after placing the final result in the first k slots of nums.
#Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

#solution:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}
        k = 0
        x = 0
        while x<len(nums):
            if not nums[x] in hashmap:
                nums[k] = nums[x]                           #update kth position of array with current element
                k = k+1                                     #update k only when new element found
                hashmap[nums[x]] = 1                        #update hashmap with new value
            elif int(hashmap[nums[x]]) < 2:                 #update k+1th position if hashmap already contains number once
                nums[k] = nums[x]                           
                k = k+1
                hashmap[nums[x]] = int(hashmap[nums[x]])+1  #make count = 2
            #else:
            #do nothing
            x = x+1 
        return k                                            #return first k elements of array