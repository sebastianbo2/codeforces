# problem : https://codeforces.com/problemset/problem/2167/C

for i in range(int(input())):
    input()
    nums = list(map(int, input().split(" ")))

    odd_flag = False
    even_flag = False

    for d in range(len(nums)):
        if (nums[d] % 2 == 1):
            odd_flag = True
        elif (nums[d] % 2 == 0):
            even_flag = True

        if odd_flag and even_flag:
            break

    if odd_flag and even_flag:
        nums.sort()

    for p in range(len(nums)):
        print(nums[p], end=" ")
    
    print()