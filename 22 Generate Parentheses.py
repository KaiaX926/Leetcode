# The core idea is to use the DFS method to add '()' at every possible position. If it has not appeared before, then add it to the result.
# Only when there are n pairs of brackets in each string, the result list will be returned as the final result.
# Since we are using the DFS method, the loop will start from the root node, which in this problem, is when only put one pair of brackets in the string.
# There's only one result and it will be used as the basis when we consider adding one more pair of brackets.
# When we consider arranging more than one pair of brackets, we use each item as the basis (obtained in the loop before), and add one pair of brackets in each possible position once.
# In each new loop, the result list will be updated as none at the beginning.
# So each new string will be added to the result list in this layer if it has not appeared before. 
# Finally, when the layer number is equal to the expected number, the result will be output as the final result.


class Solution(object):
    

    def generateParenthesis(self,n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            print('first')
            l = ['()']
            return l
        
        profix = self.generateParenthesis(n - 1)
        l = []
        #print('profix:',profix,n)
        for item in profix:
            #print('item:', item)
            lon = len(item)
            for j in range(lon):
                add = item[:j] + '()' + item[j:]
                if add not in l:
                    l.append(add)
        return l
