# 241
from math import cos, sin
import stat


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(M):
    flag = False
    for j in range(N):
        if B[i] == A[j]:
            flag = True
            A[j] = -1
            break
    if flag == False:
        print("No")
        exit()
print("Yes")
        

# 242
S = list(input())
S.sort()
print("".join(S))


# 243
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count1 = 0
count2 = 0
for i in range(N):
    if A[i]==B[i]:
        count1 += 1
for i in range(N):
    for j in range(N):
        if A[i] == B[j] and i != j:
            count2 += 1
print(count1)
print(count2)


# 244
N = int(input())
T = input()
x = 0
y = 0
muki = [(1, 0), (0, -1), (-1, 0), (0, 1)]
a = 0
for i in range(N):
    if T[i] == "R":
        a += 1
    if T[i] == "S":
        dx, dy = muki[a%4]
        x += dx
        y += dy
print(x, y)

#
N = int(input())
T = input()
x, y = 0, 0
dx, dy = 1, 0
for t in T:
    if t =="S":
        x+=dx
        y+=dy
    else:
        dx, dy = dy, -dx
print(x, y)


# 245
N = int(input())
A = set(map(int, input().split()))
B = set(i for i in range(N+1))
print(min(B-A))


# 246
A, B = map(int, input().split())
r = (A**2+B**2)**0.5
print(A/r, B/r)


# 247
N = int(input())
S = []
T = []
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)
for i in range(N):
    flag = False
    for s in [S[i], T[i]]:
        ok1 = True
        for j in range(N):
            #名字か名前のどちらかが他と一致するならok1はFalse
            if i!=j and (s==S[j] or s==T[j]):
                ok1 = False
        #片方が使えるならTrue
        if ok1 == True:
            flag = True
    if flag == False:
        print("No")
        exit()
print("Yes")  


# 248
A, B, K = map(int, input().split())
for i in range(31):
    if A*K**i >= B:
        print(i)
        break


# 249
S = input()
flag_s = False
flag_l = False
for i in range(len(S)):
    if ord("a") <= ord(S[i]) <= ord("z"):
        flag_s = True
    if ord("A") <= ord(S[i]) <= ord("Z"):
        flag_l = True
if len(S) == len(set(list(S))) and flag_l==True and flag_s==True:
    print("Yes")
else:
    print("No")


# 250
N, A, B = map(int, input().split())
for i in range(N):
    for _ in range(A):
        for j in range(N):
            if (i+j)%2==0:
                a = "."
            else:
                a = "#"
            for _ in range(B):
                print(a, end="")
        print("")


# 251
N, W = map(int, input().split())
A = list(map(int, input().split()))
count = set()

for i in range(N):
    if A[i] <= W:
        count.add(A[i])
    for j in range(N):
        if A[i]+A[j] <= W and i != j:
            count.add(A[i]+A[j])
        for k in range(N):
            if A[i]+A[j]+A[k] <= W and i != j and j!=k and k!=i:
                count.add(A[i]+A[j]+A[k])
print(len(count))


# 252
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = max(A)
for i in range(K):
    if A[B[i]-1] == M:
        print("Yes")
        exit()
print("No")


# 253
H, W = map(int, input().split())
a = []
for y in range(H):
    l = input()
    for x in range(W):
        if l[x]=="o":
            a.append((x,y))
print(abs(a[0][0]-a[1][0])+abs(a[0][1]-a[1][1]))


# 254
N = int(input())
A = [[1]*(i+1) for i in range(N)]
for i in range(1, N):
    for j in range(1, i-1):
        A[i][j] = A[i-1][j] + A[i-1][j-1]
for i in range(N):
    print(*A[i])


# 255
N, K = map(int, input().split())
A = list(map(int, input().split()))
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

def dis(P1, P2):
    return ((P1[0]-P2[0])**2 + (P1[1]-P2[1])**2)**0.5

farest = 0
for i in range(N):
    near =10**10
    for k in range(K):
        near = min(near, dis(P[i], P[A[k]-1]))
    farest = max(farest, near)
            
print(farest)


# 256
N = int(input())
A = list(map(int, input().split()))
P = 0
state = [0, 0, 0, 0]
for x in A:
    next = [0, 0, 0, 0]
    state[0] = 1
    for i in range(4):
        if state[i] == 1:
            if i+x >= 4:
                P += 1
            else:
                next[i+x] = 1
    state = next
print(P)


# 257
n, k, q = map(int,input().split())
A = list(map(int,input().split()))
L = list(map(int,input().split()))
state = [0]*(n+2)
for i in range(k):
    state[A[i]] = 1

for i in range(q):
    p = A[L[i]-1]
    if p!=n and state[p+1] == 0:
        state[p], state[p+1] = state[p+1], state[p]
        A[L[i]-1] += 1

for i in range(n+1):
    if state[i] != 0:
        print(i, end=" ")


# 258
N = int(input())
A = [ input() for _ in range(N)]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
ans = 0
for i in range(N):
    for j in range(N):
        for r in range(8):
            x = i
            y = j
            sum_a = 0
            for _ in range(N):
                sum_a *= 10
                sum_a += int(A[x][y])
                x = (x + dx[r])%N
                y = (y + dy[r])%N
            ans = max(ans, sum_a)
for i in range(N):
    print(str(ans)[i], end="")
            

# 259
from math import cos, sin, radians

a, b, d = map(int, input().split())
d = radians(d)

x = a*cos(d) - b*sin(d)
y = a*sin(d) + b*cos(d)
print(x, y)


# 260
N,X,Y,Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = []
for i in range(N):
    S.append( (i+1, A[i], B[i]) )
S.sort(key=lambda x: (-x[1], x[0]))
S[X:] = sorted(S[X:], key=lambda x: (-x[2], x[0]))
S[X+Y:] = sorted(S[X+Y:], key=lambda p: (-p[1]-p[2], p[0]))
S[:X+Y+Z] = sorted(S[:X+Y+Z], key=lambda p: p[0])

for p in S[:X+Y+Z]:
    print(p[0])

