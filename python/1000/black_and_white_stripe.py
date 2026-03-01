# problem : https://codeforces.com/problemset/problem/1690/D

# IDEA : this is a sliding window problem, where the window is of length k
# start with the first position, and compute the amount of whites in the interval of 0, k
# everytime you "slide" right by 1, decrease the count of whites by 1 if your left edge was a white and is not gone
# increase the count of whites by 1 if your right edge has a white after incrementing
# record the minimum count of whites in an interval of length k and that is our answer

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
