class Solution(object):
    def fullJustify(self,words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        import math

        x,y,i,w = 0,0,0,[]
        res = []
        while i < len(words):

            x += len(words[i])
            y += 1
            
            if x <= maxWidth - y + 1:
                w.append(words[i])
                i += 1
                continue
                
            else:
                r = ''
                if y != 2:
                    x -= len(words[i])
                    y -= 1
                    space = (maxWidth - x)//(y - 1)
                    e = (maxWidth - x)%(y - 1)
                    if e > 0:
                        space += 1

                    for j in range(len(w) - 2):
                        r += w[j] + ' '*int(space)
                    rest = maxWidth - x - ((y - 2)*space)
                    print(rest)
                    r += w[-2] + ' '*int(rest) + w[-1]
                    res.append(r)
                else:
                    space = maxWidth - x
                    r += w[0] + ' '*space
                    res.append(r)
                    
            
            x,y,w = 0,0,[]
            #i += 1
        
        print(w)
        
        if len(w) != 0:
            r = ''
            for j in range(len(w) - 1):
                r += w[j] + ' '
            r += w[-1] 
            r += ' '*int(maxWidth - len(r))
            res.append(r)
        
        return res
            
