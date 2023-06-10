#A

N = int(input())

# スタート地点・ゴール地点と各給水所の位置を格納したリスト
water_stations = [0] + [5*i for i in range(1, 21)] + [100]

# 高橋くんがいる地点に最も近い給水所を求める
nearest_station = min(water_stations, key=lambda x: abs(x - N))

print(nearest_station)


#B
p, q = input().split()

def ret(x):
    if x == "A":
        return 0
    elif x == "B":
        return 1
    elif x == "C":
        return 2
    elif x == "D":
        return 3
    elif x == "E":
        return 4
    elif x == "F":
        return 5
    elif x == "G":
        return 6
A = [0, 3, 1, 4, 1, 5, 9]
pp = ret(p)
qq = ret(q)

a = 0
if pp > qq:
    a = pp
    pp = qq
    qq = a

B = [0]*8
for i in range(1, 8):
    B[i] = B[i-1] + A[i-1]

dis = B[qq+1]- B[pp+1]
print(dis)


#C
H, W = map(int, input().split())

grid = []
for _ in range(H):
    row = input().strip()
    grid.append(row)

# クッキーが置かれているマスを探索
for i in range(0, H):
    for j in range(0, W):
        if grid[i][j] == '.':
            if i != 0 and j != 0:
                if ( 
                    (grid[i - 1][j] == '#' and grid[i + 1][j] == '#')or
                    (grid[i - 1][j] == '#' and grid[i][j - 1] == '#')or
                    (grid[i - 1][j] == '#' and grid[i][j + 1] == '#')or
                    (grid[i + 1][j] == '#' and grid[i][j - 1] == '#')or
                    (grid[i + 1][j] == '#' and grid[i][j + 1] == '#')or
                    (grid[i][j - 1] == '#' and grid[i][j + 1] == '#')
                    ):
                        print(i+1, j+1)
                        exit()
            elif i == 0 and j !=0:
                if(
                    (grid[i + 1][j] == '#' and grid[i][j - 1] == '#')or
                    (grid[i + 1][j] == '#' and grid[i][j + 1] == '#')or
                    (grid[i][j - 1] == '#' and grid[i][j + 1] == '#')
                    ):
                        print(i+1, j+1)
                        exit()
            elif i != 0 and j ==0:
                if(                    
                    (grid[i - 1][j] == '#' and grid[i + 1][j] == '#')or
                    (grid[i - 1][j] == '#' and grid[i][j + 1] == '#')or
                    (grid[i + 1][j] == '#' and grid[i][j + 1] == '#')
                    ):
                        print(i+1, j+1)
                        exit()
            elif i==0 and j==0:
                 if grid[i + 1][j] == '#' and grid[i][j + 1] == '#':
                    print(i+1, j+1)
                    exit()
####
H, W = map(int, input().split())

grid = []
for _ in range(H):
    row = list(input().strip())
    grid.append(row)

min_i, min_j, max_i, max_j = H - 1, W - 1, 0, 0

# クッキーが置かれているマスの最小と最大の行と列を見つける
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)

# クッキーが置かれていた部分長方形内で、'.'のマスを見つける
for i in range(min_i, max_i + 1):
    for j in range(min_j, max_j + 1):
        if grid[i][j] == '.':
            print(i + 1, j + 1)
            exit()
###

#D

import bisect

def sleep_duration(N, A, Q, queries):
    # 睡眠時間の累積和を計算
    cum_sleep = [0]*(N+1)
    for i in range(2, N+1, 2):
        cum_sleep[i] = cum_sleep[i-2] + (A[i-1] - A[i-2])

    # 各クエリに対して答えを求める
    results = []
    for l, r in queries:
        # 寝る時間と起きる時間を二分探索で見つける
        sleep_time = bisect.bisect_right(A, l-1)
        wake_time = bisect.bisect_right(A, r)

        # 睡眠時間を累積和から計算
        sleep_duration = cum_sleep[wake_time] - cum_sleep[sleep_time]

        # 睡眠時間がクエリの区間をはみ出していたら調整する
        if sleep_time % 2 == 0 and l > A[sleep_time-1]:
            sleep_duration -= l - A[sleep_time-1]
        if wake_time % 2 == 0 and r < A[wake_time-1]:
            sleep_duration += A[wake_time-1] - r

        results.append(sleep_duration)

    return results

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

print(sleep_duration(N, A, Q, LR))




















