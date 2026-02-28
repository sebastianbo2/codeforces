# problem : https://codeforces.com/problemset/problem/706/C

# At every index in the list of strings you can choose to either reverse them or not reverse them
# Choosing to reverse costs energy and choosing not to doesn't cost anything. However, we must keep the array valid
# So, if our choice leads to an invalid array we must set the value at a maximum (so that when choosing the best this will be removed as soon as possible)
# If all values are the max value, there is no possible configuration which means we must output -1
# At each index we choose the best answer: minimum (we must check if every possibility is valid in order to remove the invalid ones)

n = int(input())

nums = list(map(int, input().split(" ")))

max = pow(10, 15)

strings = [[""] * n, [""] * n]

ans = [[max] * n, [max] * n]

for i in range(0, n):
    strings[0][i] = input()
    strings[1][i] = strings[0][i][::-1]

    if (i == 0):
        # set base params
        ans[0][i] = 0
        ans[1][i] = nums[i]
    else:
        if (strings[0][i] >= strings[0][i - 1] and strings[0][i] >= strings[1][i - 1]):
            ans[0][i] = min(ans[0][i - 1], ans[1][i - 1])
        else:
            if (strings[0][i] >= strings[0][i - 1]):
                ans[0][i] = ans[0][i - 1]
            elif (strings[0][i] >= strings[1][i - 1]):
                ans[0][i] = ans[1][i - 1]
            else:
                ans[0][i] = max


        if strings[1][i] >= strings[0][i - 1] and strings[1][i] >= strings[1][i - 1]:
            ans[1][i] = min(ans[0][i - 1], ans[1][i - 1]) + nums[i]
        else:
            if (strings[1][i] >= strings[0][i - 1]):
                ans[1][i] = ans[0][i - 1] + nums[i]
            elif (strings[1][i] >= strings[1][i - 1]):
                ans[1][i] = ans[1][i - 1] + nums[i]
            else:
                ans[1][i] = max

final = min(ans[0][n - 1], ans[1][n - 1])

print(final if final != max else -1)