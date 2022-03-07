class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        self.res,temp = [],[]
        
        def new(num,temp):
            temp = [i*num for i in temp]
            temp.append(num)
            self.res += temp
            return temp
        
        for num in nums:
            temp = new(num,temp)
            
        print(self.res) 
        return max(self.res)
        
  
#------------------------------------
# There are three conditions to get the updated MAXIMUM: old maximum * new number (positive * positive), old minmum * new number (negative * negative), new number
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        #We need to keep track of both the current Minimum product and current Maximum product because we can possibily
        #Have negative numbers in our nums array
        currMin, currMax = 1, 1
        
        #globalMax will represent a global maximum value
        globalMax = max(nums)
        
        for n in nums:
            
            #We need to keep a copy of currMax when we calculate currMin
            oldcurrMax = currMax
            
            #currMax product will either be currMax * current number we're on
            #currMin * current number we're on because it could be negative, and just the current number
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(oldcurrMax * n, currMin * n, n)
            print(currMax, currMin)
            globalMax = max(globalMax, currMax)
            
        return globalMax
