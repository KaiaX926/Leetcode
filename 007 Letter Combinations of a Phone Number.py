dmap = {'2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' ',
        None: None}

i = 0

def letterCombinations(i,digits):
        # DFS
        result = []
        ls = len(digits)
        if ls == 0:
            return result
        current = digits[0]
        posfix = letterCombinations(i,digits[1:])
        print('pos: ',i,posfix)
        for t in dmap[current]:
            print(''*5,t)
            if len(posfix) > 0:
                for p in posfix:
                    temp = t + p
                    result.append(temp)
            else:
                result.append(t)
        i += 1
        print('res: ',i,result)
        return result
     
     
#------------------------------------------------------------------------
# Understandnig of the process
 letterCombinations(i,digits)
     current = digits[0] #'2'
     posfix = letterCombinations(i,digits[1:])#0 '34'
     current = digits[0] #'3'
           posfix = letterCombinations(i,digits[1:])#0 '4'
           current = digits[0] #'4'
                posfix = letterCombinations(i,digits[1:])#0 ''
                 ls == 0 : 
                 return result#[]  posfix_temp = []
            print('pos: ',i,posfix) # 0 []
            dmap[current] #'4'
            i += 1 # 1
            print('res: ',i,result) # 1 ['g', 'h', 'i']
      print('pos: ',i,posfix) # 0 ['g', 'h', 'i']
      dmap[current] #'3'
      i += 1 # 1 
      print('res: ',i,result) # 1 ['dg', 'dh', 'di', 'eg', 'eh', 'ei', 'fg', 'fh', 'fi']
  print('pos: ',i,posfix) # 1 ['dg', 'dh', 'di', 'eg', 'eh', 'ei', 'fg', 'fh', 'fi']
  dmap[current] #'2'
  i += 1 # 1 
  print('res: ',i,result) # 1 ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
