
def kmpSolution(txt,pat):
    m = len(pat)
    n = len(txt)

    lps1 = lpsGen(pat,m)

    print(lps1)

    i = 0
    j = 0

    while (n-i) >= (m-j):
        if pat[j] == txt[i]:
            i+=1
            j+=1
        if j==m:
            return (i-j)
        elif i<n and pat[j]!=txt[i]:
            if j!=0:
                j=lps1[j-1]
            else:
                i+=1

def lpsGen(pat,m):
    len = 0
    lps = [0]*m

    i = 1
    while i<m:
        if pat[i]==pat[len]:
            len+=1
            lps[i]=len
            i+=1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i]=0
                i+=1
    return lps

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
ans = kmpSolution(txt,pat)

print(ans)

print("KMP2 branch")