
map(int, input().split())

###A

def arrow(s):
    return s[0] == '<' and s[-1] == '>' and all(c == '=' for c in s[1:-1])

S = input()
print('Yes') if arrow(S) else print('No')


###B
import math

def ceil_divide(X):
    return -(-X // 10)

X = int(input())
print(ceil_divide(X))



###C
from collections import Counter

def count_swap(S):
    total = 0
    N = len(S)
    char_counts = Counter(S)
    a = N
    for count in char_counts.values():
        a -= count
        total += count*a
    if max(char_counts.values()) >= 2:
        total += 1

    return total

S = input()
print(count_swap(S))


###D
from itertools import combinations

def find_valid_tile_combinations(tiles, H, W):
    valid_combinations = []
    for r in range(1, len(tiles) + 1):
        for combo in combinations(tiles, r):
            if sum(a * b for a, b in combo) == H * W:
                valid_combinations.append(combo)
    return valid_combinations

def find_next_empty_cell(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return None

def can_place_tile(grid, tile, x, y):
    h, w = tile
    for i in range(h):
        for j in range(w):
            if x + i >= len(grid) or y + j >= len(grid[0]) or grid[x + i][y + j] != 0:
                return False
    return True

def place_tile(grid, tile, x, y):
    h, w = tile
    for i in range(h):
        for j in range(w):
            grid[x + i][y + j] = 1

def remove_tile(grid, tile, x, y):
    h, w = tile
    for i in range(h):
        for j in range(w):
            grid[x + i][y + j] = 0

def solve(grid, tiles, index):
    if index == len(tiles):
        return all(all(cell == 1 for cell in row) for row in grid)

    next_cell = find_next_empty_cell(grid)
    if next_cell is None:
        return False

    x, y = next_cell
    for i in range(index, len(tiles)):
        for orientation in [(tiles[i][0], tiles[i][1]), (tiles[i][1], tiles[i][0])]:
            if can_place_tile(grid, orientation, x, y):
                place_tile(grid, orientation, x, y)
                if solve(grid, tiles[:i] + tiles[i+1:], 0):
                    return True
                remove_tile(grid, orientation, x, y)
    return False

def can_fill_grid_with_combination(H, W, combination):
    grid = [[0] * W for _ in range(H)]
    return solve(grid, list(combination), 0)

N, H, W = map(int, input().split())
tiles = []
for _ in range(N):
    a, b = map(int, input().split())
    tiles.append((a, b))

valid_combinations = find_valid_tile_combinations(tiles, H, W)

for combo in valid_combinations:
    if can_fill_grid_with_combination(H, W, combo):
        print("Yes")
        break
else:
    print("No")


###E
N, K = map(int, input().split())
balls = [tuple(map(int, input().split())) for _ in range(N)]

groups = []
for color, value in balls:
    if groups and groups[-1][0] == color:
        groups[-1][1].append(value)
    else:
        groups.append((color, [value]))

remove_count = 0
total_value = 0
for color, values in groups:
    remove_count += len(values) - 1
    total_value += max(values)

if remove_count > K:
    print(-1)
else:
    # 残りのK - remove_count回で価値の合計を最大化
    additional_values = []
    for color, values in groups:
        additional_values.extend(sorted(values)[:-1])
    additional_values.sort(reverse=True)
    total_value += sum(additional_values[:K - remove_count])
    print(total_value)

