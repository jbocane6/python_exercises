def pgen(n):
    a = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if a[i] == True:
            for j in range(i*i, n+1, i):
                a[j]=False
    
    pl = []
    for p in range(2, n+1):
        if a[p]: pl.append(p)
    return pl

print(pgen(1000))
