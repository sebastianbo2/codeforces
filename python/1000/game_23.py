# problem : https://codeforces.com/problemset/problem/1141/A

# IDEA: remove all factors of 2 and 3 from the numbers and if they are equal then it is doable
# also check if n has a higher factor of 2 or 3 cus then it would not be possible (only multiplication is done)

n, m = map(int, input().split(" "))

def getAnswer(n, m):

    ans = 0
    
    while n % 2 == 0 or m % 2 == 0:
        if n % 2 == 0 and m % 2 == 0:
            n /= 2
            m /= 2
        elif n % 2 == 0:
            return -1
        elif m % 2 == 0:
            m /= 2
            ans += 1
    
    while n % 3 == 0 or m % 3 == 0:
        if n % 3 == 0 and m % 3 == 0:
            n /= 3
            m /= 3
        elif n % 3 == 0:
            return -1
        elif m % 3 == 0:
            m /= 3
            ans += 1
    
    return ans if n == m else -1

print(getAnswer(n, m))