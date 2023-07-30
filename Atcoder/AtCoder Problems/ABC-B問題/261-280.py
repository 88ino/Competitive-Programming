# 261
import imp
from turtle import Turtle


N = int(input())
A = [input() for _ in range(N)]
flag = True
for i in range(N):
    for j in range(N):
        if (A[i][j]=="W" and A[j][i]=="W") or (A[i][j]=="L" and A[j][i]=="L") or (A[i][j]=="D" and A[j][i]!="D"):
            flag = False
if flag:
    print("correct")
else:
    print("incorrect")


# 262
N, M = map(int, input().split())
G = [[False]*N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u][v] = True
    G[v][u] = True

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if G[i][j] and G[j][k] and G[k][i]:
                ans += 1
print(ans)
    

# 263
N = int(input())
P = list(map(int, input().split()))
a = N
ans = 0
while a != 1:
    a = P[a-2]
    ans += 1
print(ans)


# 264
R, C = map(int, input().split())
if max(abs(R-8), abs(C-8))%2 == 1:
    print("black")
else:
    print("white")


# 265
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
B = {}
for _ in range(M):
    x, y = map(int, input().split())
    x -= 2
    B[x] = y

time = T
for i in range(N-1):
    if time - A[i] <= 0:
        print("No")
        exit()
    time -= A[i]
    if i in B:
        time += B[i]

print("Yes")


# 266
N = int(input())
m = 998244353
print(N%m)


# 267
s = input()
S = [None] + list(int(s[i]) for i in range(10))
S_l = [ S[7], S[4], S[2]+S[8], S[1]+S[5], S[3]+S[9], S[6], S[10] ]
for i in range(7):
    if S[1] != 0:
        break
    if S_l[i] != 0:
        for j in range(i+1, 7):
            if S_l[j] == 0:
                for k in range(j+1, 7):
                    if S_l[k] != 0:
                        print("Yes")
                        exit()
print("No")


# 268
S = input()
T = input()
if len(S) > len(T):
        print("No")
        exit()

for i in range(len(S)):
    if S[i] != T[i]:
        print("No")
        exit()
print("Yes")


# 269
M = []
for i in range(10):
    a = input()
    M.append(a)
A, C = 100, 100
B, D = 0, 0
for i in range(10):
    for j in range(10):
        if M[i][j] == "#":
            A = min(i+1, A)
            B = max(i+1, B)
            C = min(j+1, C)
            D = max(j+1, D) 
print(A, B)
print(C, D)


# 270
X, Y, Z = map(int, input().split())
if Y < 0:
    X*=-1
    Y*=-1
    Z*=-1
#ゴールが壁より右にある時ハンマーが必要
if Y < X:
    #ハンマーが壁より右にあると不可能
    if Y < Z:
        print(-1)
        exit()
    else:
        if Z > 0:
            print(X)
        else:
            print(2*abs(Z) + X)

#ゴール前に壁がないとき
else:
    print(abs(X))   


# 271
N, Q = map(int, input().split())
an = []
for _ in range(N):
    l, *a = map(int, input().split())
    an.append([*a])

for _ in range(Q):
    s, t = map(int, input().split())
    print(an[s-1][t-1])


# 272
N, M = map(int, input().split())
check = [ [False]*N for _ in range(N) ]
for _ in range(M):
    x = list(map(int, input().split()))
    for i in range(x[0]):
        for j in range(i+1, x[0]):
            check[x[i+1]-1][x[j+1]-1] = True
            check[x[j+1]-1][x[i+1]-1] = True
for i in range(N):
    for j in range(N):
        if check[i][j]==False and i!=j:
            print("No")
            exit()
print("Yes")


# 273
X, K = map(int, input().split())
for i in range(K):
    X = round(X+0.1, -i-1)
print(int(X))


# 274
H, W = map(int, input().split())
C = [ input() for _ in range(H) ]
X = [0]*W
for j in range(W):
    for i in range(H):
        if C[i][j] == "#":
            X[j] += 1
for j in range(0, W):
    print(X[j], end=" ")


# 275
a, b, c, d, e, f = map(int, input().split())
print( (a*b*c-d*e*f) % 998244353 )


# 276
N, M = map(int, input().split())
G = [ [] for _ in range(N+1) ]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in range(1, N+1):
    G[i].sort()
    print(len(G[i]), end=" ")
    print(*G[i])


# 277
N = int(input())
flag = True
first = ["H", "D", "C", "S"]
second = ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"]
identity = []
for _ in range(N):
    s = input()
    if not (s[0] in first and s[1] in second and s not in identity):
        flag = False
    identity.append(s)
if flag:
    print("Yes")
else:
    print("No")
        

# 278
H, M = map(int, input().split())
def check(h, m):
    A = h//10
    B = h%10
    C = m//10
    D = m%10
    return A*10+C<=23 and B*10+D<=59

while not check(H, M):
    M += 1
    if M==60:
        H += 1
        M = 0
    H %= 24
print(H, M)


# 279
S = input()
T = input()
if T in S:
    print("Yes")
else:
    print("No")


# 280
N = int(input())
S = list(map(int, input().split()))
A = []
A.append(S[0])
for i in range(1, N):
    a = S[i] - sum(A[:i])
    A.append(a)
print(*A)

