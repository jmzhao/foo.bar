import math

def answer(n):
    ans = 0
    while n > 0 :
        a = int(math.sqrt(n))
        n -= a * a
        ans += 1
    return ans
