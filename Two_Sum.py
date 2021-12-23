""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""
#Brute Force
#Time Complexity: O(n**2)
#Space Complexity: O(n)
class Solution(object):
    def twosum_naive(nums,target):
        n = len(nums) - 1
        for i in range (0, n):
            for j in range (i, n):
                if nums[i] + nums[j] == target:
                    return i,j
        return None
    num = [1, 3, 6, 7, 9]
    targets = 9
    n = len(num)
    print( twosum_naive(num, targets))

    # Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    class Solution(object):
        def twosum_twopointers(nums, target):
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    return left, right
            return None

        numbers = [1, 3, 6, 7, 9]
        target1 = 9
        n = len(numbers)
        print(twosum_twopointers(numbers, target1))
#HASHMAP
#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution(object):
    def twosum_hashmap(nums, target):
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return [i, hash_map[nums[i]]]
            else:
                hash_map[target - nums[i]] = i
    num = [ 1, 2, 4, 3, 6, 7]
    k = 6
    n = len(arr)
    print("The numbers that add up to 6 are at index" , twosum_hashmap(num, k))
