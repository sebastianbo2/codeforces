places = list(map(int, input().split(" ")))

n, m = places[0], places[1]

p = dict()

for i in range(m):
    word = list(input().split(" "))
    word1, word2 = word[0], word[1]
    p[word1] = word1 if len(word1) <= len(word2) else word2

lecture = list(input().split(" "))

for i in range(n):
    print(p[lecture[i]], end=" ")