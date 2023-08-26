###A

N, H, X = map(int, input().split())
P = list(map(int, input().split()))
for i in range(N):
    if H + P[i] >= X:
        print(i+1)
        exit()



###B

N = int(input())
A = list(map(int, input().split()))
A.sort()
num = set([i + A[0] for i in range(N+1)])
A = set(A)
ans = num-A
print(ans.pop())




###C
import sys
sys.setrecursionlimit(100)

def dfs(node, visited, graph, distance):
    visited[node] = True
    max_distance = distance
    
    for neighbor, road_length in graph[node]:
        if not visited[neighbor]:
            max_distance = max(max_distance, dfs(neighbor, visited, graph, distance + road_length))
    
    visited[node] = False
    return max_distance

def find_longest_path(N, M, roads):
    # Create graph using adjacency list
    graph = {i: [] for i in range(1, N+1)}
    for a, b, c in roads:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    max_path_length = 0
    for i in range(1, N+1):
        visited = [False] * (N + 1)
        max_path_length = max(max_path_length, dfs(i, visited, graph, 0))
    
    return max_path_length


N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]
ans = find_longest_path(N, M, roads)
print(ans)


##

from itertools import permutations

def find_longest_path_bitdp(N, M, roads):
    # Mapping from (a, b) to distance
    distance_map = {(a, b): c for a, b, c in roads}
    distance_map.update({(b, a): c for a, b, c in roads})

    # Initialize DP table with -inf
    dp = [[-float('inf')] * (N + 1) for _ in range(1 << N)]
    for v in range(1, N + 1):
        dp[1 << (v - 1)][v] = 0

    # Update DP table
    for S in range(1 << N):
        for u in range(1, N + 1):
            if not (S & (1 << (u - 1))):
                continue
            for v in range(1, N + 1):
                if (S & (1 << (v - 1))) or not ((u, v) in distance_map):
                    continue
                dp[S | (1 << (v - 1))][v] = max(dp[S | (1 << (v - 1))][v], dp[S][u] + distance_map[(u, v)])
                
    return max(max(row) for row in dp)

N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]
ans = find_longest_path_bitdp(N, M, roads)

print(ans)

###D

def backtrack(election_data_sorted, idx, seats_gained, swaps_made, seats_needed):
    if idx == len(election_data_sorted):
        return float('inf') if seats_gained < seats_needed else swaps_made
    
    # If the seats gained already exceeds the needed seats, return the swaps made
    if seats_gained >= seats_needed:
        return swaps_made

    # Current district data
    swap_cost, seats, efficiency = election_data_sorted[idx]

    # Option 1: Not considering the current district
    option1 = backtrack(election_data_sorted, idx + 1, seats_gained, swaps_made, seats_needed)

    # Option 2: Considering the current district
    option2 = backtrack(election_data_sorted, idx + 1, seats_gained + seats, swaps_made + swap_cost, seats_needed)

    return min(option1, option2)

def min_swaps_to_win_backtrack(N, election_data):
    total_seats = sum(x[2] for x in election_data)
    needed_seats = total_seats // 2 + 1
    takahashi_initial_seats = sum(x[2] for x in election_data if x[0] > x[1])
    
    # If Takahashi already has the majority
    if takahashi_initial_seats >= needed_seats:
        return 0

    # Remaining seats needed
    seats_needed = needed_seats - takahashi_initial_seats

    # Calculate the swap costs and efficiency for each district
    swap_data = [((data[1] - data[0] + 1) // 2, data[2], (data[1] - data[0] + 1) // 2 / data[2]) for data in election_data if data[0] <= data[1]]

    # Sort by efficiency
    swap_data_sorted = sorted(swap_data, key=lambda x: x[2])

    # Backtracking to find the minimum swaps
    return backtrack(swap_data_sorted, 0, takahashi_initial_seats, 0, needed_seats)


N = int(input())
data = []
for _ in range(N):
    x, y, z = map(int, input().split())
    data .append((x, y, z))
result = min_swaps_to_win_backtrack(N, data)
print(result)





###E
from collections import deque

def mark_vision_v2(grid, H, W):
    vision_grid = [list(row) for row in grid]
    
    dirs = {
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
        '^': (-1, 0)
    }

    for i in range(H):
        for j in range(W):
            if grid[i][j] in dirs:
                dx, dy = dirs[grid[i][j]]
                x, y = i + dx, j + dy
                while 0 <= x < H and 0 <= y < W and grid[x][y] not in ['#', '>', 'v', '<', '^', 'S', 'G']:
                    vision_grid[x][y] = '#'
                    x += dx
                    y += dy

    return vision_grid

def bfs_shortest_path_v2(vision_grid, H, W):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    start, goal = None, None
    for i in range(H):
        for j in range(W):
            if vision_grid[i][j] == 'S':
                start = (i, j)
            if vision_grid[i][j] == 'G':
                goal = (i, j)
    
    visited = [[False] * W for _ in range(H)]
    queue = deque([(start, 0)]) 

    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == goal:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and vision_grid[nx][ny] not in ['#', '>', 'v', '<', '^']:
                visited[nx][ny] = True
                queue.append(((nx, ny), dist + 1))
    
    return -1  

H, W = map(int, input().split())
grid = [input() for _ in range(H)]
marked_grid_v2 = mark_vision_v2(grid, H, W)
result_v2 = bfs_shortest_path_v2(marked_grid_v2, H, W)
print(result_v2)

