import math

for t in range(int(input())):

    n, k = map(int, input().split(" "))

    k *= math.ceil(n / k)

    print(math.ceil(k / n))