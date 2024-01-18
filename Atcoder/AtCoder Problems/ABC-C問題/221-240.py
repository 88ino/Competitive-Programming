# 221
from itertools import permutations

N = list(input())
ans = []
for v in permutations(N):
    for i in range(1, len(N)):
        a = v[:i]
        b = v[i:]
        if b[0] == "0":
            continue
        a = int("".join(a))
        b = int("".join(b))
        ans.append(a*b)
print(max(ans))


# 222
def GCP(a,b):
    if a == b:
        return -1
    elif (a=="G" and b=="C") or (a=="C" and b=="P") or (a=="P" and b=="G"):
        return 0
    else:
        return 1

N, M = map(int, input().split())
A = [ input() for _ in range(2*N) ]
rank = [[0, i] for i in range(2*N)]
     
for j in range(M):
    for i in range(N): 
        P1 = rank[2*i][1]
        P2 = rank[2*i+1][1]
        result = GCP(A[P1][j], A[P2][j])
        if result != -1:
            rank[2*i+result][0] -= 1
    rank.sort()
    
for _,i in rank: 
    print(i+1)


# 223
N = int(input())
T = []
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    T.append(a/b)
ans = 0
time = sum(T) / 2

for i in range(N):
    if time - T[i] < 0:
        ans += B[i]*(time)
        break
    time -= T[i]
    ans += A[i]

print(ans)


# 224

def is_triangle(d1, d2, d3):
    r = (d2[0]-d1[0])*(d3[1]-d1[1]) - (d2[1]-d1[1])*(d3[0]-d1[0])
    if r == 0:
        return False
    else:
        return True

N = int(input())
dot = []
for _ in range(N):
    x, y = map(int, input().split())
    dot.append((x,y))
count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if is_triangle(dot[i], dot[j], dot[k]):
                count += 1
print(count)


# 225
N, M = map(int, input().split())
B = [ list(map(int, input().split())) for _ in range(N) ]
flag = True
lim = 10**100*7+7
if (B[0][0]-1)%7 + M-1 >= 7:
    flag = False
for i in range(N):
    for j in range(M):
        if B[i][j] != B[0][0] + i*7 + j or B[i][j] > lim:
            flag = False
if flag:
    print("Yes")
else:
    print("No")


# 226
from collections import deque
N = int(input())
T = []
A = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    T.append(tmp[0])
    if tmp[1]==0:
        A.append([-1])
    else:
        A.append(tmp[2:])

ans = 0
Q = deque()
Q.append(N-1)
st = set()
while Q:
    now = Q.popleft()
    if now in st:
        continue
    st.add(now)
    ans += T[now]

    if A[now][0] == -1:
        continue
    for i in range(len(A[now])):
        if A[now][i]-1 in st:
            continue
        Q.append(A[now][i]-1)
print(ans)


# 227
N = int(input())
ans = 0
for a in range(1, N+1):
    if a**3 > N:
        break
    for b in range(a, N+1):
        if a*b**2 > N:
            break
        #Cは[B, N/AB]
        ans += N//a//b -b +1
print(ans)


# 228
N, K = map(int, input().split())
P = []
for _ in range(N):
    p = sum(list(map(int, input().split())))
    P.append(p)
Q = sorted(P, reverse=True)
ikiti = Q[K-1]
for i in range(N):
    if P[i] + 300 >= ikiti:
        print("Yes")
    else:
        print("No")


# 229
N, W  = map(int, input().split())
ans = 0
C = []
for _ in range(N):
    a, b = map(int, input().split())
    C.append((a, b))
C.sort(reverse=True)
i = 0
while W > 0 and N > i:
    A = C[i][0]
    B = C[i][1]
    ans += A*min(B, W)
    i += 1
    W -= B
print(ans)


# 230
N, A, B = map(int,input().split())
P, Q, R, S = map(int,input().split())

k1 = max(1-A, 1-B)
k2 = min(N-A, N-B)
k3 = max(1-A, B-N)
k4 = min(N-A, B-1)

masu = [['.']*(S-R+1) for _ in range(Q-P+1)]

for i in range(Q-P+1):
    for j in range(S-R+1):
        ki = P + i - A
        kj = R + j - B
        if ki == kj:
            if k1 <= ki <= k2:
                masu[i][j] = '#'
        if ki == B - R - j:
            if k3 <= ki <= k4:
                masu[i][j] = '#'

for i in range(Q-P+1):
    print(''.join(masu[i]))


# 231
from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
for _ in range(Q):
    x = int(input())
    ans = N - bisect_left(A, x)
    print(ans)


# 232
from itertools import permutations

N, M = map(int, input().split())
X = [ [False]*N for _ in range(N)] 
Y = [ [False]*N for _ in range(N)] 

for _ in range(M):
    a, b = map(int, input().split())
    X[a-1][b-1] = True
    X[b-1][a-1] = True
for _ in range(M):
    c, d = map(int, input().split())
    Y[c-1][d-1] = True
    Y[d-1][c-1] = True

ans = False
for p in permutations(range(N)):
    flag = True
    for i in range(N):
        for j in range(N):
            if X[i][j] != Y[p[i]][p[j]]:
                flag = False
    if flag:
        ans = True
print("Yes" if ans else "No")


# 233
N, X = map(int, input().split())
a = []
for _ in range(N):
    _, *a_ = list(map(int, input().split()))
    a.append(a_)

P = [1]
for i in range(N):
    tmp = []
    for ai in a[i]:
        for p in P:
            tmp.append(ai*p)
    P = tmp

print(P.count(X))


# 234
K = int(input())
r = []
while K!=0:
    a = K%2
    K //= 2
    if a == 1:
        a = 2
    r.append(a)
r.reverse()
ans = ''.join(str(i) for i in r)
print(ans)


# 235
from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = defaultdict(list)

for i in range(N):
    L[A[i]].append(i+1)

for _ in range(Q):
    x, k = map(int, input().split())
    if len(L[x]) < k:
        print(-1)
        continue
    print(L[x][k-1])


# 236
N, M = map(int, input().split())
S = input().split()
T = set(input().split())

for s in S:
    if s in T:
        print("Yes")
    else:
        print("No")


# 237



# 238



# 239



# 240



