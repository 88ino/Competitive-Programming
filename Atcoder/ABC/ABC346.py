
map(int, input().split())

int(input())

###A
N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N-1):
    B.append(A[i]*A[i+1])
print(*B)


###B
def substring(W, B):
    pattern = "wbwbwwbwbwbw" * 20  
    cumulative_sum = [0] * (len(pattern) + 1)
    for i in range(1, len(pattern) + 1):
        cumulative_sum[i] = cumulative_sum[i - 1] + (1 if pattern[i - 1] == 'w' else 0)

    for i in range(len(pattern)):
        for j in range(i, len(pattern)):
            w_count = cumulative_sum[j + 1] - cumulative_sum[i]
            b_count = (j - i + 1) - w_count
            if w_count == W and b_count == B:
                return "Yes"
    return "No"

W, B = map(int, input().split())
print(substring(W, B))



###C
def missing_numbers(N, K, A):
    numbers_in_A = set([a for a in A if 1 <= a <= K])

    total_sum = K * (K + 1) // 2

    sum_in_A = sum(numbers_in_A)

    return total_sum - sum_in_A

N, K = map(int, input().split())
A = list(map(int, input().split()))
print(missing_numbers(N, K, A))


###D
def min_cost_s(N, S, C):
    cum_cost_10 = [0] * (N + 1)
    cum_cost_01 = [0] * (N + 1)
    for i in range(N):
        cum_cost_10[i + 1] = cum_cost_10[i] + (C[i] if S[i] != '10'[i % 2] else 0)
        cum_cost_01[i + 1] = cum_cost_01[i] + (C[i] if S[i] != '01'[i % 2] else 0)

    # 一カ所だけ隣り合う文字が等しくなる場所を全探索
    min_cost = float('inf')
    for i in range(N - 1):
        # 隣り合う文字が00になる場合
        cost_b = cum_cost_10[i] if i % 2 == 1 else cum_cost_01[i]
        cost_a = cum_cost_01[N] - cum_cost_01[i + 2] if i % 2 == 1 else cum_cost_10[N] - cum_cost_10[i + 2]
        cost_00 = cost_b + cost_a
        if S[i] == '1':
            cost_00 += C[i]
        if S[i + 1] == '1':
            cost_00 += C[i + 1]

        # 隣り合う文字が11になる場合
        cost_b = cum_cost_10[i] if i % 2 == 0 else cum_cost_01[i]
        cost_a = cum_cost_01[N] - cum_cost_01[i + 2] if i % 2 == 0 else cum_cost_10[N] - cum_cost_10[i + 2]
        cost_11 = cost_b + cost_a
        if S[i] == '0':
            cost_11 += C[i]
        if S[i + 1] == '0':
            cost_11 += C[i + 1]

        min_cost = min(min_cost, cost_00, cost_11)

    return min_cost

N = int(input())
S = input()
C = list(map(int, input().split()))
print(min_cost_s(N, S, C))



###E
from collections import defaultdict

H, W, M = map(int, input().split())
operations = [list(map(int, input().split())) for _ in range(M)]

row_colors = defaultdict(int)
col_colors = defaultdict(int)

color_count = defaultdict(int)

for T, A, X in reversed(operations):
    if T == 1:  # 行の操作
        if row_colors[A] == 0:  # まだ塗られていない場合
            row_colors[A] = X
            color_count[X] += W - len(col_colors)  # 未塗装の列の数だけマスを塗る
    else:  # 列の操作
        if col_colors[A] == 0:  # まだ塗られていない場合
            col_colors[A] = X
            color_count[X] += H - len(row_colors)  # 未塗装の行の数だけマスを塗る

result = [(color, count) for color, count in color_count.items() if count > 0]
result.sort()
print(len(result))
for color, count in result:
    print(color, count)


