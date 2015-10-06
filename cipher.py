__author__ = 'Robert'

n,k = input().split()
n,k = int(n),int(k)

ss = input()
sc = list(ss)

s = [0] * (n+k-1)

for i in range(n+k-1):
    if sc[i] == '0': s[i] = 0
    else: s[i] = 1

a = [0] * n

m = n//2 + 1
c = n + k - 2

n -= 1

a[0] = s[0]
a[n] = s[c]

y = 0
w = 0

for i in range(1,k):
    if i > n: break

    y += a[i-1]
    z = (s[i] + y)%2
    a[i] = z
    o = n-i
    w += a[o+1]
    z = (s[c-i] + w)%2
    a[o] = z

for i in range(k,m):
    y -= a[i-k]
    y += a[i-1]
    z = (s[i] + y)%2
    a[i]= z
    o = n-i
    w -= a[o+k]
    w += a[o+1]
    z = (s[c-i] + w)%2
    a[o] = z

[print(i,end='') for i in a]

