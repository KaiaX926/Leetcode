class Solution:
    def grayCode(self, n):
        return ((x>>1)^x for x in range(1<<n))
    
# ^	XOR	Sets each bit to 1 if only one of two bits is 1



#--------------------------------------------------------
def grayCode(n):
    ini = '0' * n
    ans,res = [],[ini]
    head = len(ini) - 1
    while head >= 0:
        print('when head = %s' %head)
        lead = len(ini) - 1
        ini = ini[:head] + '1' + ini[head+1:]
        res.append(ini)
        print('ini:',ini)
        fliprest(ini,head,lead,res)
        print('current res:',res)
        ini = res[-1]
        head -= 1

    for item in res:
        ans.append(int(item,2))
    return ans
        
def fliprest(ini,head,lead,res):
    print('head vs lead', head, lead)
    
    loc = len(ini) - 1
    
    
    while loc > lead:
            print('head vs lead vs loc', head, lead, loc)
        
            if ini[loc] == '0':
                ini = ini[:loc] + '1' + ini[loc+1:]
            else:
                ini = ini[:loc] + '0' + ini[loc+1:]
            res.append(ini)
            loc -= 1
            
    print('END!!! head vs lead vs loc', head, lead, loc)
    if lead > head:
        if ini[lead] == '0':
            ini = ini[:lead] + '1' + ini[lead+1:]
        else:
            ini = ini[:lead] + '0' + ini[lead+1:]
        print(ini)
        res.append(ini) 
    
    lead -= 1   
    if lead > head:
        fliprest(ini,head,lead,res)

    return res
    
