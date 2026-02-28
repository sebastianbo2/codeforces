# problem : https://codeforces.com/contest/2091/problem/B

# sort the array and start from the top : we can eliminate every number above the threshold as a solo group and
# once we hit small numbers we keep going till a group is filled and save that and keep going until no more valid groups can be made

for t in range(int(input())):

    n, x = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))

    nums.sort()

    sum = 0

    ctr = n - 1

    while (ctr >= 0):
        if (nums[ctr] >= x):
            sum += 1
            ctr -= 1
        else:
            strength = nums[ctr]
            amount = 0

            while (strength * amount < x and ctr >= 0):
                amount += 1
                
                if (nums[ctr] < strength):
                    strength = nums[ctr]

                ctr -= 1

            if (strength * amount >= x):
                sum += 1
    
    print(sum)