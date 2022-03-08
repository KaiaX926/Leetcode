class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        for i in range(min(len(v1),len(v2))):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        
        if len(v1)>len(v2) and any(int(i) != 0 for i in v1[len(v2):]):
            return 1
        elif len(v1)<len(v2) and any(int(i) != 0 for i in v2[len(v1):]):
            return -1
        else:
            return 0
       
