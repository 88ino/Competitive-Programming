#61
N, M = map(int, input().split())

E = [list(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(N+1)]
for a, b in E:
    G[a].append(b)
    G[b].append(a)

for i in range(1, N+1):
    print(str(i), end=": {")
    print(", ".join(map(str, G[i])), end="")
    print("}")

#62
import sys
sys.setrecursionlimit(120000)

def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(N+1)]

for a, b in E:
    G[a].append(b)
    G[b].append(a)

visited = [False]*(N+1)
dfs(1, G, visited)

Ans = True
for i in range(1, N+1):
    if visited[i] == False:
        print("The graph is not connected.")
        exit()
print("The graph is connected. ")

#63
from collections import deque
N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N+1)]
for a, b in E:
    G[a].append(b)
    G[b].append(a)

dist = [-1]*(N+1)
dist[1] = 0
Q = deque()
Q.append(1)

while len(Q) >= 1:
    pos = Q.popleft()
    for next in G[pos]:
        if dist[next] == -1:
            dist[next] = dist[pos] + 1
            Q.append(next)

for i in range(1, N+1):
    print(dist[i])

#64
import heapq
N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N+1)]
for a, b, c in E:
    G[a].append((b, c))
    G[b].append((a, c))

INF = 10**10
END = [False]*(N+1)
cur = [INF]*(N+1)
cur[1] = 0
Q = []
heapq.heappush(Q, (cur[1], 1))

while len(Q) >= 1:
    pos = heapq.heappop(Q)[1]
    if END[pos] == True:
        continue

    END[pos] = True
    for e in G[pos]:
        if cur[e[0]] > cur[pos] + e[1]:
            cur[e[0]] = cur[pos] + e[1]
            heapq.heappush(Q, (cur[e[0]], e[0]))

for i in range(1, N+1):
    if cur[i] != INF:
        print(cur[i])
    else:
        print("-1")

#65
N = int(input())
A = list(map(int, input().split()))

G = [[] for _ in range(N+1)]
for i in range(2, N+1):
    G[A[i-2]].append(i)

dp = [0]*(N+1)
for i in range(N, 0, -1):
    for j in G[i]:
        dp[i] += dp[j] + 1
print(*dp[1:])

#66
class unionfind:
    def __init__(self, n):
        self.n = n
        self.par = [-1]*(n+1)
        self.size = [1]*(n+1)
    
    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x
    
    def unite(self, u, v):
        root_u = self.root(u)
        root_v = self.root(v)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                self.par[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.par[root_v] = root_u
                self.size[root_u] += self.size[root_v]
    
    def same(self, u, v):
        return (self.root(u) == self.root(v))

N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]

uf = unionfind(N)
for tp, u, v in queries:
    if tp == 1:
        uf.unite(u, v)
    if tp == 2:
        if uf.same(u, v):
            print("Yes")
        else:
            print("No")

#67
class unionfind:
    def __init__(self, n):
        self.n = n
        self.par = [-1]*(n+1)
        self.size = [1]*(n+1)
    
    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x
    
    def unite(self, u, v):
        root_u = self.root(u)
        root_v = self.root(v)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                self.par[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.par[root_v] = root_u
                self.size[root_u] += self.size[root_v]
    
    def same(self, u, v):
        return (self.root(u) == self.root(v))
    
N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]

E.sort(key = lambda x: x[2])

uf = unionfind(N)
ans = 0
for a, b, c in E:
    if not uf.same(a, b) == True:
        uf.unite(a, b)
        ans += c

print(ans)

#68
class maxflow_edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

def dfs(pos, goal, F, G, used):
    if pos == goal:
        return F
    used [pos] = True
    for e in G[pos]:
        if e.cap > 0 and not used[e.to]:
            flow = dfs(e.to, goal, min(F, e.cap), G, used)

            if flow >= 1:
                e.cap -= flow
                G[e.to][e.rev].cap += flow
                return flow
    return 0

def maxflow(N, s, t, edges):
    G = [list() for _ in range(N+1)]
    for a, b, c in edges:
        G[a].append(maxflow_edge(b, c, len(G[b])))
        G[b].append(maxflow_edge(a, 0, len(G[a])-1))
    INF = 10**10
    total = 0
    while True:
        used = [False]*(N+1)
        F = dfs(s, t, INF, G, used)
        if F > 0:
            total += F
        else:
            break
    return total

N, M = map(int, input().split()) 
edges = [list(map(int, input().split())) for _ in range(M)]

ans = maxflow(N, 1, N, edges)
print(ans)

#69
class maxflow_edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

def dfs(pos, goal, F, G, used):
    if pos == goal:
        return F
    used [pos] = True
    for e in G[pos]:
        if e.cap > 0 and not used[e.to]:
            flow = dfs(e.to, goal, min(F, e.cap), G, used)

            if flow >= 1:
                e.cap -= flow
                G[e.to][e.rev].cap += flow
                return flow
    return 0

def maxflow(N, s, t, edges):
    G = [list() for _ in range(N+1)]
    for a, b, c in edges:
        G[a].append(maxflow_edge(b, c, len(G[b])))
        G[b].append(maxflow_edge(a, 0, len(G[a])-1))
    INF = 10**10
    total = 0
    while True:
        used = [False]*(N+1)
        F = dfs(s, t, INF, G, used)
        if F > 0:
            total += F
        else:
            break
    return total

N = int(input())
C = [input() for _ in range(N)]

edges = []
for i in range(N):
    for j in range(N):
        if C[i][j] == "#":
            edges.append((i+1, N+j+1, 1))

for i in range(N):
    edges.append((2*N+1, i+1, 1))
    edges.append((N+i+1, 2*N+2, 1))

ans = maxflow(2*N+2, 2*N+1, 2*N+2, edges)
print(ans)

#70
from collections import deque
N, M = map(int, input().split())
A = list(map(int, input().split()))
act = [list(map(lambda x: int(x)-1, input().split())) for i in range(M)]

def get_next(pos, x, y, z):
    state = [(pos//(2**i))%2 for i in range(N)]
    state[x] = 1 - state[x]
    state[y] = 1 - state[y]
    state[z] = 1 - state[z]

    ret = 0
    for i in range(N):
        if state[i] == 1:
            ret += 2**i
    return ret

G = [ list() for _ in range(2**N)]
for i in range(2**N):
    for x, y, z in act:
        nextstage = get_next(i, x, y, z)
        G[i].append(nextstage)

start = 0
for i in range(N):
    if A[i] == 1:
        start += 2**i
goal = 2**N -1

dist = [-1]*(2**N)
dist[start] = 0
Q = deque()
Q.append(start)

while len(Q) >= 1:
    pos = Q.popleft()
    for nex in G[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            Q.append(nex)

print(dist[goal])
