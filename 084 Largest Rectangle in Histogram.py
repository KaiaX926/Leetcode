class Solution(object):
    def largestRectangleArea(self,heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        start = [0]
        area = heights[0]#[heights[0]]
        for i in range(1,len(heights)):
            if heights[i] > heights[i-1]:
                start.append(i)
                area = max(area,heights[i])
                #area.append(heights[i])
            for loc in start:
                a = (i - loc + 1)*min(heights[loc:i+1])
                area = max(area,a)
                #area.append(a)
        
        return area #max(area)




# --------------------------------------------------------
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ma = heights[0]
        for i in range(len(heights)):
            r = self.checkeach(heights,i)
            ma = max(r,ma)
        
        return ma
            
        
    def checkeach(self,heights,i):
        ma = heights[i]
        for j in range(i,len(heights)):
            h = min(heights[i:j+1])
            area = h * (j-i+1)
            ma = max( area , ma)
        return ma
