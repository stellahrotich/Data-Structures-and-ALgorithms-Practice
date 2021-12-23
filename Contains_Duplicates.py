class Solution(object):
    """Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct."""
    # O(n) time and O(n) space
    def contains_duplicates(self, nums):
        res = {}
        for n in nums[1:]:
            if n in res:
                return True
            else:
                res[n] = 1
        return False
    
#O(n) time and O(n) space
class solution(object):
    def contains_duplicates2(self, nums):
        return len(set(nums)) != len(sum(nums))

#O(n) time and O(n log n)  space
class Solution(object):
    def contains_duplicates3(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return False
            return True
#Time: O(n); Space: O(n)
class Solution:
    def containsDuplicate(self, nums):
        count = {}
        for i in nums:
            if i in count:
                return True
            count[i] = 1
        return False
