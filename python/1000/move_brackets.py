# problem : https://codeforces.com/problemset/problem/1374/C

for t in range(int(input())):

    length = int(input())
    s = input()

    need_front = 0
    need_end = 0

    for i in range(length):
        if (s[i] == "("):
            need_end += 1
        else:
            if (need_end > 0):
                need_end -= 1
            else:
                need_front += 1
    
    print(need_front)