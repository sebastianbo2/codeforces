for t in range(int(input())):

    n, k = map(int, input().split(" "))
    s = input()

    c = 0

    for g in range(k):
        if s[g] == "W":
            c += 1
    
    l, r = 0, k - 1

    best = c

    while (r < n - 1):
        r += 1

        if s[r] == "W":
            c += 1
        
        if s[l] == "W":
            c -= 1
        
        l += 1

        best = min(best, c)

    print(best)
