# IDEA: Since n can only be 12, 123, 1234 then the number of permutations are a limited amount, which we can generate at the start once and save them in an array
# I chose to not generate them during runtime and just have them saved beforehand, but it doesnt change much unless you generate it on every test case
# You check if two characters are equal, and if not you check if they are elsewhere (to add them to B count)
# very simple problem

perms = [
    ['12', '21'],
    ['123', '132', '213', '231', '312', '321'],
    ['1234', '1243', '1324', '1342', '1423', '1432', '2134', '2143', '2314', '2341', '2413',
     '2431', '3124', '3142', '3214', '3241', '3412', '3421', '4123', '4132', '4213', '4231', '4312', '4321']
]

for t in range(int(input())):

    inp = input().split(" ")

    n = inp[0]

    j = perms[len(n) - 2][int(inp[1]) - 1]
    k = perms[len(n) - 2][int(inp[2]) - 1]

    A = 0
    B = 0

    for i in range(len(n)):
        if j[i] == k[i]:
            A += 1
        elif j.find(k[i]) != -1:
            B += 1

    print(str(A) + "A" + str(B) + "B")