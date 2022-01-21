class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        p1,p2,right = m-1,n-1,m+n-1

        while right >= 0 and p1 >= 0 and p2 >= 0 and nums1[right] == 0:
            if nums1[p1] >= nums2[p2]:
                nums1[right],nums1[p1] = nums1[p1],0
                p1 -= 1
                right -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[right] = nums2[p2]
                p2 -= 1
                right -= 1
            print(nums1)
            print(p1,p2,right)
        
        if p2 >= 0:
            print(p2)
            nums1[right - p2:right+1] = nums2[:p2+1]
        
        return nums1    
                    
