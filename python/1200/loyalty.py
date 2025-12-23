# idea sort and buy bad items till next buy increases when buying best so buy best for most points
# problem : https://codeforces.com/problemset/problem/2161/C

for t in range(int(input())):

    line1 = input().split(" ")
    n, X = int(line1[0]), int(line1[1])

    nums = list(map(int, input().split(" ")))
    nums.sort()

    l, r = 0, len(nums) - 1

    bought = []

    total = 0
    points = 0

    while (l <= r):
        if ((total + nums[r]) // X > total // X):
            total += nums[r]
            bought.append(nums[r])
            points += nums[r]
            r -= 1
        else:
            total += nums[l]
            bought.append(nums[l])
            l += 1
    
    print(points)

    for d in range(len(bought) - 1):
        print(bought[d], end=" ")

    print(bought[len(bought) - 1])
