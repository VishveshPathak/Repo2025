"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n."""

#solution: 
class Solution:
    def add_element(self, nums, ins):
        for i in range(len(nums)):          #run through the array until inserted element < nums[i] 
            if nums[i] > ins:
                x = len(nums)-1
                while x>i:                  #start from back of the array and shift all elements right until x = i
                    nums[x] = nums[x-1]
                    x = x-1
                nums[i] = ins
                break
        return nums
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count = 0
        while count < n:                        #if nums2 is empty, return nums1
            if nums1[m-1]<=nums2[count]:        #if nums2[count] > max element of nums1, increase size on nums1 by 1 and append at that position
                nums1[m] = nums2[count]
            else:                               #else insert at correct position and shift entire array right till the position
                nums1 = self.add_element(nums1, nums2[count])
            m = m+1
            count = count+1

            