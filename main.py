n, a, b = map(int, input().split(" "))

print(b + 1 if b + 1 <= n - a else n - a)