#| operate | bit value | octal value |                       description                        |
#| ------- | --------- | ----------- | -------------------------------------------------------- |
#|         | 00000100  |           4 |                                                          |
#| 4 << 2  | 00010000  |          16 | move all bits to left 2 bits, filled with 0 at the right |
#| 16 >> 2 | 00000100  |           4 | move all bits to right 2 bits, filled with 0 at the left |

class Solution:
    def lastRemaining(self, n: int) -> int:
        ans = 1
        k, cnt, step = 0, n, 1
        while cnt > 1:
            if k % 2 == 0:
                ans += step
            else:
                if cnt % 2:
                    ans += step
            k += 1
            cnt >>= 1
            step <<= 1
            
        return ans
