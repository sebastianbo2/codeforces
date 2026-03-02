# problem : https://codeforces.com/problemset/problem/450/A

# IDEA : u can just loop through and simulate the question to see which child is remaining
# keep removing m from every child until only 1 child is left and no matter how many he needs he will be the one left since it is a 1 length line
# go through the array one last time to find him if ur tracking how many have left the line

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