# IDEA: We group every consecutive L or R drum sequence and check the equivalent sequence in the other string
# As soon as one of them is impossible, we know the answer is NO
# If no impossible ones were found we know the answer is YES

# problem : https://codeforces.com/problemset/problem/2094/D

for t in range(int(input())):

    s = input()
    p = input()

    ctr = 0

    possible = True

    Lp, Rp = ctr, ctr
    Ls, Rs = ctr, ctr

    flag = False

    while (Rp < len(p) or Rs < len(s)):

        Lp = Rp
        Ls = Rs

        while (Rp < len(p) and p[Lp] == p[Rp]):
            Rp += 1
        
        while (Rs < len(s) and s[Ls] == s[Rs]):
            Rs += 1
        
        if (Ls < len(s) and Lp < len(p) and s[Ls] != p[Lp]):
            flag = True
            break

        if (Rp - Lp > 2 * (Rs - Ls) or Rp - Lp < Rs - Ls):
            flag = True
            break
    
    print("YES" if not flag else "NO")

        
