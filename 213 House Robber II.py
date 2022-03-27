class Solution:
    def robHelper(self,nums,start,end):
        rob1,rob2 = 0,0
        for n in range(start,end):

            temp = max(nums[n]+rob1,rob2)

            rob1 = rob2 # do not rob last position
            rob2 = temp
            print(rob1,rob2)
            
        return rob2
    
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        money1 = self.robHelper(nums,1,len(nums))
        print('-'*10)
        money2 = self.robHelper(nums,0,len(nums)-1)
        
        return max(money1,money2)
        
