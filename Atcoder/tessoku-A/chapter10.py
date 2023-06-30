#71
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

ans = 0
for i in range(N):
    ans += A[i]*B[i]

print(ans)

#72
import itertools

H, W, K = map(int, input().split())
c = [ input() for _ in range(H)]

def paint_row(H, W, d, remain):
    column = [ ([d[i][j] for i in range(H)].count('.'), j) for j in range(W) ]
    column.sort(reverse=True)

    for j in range(remain):
        idx = column[j][1]
        for i in range(H):
            d[i][idx] = '#'
    
    return sum( map(lambda x: x.count('#'), d) )

ans = 0
for v in itertools.product([0, 1], repeat=H):
    d = [ list(c[i]) for i in range(H) ]
    remain = K
    for i in range(H):
        if v[i] == 1:
            d[i] = ['#']*W
            remain -= 1
    if remain >= 0:
        sub = paint_row(H, W, d, remain)
        ans = max(ans, sub)

print(ans)

#73
import heapq

N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(M)]

G = [list() for _ in range(N+1)]
for a, b, c, d in road:
    G[a].append((b, c*10000-d))
    G[b].append((a, c*10000-d))

INF = 10**10
definition = [False]*(N+1)
cur = [INF]*(N+1)
cur[1] = 0
Q = []
heapq.heappush(Q, (cur[1], 1) )

while len(Q) >= 1:
    pos = heapq.heappop(Q)[1]
    if definition[pos] == True:
        continue
    definition[pos] = True
    for e in G[pos]:
        if cur[e[0]] > cur[pos] + e[1]:
            cur[e[0]] = cur[pos] + e[1]
            heapq.heappush(Q, (cur[e[0]], e[0]) )

dist = (cur[N] + 9999)//10000
#tree = dist*10000 - cur[N]
tree = (10000-cur[N])%10000

print(dist, tree)

#74
N = int(input())
P = [ list(map(int, input().split())) for _ in range(N) ]
X = [None]*N
Y = [None]*N

for i in range(N):
    for j in range(N):
        if P[i][j] != 0:
            X[i] = P[i][j]
            Y[j] = P[i][j]

def inversion(A):
    ans = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                ans += 1
    return ans

print( inversion(X) + inversion(Y) )

#75
N = int(input())
problem = [ list(map(int, input().split())) for _ in range(N) ]

problem.sort(key=lambda x: x[1])
dp = [ [-10**10]*(1441) for _ in range(N+1) ]
dp[0][0] = 0
for i in range(N):
    T, D = problem[i]
    for j in range(1441):
        if j > D or j < T:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max( dp[i][j], dp[i][j-T] + 1 )
ans = max(dp[N])
print(ans)

#76
import bisect

N, W, L, R = map(int, input().split())
X = list(map(int, input().split()))
X = [0] + X + [W]

M = 10**9+7
dp = [0]*(N+2)
dp_sum = [0]*(N+2)
dp[0] = 1
dp_sum[0] = 1

for i in range(1, N+2):
    posl = bisect.bisect_left(X, X[i]-R)
    posr = bisect.bisect_left(X, X[i]-L+1)-1

    dp[i] = (dp_sum[posr] if posr>=0 else 0) - (dp_sum[posl-1] if posl>=1 else 0)
    dp[i] %= M

    dp_sum[i] = dp_sum[i-1] + dp[i]
    dp_sum[i] %= M

print(dp[N+1])

#77
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def check(x):
    count = 0
    last = 0
    for i in range(N):
        if A[i] - last >= x and L - A[i] >= x:
            count += 1
            last = A[i]
    return (count >= K)

left, right = 1, 10**9
while left < right:
    mid = (left + right + 1)//2
    ans = check(mid)
    if ans == False:
        right = mid - 1
    else:
        left = mid

print(left)
