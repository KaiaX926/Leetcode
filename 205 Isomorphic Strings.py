class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # def decompose(x):
        #     temp = {}
        #     for i in x:
        #         if i not in temp:
        #             temp[i] = 1
        #         else:
        #             temp[i] += 1
        #     ans = list(temp.values())
        #     ans.sort()
        #     return ans
        
        def decompose(x):
            temp = {}
            for i in range(len(x)):
                if x[i] not in temp:
                    temp[x[i]] = [i]
                else:
                    temp[x[i]].append(i)
            ans = list(temp.values())
            return ans
        
        return decompose(s) == decompose(t)
        
        
        
