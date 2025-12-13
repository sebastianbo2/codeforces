# problem : https://codeforces.com/problemset/problem/1913/B

for t in range(int(input())):

    s = input()

    ones = 0
    zeros = 0

    best = 0

    for d in range(len(s)):

        if (s[d] == "1"):
            ones += 1
        else:
            zeros += 1

    # if they are equal, we know that we can mismatch every index
    if (zeros == ones):
        print(0)
        continue
        
    for m in range(len(s)):
        if (zeros == 0 or ones == 0):
            best = ones + zeros
        
        if (s[m] == "1"):
            zeros -= 1
        else:
            ones -= 1

    print(best)