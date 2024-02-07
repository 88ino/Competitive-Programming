# 281
S = list(input())
n = len(S)
flag = True
if n != 8:
    print("No")
    exit()
if S[0].isdecimal() or S[-1].isdecimal():
    flag = False
for i in range(1, n-1):
    if S[i].isdecimal() == False:
        flag = False
        break
if S[1] == "0":
    flag = False

print("Yes") if flag else print("No")


# 282
N, M = map(int, input().split())
S = []
for _ in range(N):
    s = input()
    S.append(s)
ans = 0

for i in range(N-1):
    for j  in range(i+1, N):
        flag = True
        for k in range(M):
            if S[i][k] == "x" and S[j][k] == "x":
                flag = False
        if flag:
            ans += 1
print(ans)


# 283
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    q0, *q = map(int, input().split())
    if q0 == 1:
        A[q[0]-1] = q[1]
    else:
        print(A[q[0]-1])


# 284
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A[i] %2 == 1 for i in range(N)))


# 285
N = int(input())
S = input()

for i in range(1, N):
    a = 0
    for k in range(N-i):
        if S[k] == S[i+k]:
            break
        a = k + 1 
    print(a)
    

# 286
N = int(input())
S = list(input())
T = []
for i in range(N):
    if i >= 1 and T[-1] == "n" and S[i] == "a":
        T.append("y")
    T.append(S[i])

ans = "".join(T)
print(ans)


# 287
N, M = map(int, input().split())
S = []
T = []
for _ in range(N):
    s = input()
    S.append(s[3:])
for _ in range(M):
    t = input()
    T.append(t)

count = 0
for s in S:
    for t in set(T):
        if s == t:
                count += 1
print(count)


# 288
N, K = map(int, input().split())
S = [input() for _ in range(K)]
S.sort()
for s in S:
    print(s)


# 289
N, M = map(int, input().split())
a = set(list(map(int, input().split())))
B = []
i = 1
while i <= N:
    l = i
    r = i
    if r in a:
        for rr in range(i+1, N+1):  
            r = rr
            if rr not in a:
                break
    for j in range(r, l-1, -1):
        B.append(j)
    i = r+1

print(*B)


# 290
N, K = map(int, input().split())
S = input()
T = []
count = 0
for i in range(N):
    if S[i] == "o":
        if count >= K:
            T.append("x")
        else:
            T.append("o")
            count += 1
    else:
        T.append("x")
print("".join(T))


# 291
N = int(input())
X = list(map(int, input().split()))
X.sort()
ans = sum(X[N:-N]) / (3*N)
print(ans)


# 292
from collections import defaultdict, deque
import imp
N, Q = map(int, input().split())
p = defaultdict()
for i in range(1, N+1):
    p[i] = 0

for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        p[x] += 1
    elif c == 2:
        p[x] += 2
    else:
        if p[x] >= 2:
            print("Yes")
        else:
            print("No")


# 293
N = int(input())
A = list(map(int, input().split()))
B = set()
for i in range(N):
    p = i+1
    if p not in B:
        B.add(A[i])
ans = list(set(i for i in range(1, N+1)) - B)
ans.sort()
print(len(ans))
print(*ans)


# 294
H, W = map(int, input().split())
for i in range(H):
    s = []
    a = list(map(int, input().split()))
    for j in range(W):
        if a[j] == 0:
            s.append(".")
        else:
            s.append(chr(ord("A") + a[j] - 1))
    print("".join(s))


# 295
def dist(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

R, C = map(int, input().split())
field = []
bomb = []
for i in range(R):
    s = list(input())
    field.append(s)
    for j in range(C):
        if s[j]!="#" and s[j]!=".":
            power = int(s[j])
            bomb.append((i, j, power))

for i in range(R):
    for j in range(C):
        for b in bomb:
            r1, c1, p = b
            r2, c2 = i, j
            d = dist(r1, c1, r2, c2)
            if d <= p:
                field[r2][c2] = "."

for f in field:
    print("".join(f))


# 296
h = "abcdefgh"
w = "12345678"
for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == "*":
            print(h[j] + w[7-i])


# 297
S = input()
a = 0
for i in range(8):
    if S[i] == "B":
        a += i
if a%2==0:
    print("No")
    exit()

for i in range(8):
    if S[i] == "R":
        for j in range(i+1, 8):
            if S[j] == "R":
                print("No")
                exit()
            elif S[j] == "K":
                print("Yes")
                exit()


# 298
import numpy as np

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
A = np.array(A)
B = np.array(B)
for _ in range(4):
    if np.min(B-A) >= 0:
        print("Yes")
        exit()
    A = np.rot90(A)
print("No")


# 299
N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
if T in C:
    win = T
else:
    win = C[0]
B = []
for i in range(N):
    if C[i] == win:
        B.append((R[i], i+1))
B.sort(reverse=True)
print(B[0][1])


# 300
def w_shift(m):
    a = []
    for i in range(1, H):
        a.append(m[i])
    a.append(m[0])
    return a

def h_shift(m):
    a = []
    for i in range(H):
        a.append([*m[i][1:], m[i][0]])
    return a

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]
for i in range(H):
    if A == B:
        print("Yes")
        exit()
    for j in range(W):
        A = h_shift(A)
        if A == B:
            print("Yes")
            exit()
    A = w_shift(A)
print("No")

