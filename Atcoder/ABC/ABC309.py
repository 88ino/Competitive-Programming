




#A
A, B = map(int, input().split())
if abs(A-B)==1 and not((A==3 and B==4)or(A==4 and B==3) or (A==6 and B==7)or(A==7 and B==6)):
    print("Yes")
else:
    print("No")




#B
N = int(input())
A = [input() for i in range(N)]
for i in range(N):
    for j in range(N):
        a =i
        b=j
        if i == 0 and j ==0:
            a+=1
        elif i==0:
            b-=1
        elif j ==0 and i!=N-1:
            a+=1
        elif j ==N-1:
            a-=1
        elif i ==N-1:
            b+=1
        print(A[a][b], end="")
    print("")


#C
N, K = map(int, input().split())
M = []
total = 0
for _ in range(N):
    a, b = map(int, input().split())
    M.append((a, b))
    total += b
if total <= K:
    print(1)
    exit()
M.sort()
for i in range(N):
    if total - M[i][1] <= K:
        print(M[i][0]+1)
        exit()
    else:
        total -= M[i][1]


#D
from collections import deque

N1, N2, M = map(int, input().split())
G = [ [] for _ in range(N1+N2+1) ]
for _ in range(M):
    a, b =  map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# 幅優先探索の初期化（dist[i] = ? ではなく dist[i] = -1 で初期化していることに注意）
dist = [ -1 ] * (N1+N2 + 1)
dist[1] = 0
Q = deque()
Q.append(1)

# 幅優先探索
while len(Q) >= 1:
	pos = Q.popleft() # キュー Q の先頭要素を取り除き、その値を pos に代入する
	for nex in G[pos]:
		if dist[nex] == -1:
			dist[nex] = dist[pos] + 1
			Q.append(nex)


# 幅優先探索の初期化（dist[i] = ? ではなく dist[i] = -1 で初期化していることに注意）
dist_N = [ -1 ] * (N1+N2 + 1)
dist_N[N1+N2] = 0
Q = deque()
Q.append(N1+N2)

# 幅優先探索
while len(Q) >= 1:
	pos = Q.popleft() # キュー Q の先頭要素を取り除き、その値を pos に代入する
	for nex in G[pos]:
		if dist_N[nex] == -1:
			dist_N[nex] = dist_N[pos] + 1
			Q.append(nex)
                        

print(max(dist)+max(dist_N)+1)

#E
import sys
input = sys.stdin.readline

class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

N, M = map(int, input().split())
parent = list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    G[parent[i-2]].append(i)

order = []
depth = [0] * (N + 1)

def dfs(v, d):
    order.append((v, d))
    depth[v] = d
    for nv in G[v]:
        dfs(nv, d + 1)
        order.append((v, d))

dfs(1, 1)

query = []
for _ in range(M):
    x, y = map(int, input().split())
    query.append((x, y, depth[x] - y, len(query)))

query.sort(key=lambda x: -x[2])

BIT = FenwickTree(2 * N + 1)

ans = [0] * M
cur = 0

for v, d in order:
    while cur < M and query[cur][2] >= d:
        ans[query[cur][3]] = BIT.sum(2 * N) - BIT.sum(depth[query[cur][0]] + query[cur][1])
        cur += 1
    BIT.add(d, 1)

for a in ans:
    print(a)


#F



