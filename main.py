n, m = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))

left = n

i = 0

while (left > 1):

    if nums[i] <= 0:
        i = (i + 1) % n
        continue

    nums[i] -= m
    
    if nums[i] <= 0:
        left -= 1

    i = (i + 1) % n
        

for g in range(n):
    if nums[g] > 0:
        print(g + 1)
        break