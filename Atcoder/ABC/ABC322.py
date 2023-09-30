
map(int, input().split())

list(map(int, input().split()))

###A
N = int(input())
S = input()
a = 'ABC'
for i in range(N-2):
    if S[i]+S[i+1]+S[i+2]==a:
        print(i+1)
        exit()
print(-1)


###B
N, M = map(int, input().split())
S = input()
T = input()
if S == T[:N] and S == T[M-N:]:
    print(0) 
elif S == T[:N]:
    print(1)
elif S == T[M-N:]:
    print(2)
else:
    print(3)


###C
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [False]*(N+1)
for i in range(M):
    B[A[i]] = True
result = []
for i in range(N, 0, -1):
    if B[i]==True:
        result.append(0)
        tmp = i
    elif B[i]==False:
        result.append(tmp-i)
for i in range(N):
    print(result[N-i-1])


###D
def get_positions(polyomino):
    positions = set()
    for i, row in enumerate(polyomino):
        for j, cell in enumerate(row):
            if cell == "#":
                positions.add((i, j))
    return positions

def translate_to_origin(positions):
    min_x = min(x for x, y in positions)
    min_y = min(y for x, y in positions)
    return {(x - min_x, y - min_y) for x, y in positions}

def rotate_90(positions):
    return {(y, -x) for x, y in positions}

def check_collision(pos1, pos2):
    return bool(pos1 & pos2)

def is_valid_placement(polyominoes):
    total_cells = sum(len(poly) for poly in polyominoes)
    if total_cells != 16:
        return False

    all_positions = set().union(*polyominoes)
    if len(all_positions) != total_cells:
        return False

    max_x = max(x for x, y in all_positions)
    max_y = max(y for x, y in all_positions)
    min_x = min(x for x, y in all_positions)
    min_y = min(y for x, y in all_positions)

    if max_x >= 4 or max_y >= 4 or min_x < 0 or min_y < 0:
        return False

    for x in range(4):
        for y in range(4):
            if (x, y) not in all_positions:
                return False

    return True

def can_fill_grid(polyominoes):
    for _ in range(4):
        polyominoes[0] = rotate_90(polyominoes[0])
        for _ in range(4):
            polyominoes[1] = rotate_90(polyominoes[1])
            for _ in range(4):
                polyominoes[2] = rotate_90(polyominoes[2])
                for x1 in range(4):
                    for y1 in range(4):
                        pos1 = {(x+x1, y+y1) for x, y in polyominoes[0]}
                        for x2 in range(4):
                            for y2 in range(4):
                                pos2 = {(x+x2, y+y2) for x, y in polyominoes[1]}
                                for x3 in range(4):
                                    for y3 in range(4):
                                        pos3 = {(x+x3, y+y3) for x, y in polyominoes[2]}
                                        if is_valid_placement([pos1, pos2, pos3]):
                                            return True
    return False

polys = []
for _ in range(3):
    a =  [ input() for _ in range(4)]
    polys.append(a)

poly_positions = [translate_to_origin(get_positions(poly)) for poly in polys]

if can_fill_grid(poly_positions):
    print("Yes")
else:
    print("No")


###E
N, K, P = map(int, input().split())
plans = [list(map(int, input().split())) for _ in range(N)]
dp = {(0,)*K: 0}

def cost_goal(N, K, P, plans):
    dp = {(0,)*K: 0}

    for i in range(N):
        cost, *values = plans[i]
        values += [0] * (K - len(values))
        
        new_dp = dp.copy()
        for params, current_cost in dp.items():
            new_params = tuple(min(P, params[j] + values[j]) for j in range(K))
            new_dp[new_params] = min(new_dp.get(new_params, float('inf')), current_cost + cost)
        dp = new_dp

    return dp.get((P,)*K, -1)

print(cost_goal(N, K, P, plans))

