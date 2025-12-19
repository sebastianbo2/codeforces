# problem : https://codeforces.com/contest/2180/problem/A

for t in range(int(input())):

    inp = input().split(" ")

    l = int(inp[0])
    a = int(inp[1])
    b = int(inp[2])

    best = a

    ctr = (a + b) % l
    
    while (ctr != a):
        if (ctr > best):
            best = ctr
        
        ctr = (ctr + b) % l
    
    print(best)