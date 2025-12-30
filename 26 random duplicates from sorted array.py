#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
#Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
#The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
# solution 1: linear
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        x = 0
        if len(nums) > 1:                             # check if first element is repeated
            while x < len(nums)-1:
                if nums[x] != nums[x+1]:              # if different element found, add first element to k and end loop
                    nums[k] = nums[x]
                    k = k+1
                    break
                else:
                    nums[k] = nums[x]
                x = x+1
            if k == 0:                                 # corner case management when only 2 elements are present in array
                k = k+1
            x = 0
            while x<len(nums)-1 and k>0:               # if atleast 1 unique element in nums, add every occurrence of unique element at kth position in array
                if nums[x] != nums[x+1]:
                    nums[k] = nums[x+1]
                    k = k+1                            # update k only when unique element is found
                x = x+1
            return k
        else:
            return 1                                   # corner case management only 1 element is present in array

#solution 2: hashmap

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
            x = x+1 
        return k                                            #return first k elements of array