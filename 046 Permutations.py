# The core idea is to use DFS by changing the position of each pair of numbers in order. [DFS method goes as far as possible before backtracking]
# The first function is used to output the final result, and the second function is the main part of obtaining potential permutation.
# The thinking flow is that we try to change the order of the last several numbers. Treat the last several numbers as a new subset and recursively start the permutation step inside the new subset.
# For example, in the first step, we want to get a new list by changing the order of the last number. Of course, there is only one solution, so we add it directly to the output list.
# Then, in the second step, we try to get a new list by changing the order of the last two numbers. So we treat the last two numbers as a new set and try to find the permutations in the new set by using the same function, which will start from the last number in the new set again. Then add all the solutions to the final list.
# Recursively find the solution by adding one more number from the righthand until we have considered all positions in the list. 
# While the overall process starts from the righthand, the certain permutation method in each step begins from the lefthand by exchanging the number on the current place with each number after it.
# For example, in the third step, we want to change the order of the last three numbers. So we first treat it as a new subset.
# Then we first exchange the numbers on the first and second places in the set, then the first and third places.

class Solution(object):
    def permute(self, nums):
        # DPS with swapping
        res = []
        if len(nums) == 0:
            return res
        self.get_permute(res, nums, 0)
        return res

    def get_permute(self, res, nums, index):
        if index == len(nums):
            res.append(list(nums))
            return
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            # s(n) = 1 + s(n-1)
            self.get_permute(res, nums, index + 1)
            nums[i], nums[index] = nums[index], nums[i]
