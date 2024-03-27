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
N = int(input())
a = set(i for i in range(1, 2*N+2))
print(a.pop(), flush=True)
for _ in range(N):
    aoki = int(input())
    a.remove(aoki)
    print(a.pop(), flush=True)


# 245
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
fa = True
fb = True
for i in range(N-1):
    a, aa = A[i], A[i+1]
    b, bb = B[i], B[i+1]
    if (fa == True and abs(a-aa) <= K )or (fb == True and abs(b-aa) <= K):
        fat = True
    else:
        fat = False
    if (fa == True and abs(a-bb) <= K )or (fb == True and abs(b-bb) <= K):
        fbt = True
    else:
        fbt = False
    fa, fb = fat, fbt

    if fa==False and fb == False:
        print("No")
        exit()
print("Yes")


# 246
N, K, X = map(int, input().split())
A = list(map(int, input().split()))
ku = sum(A[i]//X for i in range(N))
if ku > K:
    print(sum(A)-K*X)
    exit()
B = [A[i]%X for i in range(N)] 
B.sort(reverse=True)
count = K-ku
a = sum(B[:count])
print(sum(A)-X*ku-a)


# 247
def S(sb, n):
    return sb + [n] + sb
N = int(input())
Sn = [1]
for i in range(1, N):
    Sn = S(Sn, i+1)
print(*Sn)


# 248
N, M, K = map(int, input().split())
Mod = 998244353
dp = [ [0]*(N*M+1) for _ in range(N+1) ]
dp[0][0] = 1
for i in range(N):
    for j in range(K):
        for k in range(1, M+1):
            if j+k <= K:
                dp[i+1][j+k] += dp[i][j] 
ans = sum(dp[N])
print(ans%Mod)


# 249
import itertools
from collections import Counter

N, K = map(int, input().split())
S = [input() for _ in range(N)]
a = [i for i in range(1, 17)]
c = []
for i in range(K, N+1):
    c.append(itertools.combinations(S, i))
ans = 0
for cc in c:
    for k in cc:
        count = Counter()
        for kk in k:
            count += Counter(kk)
        m = 0
        key = count.keys()
        for i in key:
            if count[i] == K:
                m += 1
        ans = max(ans, m)

print(ans)

        
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



