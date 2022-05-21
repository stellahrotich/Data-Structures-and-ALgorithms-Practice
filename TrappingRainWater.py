#solution1
class Solution:
    def trap(self, height):
        start = 0
        end = len(height) - 1
        max_left = 0
        max_right = 0
        water = 0
        while start < end: 
            max_left = max(max_left, height[start]) #0, 1 -> 1
            max_right = max(max_right, height[end]) #
            if height[start] <= height[end]:
                water += max_left - height[start]
                start += 1    
            else:
                water+= max_right - height[end]
                end -= 1
        return water
      
#solution2
class Solution:
    def trap(self, height): 
        if not height: return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
