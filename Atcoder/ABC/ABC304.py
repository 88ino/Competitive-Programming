
N = int(input())

S = [None]*N
A = [None]*N

for i in range(N):
    S[i], A[i] = input().split()
    A[i] = int(A[i])

mi = min(A)
mi_in = A.index(mi)

for i in range(mi_in, N):
    print(S[i])
for i in range(mi_in):
    print(S[i])

#B
N = int(input())

if N < 10**3:
    N = N
elif 10**3 <= N < 10**4:
    N = N // 10**1 * 10**1
elif 10**4 <= N < 10**5:
    N = N // 10**2 * 10**2
elif 10**5 <= N < 10**6:
    N = N // 10**3 * 10**3
elif 10**6 <= N < 10**7:
    N = N // 10**4 * 10**4
elif 10**7 <= N < 10**8:
    N = N // 10**5 * 10**5
elif 10**8 <= N < 10**9:
    N = N // 10**6 * 10**6

print(N)

#C

import math

N, D = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

infected = [False]*N
infected[0] = True

while True:
    updated = False
    for i in range(N):
        if not infected[i]:
            continue
        for j in range(N):
            if infected[j]:
                continue
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            if math.sqrt(dx**2 + dy**2) <= D:
                infected[j] = True
                updated = True
    if not updated:
        break

for i in range(N):
    print("Yes" if infected[i] else "No")

#####
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.parent[y] = x

N, D = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]
uf = UnionFind(N)

for i in range(N):
    for j in range(i+1, N):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        if dx**2 + dy**2 <= D**2:
            uf.union(i, j)

for i in range(N):
    print("Yes" if uf.find(0) == uf.find(i) else "No")

#D
W, H = map(int, input().split())
N = int(input())

strawberries = set()
for _ in range(N):
    p, q = map(int, input().split())
    strawberries.add((p, q))

A = int(input())
a = list(map(int, input().split()))

B = int(input())
b = list(map(int, input().split()))

# イチゴの数を計算する関数
def count_strawberries(left, right, bottom, top):
    count = 0
    for strawberry in strawberries:
        if left < strawberry[0] < right and bottom < strawberry[1] < top:
            count += 1
    return count

# x 軸と y 軸の直線の位置をソート
a.sort()
b.sort()

# 最小値と最大値を初期化
min_count = float('inf')
max_count = 0

# 直線ごとにイチゴの数を計算
for i in range(A + 1):
    left = 0 if i == 0 else a[i - 1]
    right = W if i == A else a[i]
    
    for j in range(B + 1):
        bottom = 0 if j == 0 else b[j - 1]
        top = H if j == B else b[j]
        
        # イチゴの数を計算
        count = count_strawberries(left, right, bottom, top)
        
        # 最小値と最大値を更新
        min_count = min(min_count, count)
        max_count = max(max_count, count)

print(min_count, max_count)

#E
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def is_good_graph(n, edges, k, forbidden_edges):
    uf = UnionFind(n)

    # Union-Findを使用して与えられた辺を結合
    for u, v in edges:
        uf.union(u-1, v-1)

    # 禁止された辺が互いに同じ親を持っているか判定
    for x, y in forbidden_edges:
        if uf.find(x-1) == uf.find(y-1):
            return False

    return True

# グラフの入力
N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))

# 良いグラフの条件を満たす頂点の入力
K = int(input())
forbidden_edges = []
for _ in range(K):
    x, y = map(int, input().split())
    forbidden_edges.append((x, y))

# クエリの入力と処理
Q = int(input())
queries = []
for _ in range(Q):
    p, q = map(int, input().split())
    queries.append((p, q))

# 各クエリに対して回答を求める
for p, q in queries:
    # クエリに対して辺を追加してグラフが良いグラフか判定
    new_edges = edges + [(p, q)]
    if is_good_graph(N, new_edges, K, forbidden_edges):
        print("Yes")
    else:
        print("No")



#F


def solve(N, S):
    MOD = 998244353

    def factorize(n):
        result = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                result.append(i)
        if n > 1:
            result.append(n)
        return result

    T = [0]*(N+1)
    for i in range(1, N+1):
        T[i] = T[i-1] + int(S[i-1] == '#')

    dp = [0]*(N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1] + pow(i, MOD-2, MOD)


    answer = 0
    for i in range(1, N+1):
        if T[i] != T[i-1] and T[i] == T[N] - T[N%i]:
            factors = set(factorize(i))
            factors.add(i)
            for f in factors:
                answer += dp[f]
                answer %= MOD

    return answer

N = int(input())
S = input()
print(solve(N, S))


#G


