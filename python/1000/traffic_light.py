# problem : https://codeforces.com/problemset/problem/1744/C

# IDEA : we build an array of distances for every point, starting from the right of the array (since you are trying to move right)
# we also need to keep track of the last green in the array (the first green spotted when starting from the right),
# since every point after it needs the distance from 0 added to it (since it has to loop through the array a second time for sure)

for t in range(int(input())):
    n, c = map(str, input().split(" "))
    n = int(n)
    s = input()
    
    distance = [0] * n
    
    green = -1
    
    last = 0
    
    for i in range(n):
        if s[n - i - 1] == "g":
            if green == -1:
                green = n - i - 1
            last = 0
        else:
            last += 1
            
        distance[n - i - 1] = last
    
    best = float('-inf')
    
    for j in range(n):
        if s[j] == c:
            best = max(best, distance[j] + (distance[0] if j > green else 0))
    
    print(best)
            