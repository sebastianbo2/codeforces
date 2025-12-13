# IDEA: count how many steps (operations 1 + 2) to type before any swaps
# We can at most only optimize by reducing by 2 steps (the edges of the chosen substring)
# To count swaps properly, we must account for the first character possibly being 1 (and therefore needing to use operation 2)
# If there are two swaps, it must be from 0 to 1 and 1 to 0 so we can arrange such that the starting character either goes from 1 to 0 or we prevent going from 1 to 0 back to 1
# If there are more than two swaps, we take away two (the edges of the chosen substring when reverse)

for t in range(int(input())):

    length = int(input())

    s = input()

    swaps = -1

    l, r = 0, 0

    while (r < len(s)):

        swaps += 1

        while (r < len(s) and s[l] == s[r]):
            r += 1
        
        l = r

    if (s[0] == "1"):
        swaps += 1

    if (swaps == 2):
        length -= 1
    elif (swaps > 2):
        length -= 2

    print(length + swaps)