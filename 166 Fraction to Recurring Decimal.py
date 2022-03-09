class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:
        ans = []
        
        if (num >= 0 and den >= 0) or (num <= 0 and den <= 0):
            sign = True
        else:
            sign = False
        
        num = abs(num)
        den = abs(den)
        
        q = num // den
        r = num % den
        
        ans.append(q)

        if r == 0:
            return "".join(map(str, ans)) if sign else "-" + "".join(map(str, ans))
        else:
            ans.append(".")
            map1 = {}
            while r != 0:
                if r in map1:
                    ans.insert(map1[r], "(")
                    ans.append(")")
                    break
                else:
                    map1[r] = len(ans)
                    r *= 10
                    q = r // den
                    r %= den
                    ans.append(q)
        
        
        return "".join(map(str, ans)) if sign else "-" + "".join(map(str, ans))
