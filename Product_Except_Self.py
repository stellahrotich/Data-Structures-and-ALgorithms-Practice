"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation."""
# O(n) Time & O(1) Space
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefixProduct = [None] * n
        prefixProduct[0] = 1
        for i in range(1, n):
            prefixProduct[i] = nums[i - 1] * prefixProduct[i - 1]
        postfixProduct = nums[-1]
        for i in range(n - 2, -1, -1):
            prefixProduct[i] *= postfixProduct
            postfixProduct *= nums[i]
        return prefixProduct
