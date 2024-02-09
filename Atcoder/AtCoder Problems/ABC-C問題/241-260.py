# 241
from turtle import ycor


def cal(x, y, dx, dy):
    count = 0
    for i in range(6):
        if min(x, y) < 0 or max(x, y) >= N:
            return  False
        if S[x][y] == "#":
            count += 1
        x += dx
        y += dy

    return count >= 4

N = int(input())
S = [input() for _ in range(N)]
direction = [(0, 1), (1, 0), (1, 1), (-1, 1)]
for a in direction:
    dx, dy = a
    for x in range(N):
        for y in range(N):
            if cal(x, y, dx, dy):
                print("Yes")
                exit()
print("No")


# 242
N = int(input())
M = 998244353
dp = [ [0]*11 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1
for n in range(1, N):
    for k in range(1, 10):
        dp[n+1][k] = dp[n][k-1] + dp[n][k] + dp[n][k+1]
        dp[n+1][k] %= M
print(sum(dp[N][k] for k in range(1, 10))%M)


# 243
N = int(input())
p = []
for i in range(N):
    x, y = map(int, input().split())
    p.append((x, y))
S = input()

max_left = dict()
min_right = dict()
for i in range(N):
    x, y = p[i]
    if S[i] == "R":
        if y in max_left and x < max_left[y]:
            print("Yes")
            exit()
        elif y in min_right:
            min_right[y] = min(x, min_right[y])
        else:
            min_right[y] = x

    if S[i] == "L":
        if y in min_right and min_right[y] < x:
            print("Yes")
            exit()
        elif y in max_left:
            max_left[y] = max(x, max_left[y])
        else:
            max_left[y] = x
print("No")


# 244



# 245



# 246



# 247



# 248



# 249



# 250



# 251



# 252



# 253



# 254



# 255



# 256



# 257



# 258



# 259



# 260



