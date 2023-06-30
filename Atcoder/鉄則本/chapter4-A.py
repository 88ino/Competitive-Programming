#16
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None]*(N+1)
dp[1] = 0
dp[2] = A[0]

for i in range(3, N+1):
    dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

print(dp[N])

#17
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [None]*(N+1)
dp[1] = 0
dp[2] = A[0]

for i in range(3, N+1):
    dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

Ans = []
P = N
while True:
    Ans.append(P)
    if P == 1:
        break

    if dp[P] == dp[P-1] + A[P-2]:
        P = P-1
    else:
        P = P-2
Ans.reverse()

print(len(Ans))
for i in range(len(Ans)):
    print(Ans[i], end=" ")
print("")

#18
N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[None]*(S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range (1, S+1):
    dp[0][i] = False

for i in range(1, N+1):
    for j in range(0, S+1):

        if j < A[i-1]:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

        else:
            if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[N][S] == True:
    print("Yes")
else:
    print("No")

#19
N, W = map(int, input().split())
w = [None]*(N+1)
v = [None]*(N+1)
for i in range(1, N+1):
    w[i], v[i] = map(int, input().split())

dp = [[0]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range (1, N+1):
    for j in range (1, W+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])

print(max(dp[N]))

#20
S = input()
T = input()
N = len(S)
M = len(T)

dp = [[None]*(M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range (N+1):
    for j in range (M+1):
        if i>=1 and j>=1 and S[i-1]==T[j-1]:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]+1)
        elif i>=1 and j>=1:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        elif j>=1:
            dp[i][j] = dp[i][j-1]
        elif i>=1:
            dp[i][j] = dp[i-1][j]

print(dp[N][M])

#21
N = int(input())
P = [None]*(N+1)
A = [None]*(N+1)
for i in range(1, N+1):
    P[i], A[i] = map(int, input().split())

dp = [[None]*(N+1) for _ in range (N+1)]
dp[1][N] = 0

for LEN in range(N-2, -1, -1):
    for l in range(1, N-LEN+1):
        r = l + LEN

        score_l = 0
        if l>=2 and l<=P[l-1] and P[l-1]<=r:
            score_l = A[l-1]
        
        score_r = 0
        if r<=N-1 and l<=P[r+1] and P[r+1]<=r:
            score_r = A[r+1]
        
        if l==1:
            dp[l][r] = dp[l][r+1] + score_r
        elif r==N:
            dp[l][r] = dp[l-1][r] + score_l
        else:
            dp[l][r] = max(dp[l-1][r] + score_l, dp[l][r+1] + score_r)

Ans = 0
for i in range(1, N+1):
    Ans = max(Ans, dp[i][i])
print(Ans)

#22
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [-10**10]*(N+1)
dp[1] = 0
for i in range(1, N):
    dp[A[i-1]] = max(dp[A[i-1]], dp[i]+100)
    dp[B[i-1]] = max(dp[B[i-1]], dp[i]+150)

print(dp[N])

#23
N, M = map(int, input().split())
A = [None]*(M)
for i in range(M):
    A[i] = list(map(int, input().split()))

dp = [[10**5]*(2**N) for _ in range(M+1)]
dp[0][0] = 0

for i in range(1, M+1):
    for j in range(0, 2**N):
        free = [None]*N
        for k in range(0, N):
            if (j//(2**k))%2 == 0:
                free[k] = 0
            else:
                free[k] = 1
        v = 0
        for k in range(0, N):
            if free[k]==1 or A[i-1][k]==1:
                v += 2**k

        dp[i][j] = min(dp[i][j], dp[i-1][j])
        dp[i][v] = min(dp[i][v], dp[i-1][j]+1)

if dp[M][2**N-1] == 10**5:
    print(-1)
else:
    print(dp[M][2**N-1])

#24
import bisect
N = int(input())
A = list(map(int, input().split()))

LEN = 0
L = []
dp = [0]*N

for i in range(N):
    pos = bisect.bisect_left(L, A[i])
    dp[i] = pos

    if dp[i] >= LEN:
        L.append(A[i])
        LEN += 1
    else:
        L[dp[i]] = A[i]
print(LEN)

#25
H, W = map(int, input().split())
c = [None]*H
for i in range(H):
    c[i] = input()

dp = [[0]*(W+1) for _ in range(H+1)]
for i in range(1, H+1):
    for j in range(1, W+1):
        if i==1 and j==1:
            dp[i][j] = 1
        else:
            if i>=2 and c[i-2][j-1]=='.':
                dp[i][j] += dp[i-1][j]
            if j>=2 and c[i-1][j-2]=='.':
                dp[i][j] += dp[i][j-1]

print(dp[H][W])

## 25'
H, W = map(int, input().split())
c = [None]*H
for i in range(H):
    c[i] = input()

dp = [[0]*(W) for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i>=1 and c[i-1][j]=='.':
            dp[i][j] += dp[i-1][j]
        if j>=1 and c[i][j-1]=='.':
            dp[i][j] += dp[i][j-1]

print(dp[H-1][W-1])
