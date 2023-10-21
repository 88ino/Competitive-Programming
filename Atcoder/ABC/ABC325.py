
###A
S, T = input().split()
print(S, "san")




###B

N = int(input())
base = []
for _ in range(N):
    w, x = map(int, input().split())
    base.append((w, x))

def max_participants(N, bases):

    working_hours = []
    for W, X in bases:
        start = (9 + X) % 24
        end = (18 + X) % 24
        working_hours.append((W, start, end))

    max_count = 0
    
    for t in range(24):
        count = 0
        for W, start, end in working_hours:
    
            if start <= end:
                if start <= t < end:
                    count += W
            else:
                if t < end or start <= t:
                    count += W
        max_count = max(max_count, count)
    return max_count

print(max_participants(N, base))

###C
import sys
sys.setrecursionlimit(10**4)

H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            
    def get_unique_parents(self):
        roots = set()
        for i in range(len(self.parent)):
            roots.add(self.find(i))
        return roots


def count_sensors(H, W, grid):
    def get_index(r, c):
        return r * W + c

    uf = UnionFind(H * W)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for r in range(H):
        for c in range(W):
            if grid[r][c] == '#':
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '#':
                        uf.union(get_index(r, c), get_index(nr, nc))
                        
    sensors = set()
    for r in range(H):
        for c in range(W):
            if grid[r][c] == '#':
                sensors.add(uf.find(get_index(r, c)))
                
    return len(sensors)

print(count_sensors(H, W, grid))



###D

from heapq import heappush, heappop

N = int(input())
items = []
for _ in range(N):
    t, d = map(int, input().split())
    items.append((t, t+d))

def max_prints(N, items):
    items.sort(key=lambda x: x[1])
    count = 0
    time = items[0][0]
    for i in range(N):
        

print(max_prints(N, items))


###E
import heapq

def min_time(N, A, B, C, D):
    INF = float('inf')
    dist_car = [INF] * N
    dist_train = [INF] * N
    dist_car[0] = 0  
    
    Q = [(0, 0, True)]  
    
    while Q:
        cost, u, is_car = heapq.heappop(Q)
        
        if cost > dist_car[u] if is_car else cost > dist_train[u]:
            continue
        
        for v in range(N):
            if v != u:
                new_cost_car = cost + D[u][v] * A
                new_cost_train = cost + D[u][v] * B + C
                
                if is_car and new_cost_car < dist_car[v]:
                    dist_car[v] = new_cost_car
                    heapq.heappush(Q, (new_cost_car, v, True))
                    
                if new_cost_train < dist_train[v]:
                    dist_train[v] = new_cost_train
                    heapq.heappush(Q, (new_cost_train, v, False))
                    
                if is_car and new_cost_train < dist_train[v]:
                    dist_train[v] = new_cost_train
                    heapq.heappush(Q, (new_cost_train, v, False))
    
    return min(dist_car[-1], dist_train[-1])

N, A, B, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(N)]

print(min_time(N, A, B, C, D))


