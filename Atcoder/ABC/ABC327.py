
map(int, input().split())

list(map(int, input().split()))

int(input())

###A
N = int(input())
S = input()
for i in range(N-1):
    if (S[i] =="a" and S[i+1]=="b") or (S[i] =="b" and S[i+1]=="a"):
        print("Yes")
        exit()
print("No")


###B
B = int(input())
for a in range(1, 10**3):
    if a**a > 10**18:
        print(-1)
        exit()
    if a**a == B:
        print(a)
        exit()


###C
def sudoku(grid):
    for row in grid:
        if len(set(row)) != 9:
            return "No"

    for col in range(9):
        if len(set(grid[row][col] for row in range(9))) != 9:
            return "No"

    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            subgrid = [grid[row][col] for row in range(start_row, start_row + 3) 
                                         for col in range(start_col, start_col + 3)]
            if len(set(subgrid)) != 9:
                return "No"
    return "Yes"

grid = [list(map(int, input().split())) for _ in range(9)]

print(sudoku(grid))


###D
from collections import deque

def is_bipartite(N, edges):
    colors = [0] * (N + 1) 
    for i in range(1, N + 1):
        if colors[i] == 0:  
            queue = deque([i])
            colors[i] = 1  
            while queue:
                node = queue.popleft()
                for neighbor in edges[node]:
                    if colors[neighbor] == 0: 
                        colors[neighbor] = -colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]: 
                        return False
    return True

def is_good_sequence_pair(N, M, A, B):
    edges = [[] for _ in range(N + 1)]
    for i in range(M):

        edges[A[i]].append(B[i])
        edges[B[i]].append(A[i])

    return "Yes" if is_bipartite(N, edges) else "No"

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(is_good_sequence_pair(N, M, A, B))


###E
def remove(N, k, P):
    indexed_performances = [(performance, i) for i, performance in enumerate(P)]
    indexed_performances.sort(key=lambda x: x[0])
    top_k_indexed_performances = indexed_performances[N-k:]
    top_k_indexed_performances.sort(key=lambda x: x[1])
    
    restored_performances = [performance for performance, _ in top_k_indexed_performances]
    return restored_performances

def calculate_rate(performance, weights, normalization):
    k = len(performance) 
    weighted_sum = sum(p * w for p, w in zip(performance, weights))
    rate = weighted_sum / normalization[k-1] - 1200 / (k ** 0.5)
    return rate

N = int(input())
P = list(map(int, input().split()))

weights = [(0.9 ** i) for i in range(N)]
normalization = [sum(weights[:k]) for k in range(1, N+1)]

best_rate = float('-inf')

for k in range(1, N+1):
    Q = remove(N, k, P)
    w = weights[:k]
    w.sort()
    a = calculate_rate(Q, w, normalization)
    best_rate = max(best_rate, a)

print(best_rate)



