# idea : compare both options of string constructions and take ideal
# problem : https://codeforces.com/contest/2180/problem/B

for t in range(int(input())):

    n = int(input())
    words = list(map(str, input().split(" ")))

    s = ""

    for i in range(n):
        if (s + words[i] < words[i] + s):
            s = s + words[i]
        else:
            s = words[i] + s

    print(s)