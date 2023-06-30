
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



