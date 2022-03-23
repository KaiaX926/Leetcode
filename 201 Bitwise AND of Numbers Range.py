# class Solution:
#     def rangeBitwiseAnd(self, left: int, right: int) -> int:
#         if right - left < 1:
#             return 0
        
#         res = int(bin(left)[2:])
#         for num in range(left,right+1):
#             res = res & int(bin(num)[2:])
        
#         return int(str(res),2)

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left, right = bin(left)[2:], bin(right)[2:]
        if len(left) != len(right): return 0
        
        num = 0
        for i in range(len(left)):
            if left[i] == right[i] == '1':
                num += pow(2, len(left)-i-1)
            elif left[i] != right[i]:
                break
        
        return num
