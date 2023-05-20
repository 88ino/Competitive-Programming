#ABC参加1回目
#A
A, B = map(int, input().split())
count = A//B
if A%B!=0:
    count+=1
print(count)

#B
H, W = map(int, input().split())
S = [input() for _ in range(H)]

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]
dirs = list(zip(dx, dy))

for i in range(H):
    for j in range(W):
        if S[i][j] == 's':
            for dx, dy in dirs:
                if all(0 <= i+k*dx < H and 0 <= j+k*dy < W and S[i+k*dx][j+k*dy] == 'snuke'[k] for k in range(5)):
                    for k in range(5):
                        print(i+k*dx+1, j+k*dy+1)
                    exit()

#C
""""""
N, M = map(int, input().split())
S = [None]*(N)
for i in range (N):
    S[i] = input()

count = 0
for i in range(N):
    for j in range(i+1, N):
        count = 0
        for k in range(M):
            if S[i][k] != S[j][k]:
                count += 1
            if count > 1:
                break
        if count ==1:
            print("Yes")
            exit()

print("No")
""""""
N, M = map(int, input().split())
S = [input() for _ in range(N)]

# 隣接リストを作成
adj = [[] for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if sum(x != y for x, y in zip(S[i], S[j])) == 1:
            adj[i].append(j)
            adj[j].append(i)

# DFSを実行して全ノードを探索
visited = [False]*N
def dfs(v):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            dfs(u)

dfs(0)

# 全ノードが探索されたかを確認
if all(visited):
    print("Yes")
else:
    print("No")

#D
N, M, D = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()), reverse=True)

ans = -1
i = 0
j = 0
while i < N and j < M:
    if abs(A[i] - B[j]) <= D:
        ans = max(ans, A[i] + B[j])
        i += 1
        j += 1
    elif A[i] > B[j]:
        i += 1
    else:
        j += 1

print(ans)
