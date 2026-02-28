# problem : https://codeforces.com/problemset/problem/2193/C

# Since there is an unlimited amount of operations we can apply, we can always maximize a value at an index i based on the highest value above it (in either array)
# We keep track of the highest number to the right at every position and construct an array of this
# Then, we build an array of sums so that we can do the "integral"/sum trick xd (sum[b] - sum[a] gives sum from a to b)

for t in range(int(input())):
    n, q = map(int, input().split(" "))
    anums = list(map(int, input().split(" ")))
    bnums = list(map(int, input().split(" ")))

    vals = [0] * n

    for i in range(n):
        vals[n - i - 1] = max(vals[n - i] if i != 0 else 0, max(anums[n - i - 1], bnums[n - i - 1]))
    
    ans = [0] * n

    for b in range(n):
        ans[b] = (ans[b - 1] if b != 0 else 0) + vals[b]

    for ques in range(q):

        l, r = map(int, input().split(" "))

        mo = ans[r - 1] - (ans[l - 2] if l - 2 >= 0 else 0)

        print(mo, end=" ")