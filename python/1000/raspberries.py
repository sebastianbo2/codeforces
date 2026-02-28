# problem : https://codeforces.com/problemset/problem/1883/C

# all possible k values exept for 4 are primes so we just note the small different from it and thats out answer
# for 4, we either need 0 operations (one number is divisible by 4 so the product is too), 1 operation (one number is 1 away from being divisible by 4),
# or 2 (2 odd numbers increase by 1 making them even, so the product divides 2 twice meaning that it divides 4)
# my solution is unfortunately far from being the best for this problem since it has alot of ifs, however its what i thought of initially and it works so its not that bad

import math

for t in range(int(input())):

    n, k = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))

    if k != 4:
        best = float('inf')
        for i in range(n):

            best = min(best, k * math.ceil(nums[i] / k) - nums[i])

        print(best)
    else:
        even_count = 0
        flag = False

        for i in range(n):
            if nums[i] % 4 == 0:
                even_count += 2
                break

            if (nums[i] + 1) % 4 == 0:
                flag = True

            if nums[i] % 2 == 0:
                even_count += 1

        if not flag:
            print(2 - min(2, even_count))
        else:
            if even_count >= 2:
                print(0)
            else:
                print(1)