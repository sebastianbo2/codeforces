m = input().split(" ")
i = int(m[1])

nums = list(map(int, input().split(" ")))

ctr = 0

prev = nums[0]

while (ctr < i and ctr < len(nums)):
    prev = nums[ctr]

    if (i - 1 == ctr + nums[ctr]):
        prev = 0
        ctr += nums[ctr]
        break

    ctr += nums[ctr]
    
print("YES" if ctr - prev == i - 1 else "NO")