
map(int, input().split())

list(map(int, input().split()))

##A

S = input()
a = S[:-1]+'4'
print(a)


###B

def print_combinations(N):
    for x in range(N + 1):
        for y in range(N + 1):
            for z in range(N + 1):
                if x + y + z <= N:
                    print(x, y, z)
                if x+y+z > N:
                    break

N = int(input())
ans = print_combinations(N)
print(ans)

###C

def process_queries(N, queries):
    positions = [(i, 0) for i in range(N, 0, -1)]
    results = []

    for query in queries:
        if query[0] == 1:

            direction = query[1]
            new_head_pos = positions[-1]

            if direction == 'U':
                new_head_pos = (new_head_pos[0], new_head_pos[1] + 1)
            elif direction == 'D':
                new_head_pos = (new_head_pos[0], new_head_pos[1] - 1)
            elif direction == 'L':
                new_head_pos = (new_head_pos[0] - 1, new_head_pos[1])
            elif direction == 'R':
                new_head_pos = (new_head_pos[0] + 1, new_head_pos[1])

            positions.append(new_head_pos)

        else:
            p = query[1]
            results.append(positions[-p])
    
    return results

N, Q = map(int, input().split())
queries = []
for _ in range(Q):
    a, b = input().split()
    a = int(a)
    if a == 2:
        b = int(b)
    queries.append((a, b))

ans = process_queries(N, queries)
for i in range(len(ans)):
    print(*ans[i])



###D

def generate_dragon_spiral(N):
    grid = [['' for _ in range(N)] for _ in range(N)]
    x, y = N // 2, N // 2 
    grid[x][y] = 'T' 

    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  
    part = 1
    step = 1

    while part <= N**2 - 1:
        for dx, dy in directions:
            for _ in range(step):
                if part > N**2 - 1:
                    break
                x, y = x + dx, y + dy
                if 0 <= x < N and 0 <= y < N:
                    grid[x][y] = str(part)
                    part += 1
            if dx != 0:  
                step += 1

    return grid

N = int(input())
a = generate_dragon_spiral(N)
for i in range(N):
    print(*a[i])

###E

from collections import deque

def solve(N, M, A, edges):
    # Graph representation
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    # DP initialization
    dp = [0] * N
    dp[0] = 1
    visited = [False] * N

    # Graph traversal using BFS
    queue = deque([0])
    while queue:
        v = queue.popleft()
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                queue.append(u)
            if A[u] >= A[v]:
                dp[u] = max(dp[u], dp[v] + (A[u] != A[v]))

    return dp[N-1]


N, M = map(int, input().split())
A = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(M)]

max_score = solve(N, A, edges)
print(max_score)

