res = []
        i,t,r = 0,0,s
        
        if len(s) > 12:
            return res
        
        #step = 1 #len(s)//4

        def fetch(s,i,res,r,t):
            l = 1
            while i <= len(r) and t <= 3 and l <= min(3,len(s) - i + 1):
                if ((int(r[i:i+l]) == 0 and l == 1 ) or (r[i] != '0' and int(r[i:i+l]) > 0))and int(r[i:i+l]) <= 255:
                    r = r[:i+l] + '.' + r[i+l:]
                    t += 1
                    i += l+1 # i = i + l + 1
                    fetch(s,i,res,r,t)
                    i -= l+1
                    r = r[:i+l] + r[i+l+1:] #r = r[:i+l] + '.' + r[i+l:]
                    
                    t -= 1
                    l += 1
                else:
                    break 
                      
            if t == 3 and ((int(r[i:]) == 0 and len(r[i:]) == 1 )or (r[i] != '0' and int(r[i:]) > 0))and int(r[i:]) <= 255:
                if r not in res:
                    res.append(r)
            
            return
       
        fetch(s,i,res,r,t)
        return res
