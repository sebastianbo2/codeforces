# problem : https://codeforces.com/problemset/problem/1791/D

# IDEA : "sliding window" the bounds of set1 and set2 (two dictionarries with counts of each character)
# the best answer is the maximized sums of unique characters in set1 and set2 

for t in range(int(input())):

    n = int(input())
    s = input()

    s1 = dict()
    s2 = dict()

    s1_uniques = 0
    s2_uniques = 0

    for mo in range(n):
        if s[mo] not in s1:
            s1[s[mo]] = 0
            s1_uniques += 1

        s1[s[mo]] += 1
    
    best = s1_uniques

    for i in range(n):
        s1[s[i]] -= 1

        if s1[s[i]] <= 0:
            s1_uniques -= 1
        
        if s[i] not in s2:
            s2[s[i]] = 0
            s2_uniques += 1
        
        s2[s[i]] += 1
        
        best = max(best, s1_uniques + s2_uniques)
    
    print(best)