# problem : https://codeforces.com/contest/1476/problem/A

# IDEA : we first need to find a possible value to be taken by the sum that is divisible by k, which is the smallest multiple of k that is bigger than n
# then, we know that every value in the array will be at least p, where p is k / n
# but we need them to be integers, so we roof it to get the maximum minimum value (some values will be k // n and some will be ceil(k /n))
# ex: for 9 expressed as 4 numbers, we have 2, 2, 2, 3, 9 / 4 = 2.25, which ceiled gives us 3

import math

for t in range(int(input())):

    n, k = map(int, input().split(" "))

    k *= math.ceil(n / k)

    print(math.ceil(k / n))