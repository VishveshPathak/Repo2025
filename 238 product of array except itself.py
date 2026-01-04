"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

#solution:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                product = product * nums[i]
        zeros = nums.count(0)
        if zeros > 1:
            for i in range(len(nums)):
                nums[i] = 0
        elif zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
        else:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = int(product/nums[i])
        return nums