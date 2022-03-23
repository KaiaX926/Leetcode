# class Solution:
#     def countPrimes(self, n: int) -> int:
#         none = []
#         for i in range(2,round(n/2)+2):
#             for j in range(i,round(n/2)+2):
#                 if i*j not in none and i*j < n:
#                     none.append(i*j)
#         print(none)
#         return len(list(set(list(range(1,n))) - set([1]+none))) #+ len(range(1,min(3,n)))

class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [0, 0] + [1] * (n - 2)
        for i in range(2,int(sqrt(n)+1)):
            if nums[i]==1:
                for j in range(i*i,n,i):
                    nums[j]=0
        return sum(nums)
