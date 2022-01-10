# The core idea is to obtain the letter usages condition of each word and check whether there are other words that use the same letters.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res, res_dic = [],[]
        
        for item in strs:
            dic = {}
            for letter in item:
                if letter not in dic:
                    dic[letter] = 1
                else:
                    dic[letter] += 1
            if dic not in res_dic:
                res.append([item])
                res_dic.append(dic)
            else:
                loc = res_dic.index(dic)
                res[loc].append(item)
        
        return res
        
