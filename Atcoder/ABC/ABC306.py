
##A##

N = int(input().strip())  # 文字列の長さを取得
S = input().strip()  # 文字列を取得

result = ''.join([s * 2 for s in S])

print(result)  # 結果を出力





##B##

A = list(map(int, input().split()))
ans = 0
for i in range(0, 64):
    ans += A[i]*2**i
print(ans)









##C##


N = int(input().strip())  # 数列の要素数を取得
A = list(map(int, input().split()))  # 数列を取得

# 空の辞書を用意
index_dict = {}

# 数列を左から順に走査
for i in range(3*N):
    if A[i] not in index_dict:  # 現在の要素が辞書に存在しない場合
        index_dict[A[i]] = [i]  # 新たにキーを追加し、その値として現在のインデックスを追加
    else:  # 現在の要素が辞書にすでに存在する場合
        index_dict[A[i]].append(i)  # その値のリストに現在のインデックスを追加

# 各キーに対して、真ん中のインデックス（リストの2番目の要素）を取り出す
middle_indices = [(k, v[1]) for k, v in index_dict.items()]

# 真ん中のインデックスを元に数列をソート
middle_indices.sort(key=lambda x: x[1])

# ソートされた数列を出力
for i in middle_indices:
    print(i[0], end=' ')


####C
N = int(input())  
A = list(map(int, input().split())) 
c = [0]*(N+1)
ans = []
for x in A:
    c[x] += 1
    if c[x] == 2:
        ans.append(x)
print(' '.join(map(str, ans)))





##D##


N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

dp = [[0]*2 for _ in range(N+1)]

dp[0][0] = 0 #健康
dp[0][1] = 0 #毒状態

for i in range(1, N+1):

    #まずi番目を食べないときを考える
    dp[i][0] = dp[i-1][0]
    dp[i][1] = dp[i-1][1]

    #i番目を食べる場合を考え、食べない場合と比較する
    if X[i-1]==0:
        #健康状態になる
        #前が健康で食べるか毒で食べるか
        dp[i][0] = max( dp[i][0], dp[i-1][0]+Y[i-1] )
        dp[i][0] = max( dp[i][0], dp[i-1][1]+Y[i-1] )

    elif X[i-1]==1:
        #毒状態になる
        #前が健康のとき
        dp[i][1] = max( dp[i][1], dp[i-1][0]+Y[i-1] )
    
print( max(dp[N]) )








N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
dp = [[0] * 3 for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N + 1, -1, 0):
    if X[i - 1] == 0:
        # 食べない場合
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        # 解毒剤入りの料理を食べる場合
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + Y[i - 1]
        # 毒入りの料理を食べる場合
        dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
    elif X[i - 1] == 1:
        # 食べない場合
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        # 解毒剤入りの料理を食べる場合
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2])
        # 毒入りの料理を食べる場合
        dp[i][2] = max(dp[i - 1][1], dp[i - 1][2]) + Y[i - 1]

print(max(dp[N]))




N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

dp = [0] * (N + 1)
Safe = True

for i in range(N - 1, -1, -1):
    if X[i] == 0:
        if Safe:
            if Y[i] >= 0:
                dp[i] = dp[i] + Y[i]
            else:
                dp[i] = dp[i + 1]
        else:
            dp[i] = dp[i + 1] + Y[i]
            Safe = True
    elif X[i] == 1:
        if Safe:
            if Y[i] > 0:
                dp[i] = dp[i + 1] + Y[i]
                Safe = False
            else:
                dp[i] = dp[i + 1]
        else:
            dp[i] = dp[i + 1]

print(dp[0])




######








