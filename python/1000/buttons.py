# problem : https://codeforces.com/problemset/problem/268/B

# IDEA : take all attempts of length 1 as an example: in the worst case, you will do n attempts and your nth attempt you will find the button that clicks
# so, you add n - 1 attempts that you "waste", and then you do n - 1 - (i) attempts of length (i + 1), where i is your current length of attempts
# this goes from 1 to n (n included)

n = int(input())

sum = 0

for i in range(n):
    sum += (n - i - 1) * (i + 1)

sum += n

print(sum)