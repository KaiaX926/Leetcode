class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(set(nums))==1 and nums[0]==0: return "0"
        def r(a,b):
            if a+b<b+a:
                return 0
            if a+b>b+a:
                return 1
        num=[str(i) for i in nums]
        for i in range(len(num)):
            for j  in range(i+1):
                if r(num[j],num[i])==0:
                    num[j],num[i]=num[i],num[j]
        return "".join(num)
