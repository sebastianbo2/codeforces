# problem : https://codeforces.com/problemset/problem/1840/C

# IDEA : this problem requires knowledge of triangle numbers, which is a way of counting the combinations in this problem ("ordered", not like a power set)
# https://www.mathsisfun.com/algebra/triangular-numbers.html Link to triangular numbers to find the formula n * (n+1) / 2
# you loop through the array counting how many indexes you've visited where the value has been "valid" (before or equal to q)
# everytime you encounter an invalid index (too high temp), you take the amount youve visited before and compute a triangular number
# for every triangular number you compute, you need to account for k (min days), so subtract that to get the amount of days that are above or equal to k (valid vacations)
# then, you need to add 1 because k's base value is 1 and not 0 (so it is offset by 1 and you need to readd it back after removing it)

for t in range(int(input())):
    
    n, k, q = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))

    sum = 0
    before = 0

    for i in range(n):
        if nums[i] <= q:
            before += 1
        else:
            if before >= k:
                sum += (before - k + 1) * (before - k + 2) // 2
            before = 0
    
    if before >= k:
        sum += (before - k + 1) * (before - k + 2) // 2

    print(sum)
