# problem : https://codeforces.com/problemset/problem/124/A

# IDEA : if you do the first 2 examples youll see that the ACTUAL possible positions is n - a because the first a positions are taken for sure
# then the only number of possible spots is whats left, but only as long as the number of spots to the right is less than b + 1 (can be equal to b)
# as a rule of thumb, you can assume that there will always be b + 1 spots avaiable since b can go down to 0
# but if b + 1 is bigger than n - a you have to limit it to n - a

n, a, b = map(int, input().split(" "))

print(b + 1 if b + 1 <= n - a else n - a)