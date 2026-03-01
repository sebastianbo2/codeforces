for t in range(int(input())):
    
    n, k, q = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))

    sum = 0
    before = 0

    for i in range(n):
        if nums[i] <= q:
            before += 1
        else:
            if before >= k:
                sum += (before - k + 1) * (before - k + 2) // 2
            before = 0
    
    if before >= k:
        sum += (before - k + 1) * (before - k + 2) // 2

    print(sum)
