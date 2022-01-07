# The core idea is to fix two of the four numbers and check whether the rest of the list contains the numbers that are equal to the target minus the first two numbers.
# The first two numbers can be any combination of the numbers in the list. And the key point of updating the pointer of the rest two numbers is to sort the list at first.


class Solution(object):
    def fourSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        r = []
        
        for i in range(len(nums) - 3):
            for j in range(i+1,len(nums) - 2):
                #print(i,j)
                rest = nums[j+1:]
                left,right = 0,len(rest) - 1
                while left < right:
                    #print(left,right)
                    s = nums[i] + nums[j] + rest[left] + rest[right]
                    add = [nums[i], nums[j], rest[left], rest[right]]
                    if s == target:
                        if add not in r:
                            r.append(add)
                        right -= 1
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        left += 1
        return r
