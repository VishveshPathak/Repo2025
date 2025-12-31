#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#solution:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        swap1 = 0
        n = len(nums)
        nums2 = []
        for i in range(n):
            nums2.append(0)
        for i in range(n):
            nums2[(i+k)%n] = nums[i]
        for i in range(n):
            nums[i] = nums2[i]