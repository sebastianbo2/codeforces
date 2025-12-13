# problem : https://codeforces.com/problemset/problem/174/A

inp = input().split(" ")

n, b = int(inp[0]), int(inp[1])

nums = list(map(int, input().split(" ")))

sum = 0

for m in range(len(nums)):
    sum += nums[m]

sum /= n

split = b / n

flag = False

for i in range(len(nums)):
    prev = nums[i]

    nums[i] = sum + split - nums[i]

    if (nums[i] < 0):
        flag = True
        break

if (flag):
    print(-1)
else:
    for d in range(len(nums)):
        print(f"{nums[d]:.6f}")