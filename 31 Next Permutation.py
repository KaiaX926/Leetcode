# The core idea is to find the number on the smallest place which is larger than the number one place less than it. The smaller place to be changed, the smaller the new number will be.
# This is the number that will be changed into a larger number. Also, the list of numbers on its right is in descending order.
# Still start from the right side, the first number that is larger than the current number is the smallest number that is larger than it.
# Switch those two numbers and change the number on the places that are smaller than the current place into ascending order. 

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 2, -2, -1):
            if i == -1 : return nums.reverse()
            if nums[i] < nums[i + 1]: break
        for j in range(n - 1, i, -1):
            if nums[j] > nums[i]: break
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1: ] = reversed(nums[i+1: ])
