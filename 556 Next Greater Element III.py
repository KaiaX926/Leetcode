# Start from the end and look for increasing pattern, it our case 7641.
# If it happen, that all number has increasing pattern, there is no bigger number with the same digits, so we can return -1.
# Now, we need to find the first digit in our ending, which is less or equal to digits[i-1]: 
# we have ending 5 7641 and we are looking for the next number with the same digits. 
# What can go instead of 5: it is 6! Let us change these two digits, so we have 6 7541 now. 
# Finally, we need to reverse last ditits to get 6 1457 as our ending.


class Solution:
    def rotate(self, l):
        p = len(l) - 1
        while p > 0:
            if l[p] > l[0]:
                return [l[p]] + sorted(l[1:p] + [l[0]] + l[p+1:])
            else:
                p -= 1
        return -1

    def nextGreaterElement(self, n: int) -> int:
        x = [int(i) for i in str(n)]
        if len(x) < 2:
            return -1
        loc = len(x) - 2
        while loc >= 0:
            if x[loc] < x[loc+1]:
                y = self.rotate(x[loc:])
                if y != -1:
                    ans = int(''.join(str(num) for num in x[:loc] + y))
                    if ans < 2**31 :
                        return ans
                return  -1
            else:
                loc -= 1
        return -1
