# IDEA: We want to find the amount of drinks we can buy that are less than or equal to our available money (on that day)
# Binary search: Sort the array and find the maximum before the condition changes : based on (T, T, T, F, F) binary search
# return left because it is the bound where the condition changes

length = int(input())

nums = list(map(int, input().split(" ")))
nums.sort()

for q in range(int(input())):
    m = int(input())

    l, r = 0, length - 1

    mid = 0

    ctr = 0

    while (l <= r):
        mid = l + (r - l) // 2

        if nums[mid] <= m :
            l = mid + 1
        elif nums[mid] > m:
            r = mid - 1

        ctr += 1
    
    print(l)