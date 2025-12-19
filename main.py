# problem : https://codeforces.com/contest/2180/problem/A

for t in range(int(input())):

    inp = input().split(" ")

    l = int(inp[0])
    a = int(inp[1])
    b = int(inp[2])

    a_odd = a % 2 == 1
    b_odd = b % 2 == 1

    if (l - 1 % 2 == 0):
        if not (a_odd and b_odd):
            print(l - 1)
        else:
            print(l - 2)
    else:
        if a_odd or b_odd:
            print(l - 1)
        else:
            print(l - 2)
    