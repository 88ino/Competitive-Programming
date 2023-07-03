#B16
N = int(input())
h = list(map(int, input().split()))

dp = [0]*(N+1)
dp[1] = 0
dp[2] = abs(h[1]-h[0])
for i in range(3, N+1):
    dp[i] = min( dp[i-1] + abs(h[i-1]-h[i-2]), dp[i-2] + abs(h[i-1]- h[i-3]) )

print(dp[N])

#B17
N = int(input())
h = list(map(int, input().split()))

dp = [0]*(N+1)
dp[1] = 0
dp[2] = abs(h[0]-h[1])
for i in range(3, N+1):
    dp[i] = min( dp[i-1] + abs(h[i-1]-h[i-2]), dp[i-2] + abs(h[i-1]- h[i-3]) )

ans = []
Place = N
while True:
    ans.append(Place)
    if Place == 1:
        break

    if dp[Place] == dp[Place-1] + abs(h[Place-1]-h[Place-2]):
        Place -= 1
    else:
        Place -= 2

ans.reverse()
ans_s = [str(i) for i in ans]
print(len(ans_s))
print(" ".join(ans_s))

#B18
N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [ [None]*(S+1) for _ in range(N+1) ]
dp[0][0] = True
for j in range(1, S+1):
    dp[0][j] = False

for i in range(1, N+1):
    for j in range(S+1):

        if j - A[i-1] >= 0:
            if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

        elif j - A[i-1] < 0:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[N][S] == False:
    print(-1)
    exit()

ans = []
place = S
for i in range(N, 0, -1):
    #i-1番目がFalse → 合計がplaceから動いている → i-1番目のカードを選んでいる
    if dp[i-1][place] == False:
        place -= A[i-1]
        ans.append(i)

ans.reverse()
ans_r = [str(i) for i in ans]
print(len(ans_r))
print(' '.join(ans_r))

#B19
N, W = map(int, input().split())
w = [None]*(N+1)
v = [None]*(N+1)
for i in range(1, N+1):
    w[i], v[i] = map(int, input().split())

dp = [ [10**15]*(100001) for _ in range(N+1) ]
dp[0][0] = 0
for i in range(1, N+1):
    for j in range(100001):
        if j < v[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min( dp[i-1][j], dp[i-1][j-v[i]]+w[i] )
ans = 0
for i in range(100001):
    if dp[N][i] <= W:
        ans = i

print(ans)

#B20
S = input()
T = input()

dp = [ [None]*(len(T)+1) for _ in range(len(S)+1) ]
dp[0][0] = 0

for i in range(len(S)+1):
    for j in range(len(T)+1):
        if S[i-1] == T[j-1] and i >= 1 and j >= 1:
            dp[i][j] = min( dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] )
        elif i >= 1 and j >= 1:
            dp[i][j] = min( dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1 )
        elif i >= 1:
            dp[i][j] = dp[i-1][j] + 1
        elif j >= 1:
            dp[i][j] = dp[i][j-1] + 1

print(dp[len(S)][len(T)])

#B21
N = int(input())
S = input()

dp = [ [None]*(N) for _ in range(N) ]
for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    if S[i] == S[i+1]:
        dp[i][i+1] = 2
    else:
        dp[i][i+1] = 1

for LEN in range(2, N):
    for l in range(N-LEN):
        r = l + LEN
        if S[l] == S[r]:
            dp[l][r] = max(dp[l+1][r], dp[l][r-1], dp[l+1][r-1] + 2)
        else:
            dp[l][r] = max(dp[l+1][r], dp[l][r-1])

print(dp[0][N-1])


#B22はない

#B23
N = int(input())
X = [None]*(N)
Y = [None]*(N)
for i in range(N):
    X[i], Y[i] = map(int, input().split())

def distance(xi, yi, xj, yj):
    return((xi-xj)**2 + (yi-yj)**2)**0.5

# dp[i][j] : すでに訪れた都市の集合i, 現在位置jのときの最小移動距離和
dp = [ [100000000.0]*N for _ in range(2**N)]
dp[0][0] = 0

for i in range(2**N):
    for j in range(N):
        if dp[i][j] < 100000000.0:

            for k in range(N):
                #iにkがまだないとき
                if (i//(2**k))%2 == 0:
                    dp[i+(2**k)][k] = min( dp[i+(2**k)][k], dp[i][j] + distance(X[j], Y[j], X[k], Y[k]) )
                    
print(dp[2**N-1][0])

#B24
import bisect

N = int(input())
X = [None]*N
Y = [None]*N
for i in range(N):
    X[i], Y[i] = map(int, input().split())


#Xが同じ時を考慮して、XでソートしてYについては降の順にする
tmp = []
for i in range(N):
    tmp.append( (X[i], -Y[i]) )
tmp.sort()

#Xの昇の順になったYの最長増加部分列を考える
A = []
for i in range(N):
    A.append(-tmp[i][1])

LEN = 0
L = []
for i in range(N):
    pos = bisect.bisect_left(L, A[i])
    if pos == LEN:
        L.append(A[i])
        LEN += 1
    else:
        L[pos] = A[i]

print(LEN)