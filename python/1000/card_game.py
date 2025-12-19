# problem : https://codeforces.com/problemset/problem/1999/B
# brute force by testing both possibilties: if one possbility can occur the reverse possibility can occur aswell so + 2

for t in range(int(input())):
    cards = list(map(int, input().split(" ")))

    a_1 = cards[0]
    a_2 = cards[1]
    b_1 = cards[2]
    b_2 = cards[3]

    total = 0

    if (a_1 > b_1 and a_2 > b_2):
        total += 2
    
    if (a_1 > b_2 and a_2 > b_1):
        total += 2

    print(total)