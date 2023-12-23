
map(int, input().split())

list(map(int, input().split()))

###A
B, G = map(int, input().split())
if B > G:
    print("Bat")
else:
    print("Glove")



###B
def trees(A, M, L, R):
    def custom_ceiling(numerator, denominator):
        return numerator // denominator + (1 if numerator % denominator != 0 else 0)

    def custom_floor(numerator, denominator):
        return numerator // denominator

    first_position = A + custom_ceiling(L - A, M) * M
    last_position = A + custom_floor(R - A, M) * M

    if first_position > last_position:
        return 0
    else:
        return (last_position - first_position) // M + 1


A, M, L, R = map(int, input().split())

print(trees(A, M, L, R))


###C
N, K = map(int, input().split())
A = list(map(int, input().split()))

def min_s(N, K, A):

    # If the number of pairs is even, pair adjacent colors
    if (2 * N - K) % 2 == 0:
        weirdness = sum(A[i + 1] - A[i] for i in range(0, K - 1, 2))
        return weirdness

    # If the number of pairs is odd, try removing each color and pair the rest
    min_weirdness = float('inf')
    for i in range(K):
        # Remove one color and calculate weirdness
        weirdness = 0
        for j in range(K):
            if j != i:
                if j % 2 == 0:
                    if j + 1 < K and (i != j + 1):
                        weirdness += A[j + 1] - A[j]
                else:
                    if j - 1 >= 0 and (i != j - 1):
                        weirdness += A[j] - A[j - 1]

        min_weirdness = min(min_weirdness, weirdness)

    return min_weirdness

print(min_s(N, K, A))

###D
def max_sleighs(N, Q, R, queries):
    R.sort()

    cum_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        cum_sum[i] = cum_sum[i - 1] + R[i - 1]

    answers = []
    for X in queries:
        low, high = 0, N
        while low < high:
            mid = (low + high + 1) // 2
            if cum_sum[mid] <= X:
                low = mid
            else:
                high = mid - 1
        answers.append(low)

    return answers

N, Q = map(int, input().split())
R = list(map(int, input().split()))
queries = []
for _ in range(Q):
    queries.append(int(input()))

ans = max_sleighs(N, Q, R, queries)
for i in range(Q):
    print(ans[i])


###E
from collections import deque

H, W = map(int, input().split())
grid = []
for _ in range(H):
    s = input()
    grid.append(s)

MOD = 998244353

def count_connected_components(grid, H, W):
    visited = [[False for _ in range(W)] for _ in range(H)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(start):
        queue = deque([start])
        visited[start[0]][start[1]] = True
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    components = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                bfs((i, j))
                components += 1

    return components

def expected_value_green_components(grid, H, W):
    # Convert grid rows to lists for mutability
    grid = [list(row) for row in grid]

    # Count the number of red cells and the initial number of green connected components
    red_cells = sum(row.count('.') for row in grid)
    initial_components = count_connected_components(grid, H, W)

    # Calculate the expected value
    expected_value = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                # Temporarily repaint the cell green
                grid[i][j] = '#'
                new_components = count_connected_components(grid, H, W)
                grid[i][j] = '.'

                # Add to the expected value
                delta = (new_components - initial_components) % MOD
                expected_value = (expected_value + delta) % MOD

    # Divide by the number of red cells, modulo 998244353
    return (expected_value * pow(red_cells, MOD - 2, MOD)) % MOD

print(expected_value_green_components(grid, H, W))


###F




