# The core idea is to divide the list into two parts, left and right. Pick the largest number in each part, calculate the distance and minimum among two numbers, and update the container if the new result is larger.
# The key step here is to remove the smaller number among two picked numbers to decrease the running time.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            result = max(min(height[left], height[right]) * (right - left), result)
            if height[left] > height[right]:
                # remove right
                right -= 1
            else:
                # remove left
                left += 1
        return result
