"""


 = map(int, input().split())

 = int(input())

"""

###A###

S = list(map(int, input().split()))
for i in range(8):
    if S[i]%25 != 0:
        print("No")
        exit()
    if not(100 <= S[i] <= 675):
        print("No")
        exit()
    for j in range(i+1, 8):
        if S[i] > S[j]:
            print("No")
            exit()
print("Yes")




###B###
N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))

color_to_price = {color: price for color, price in zip(D, P[1:])}
color_to_price['default'] = P[0]

total = 0
for color in C:
    total += color_to_price.get(color, color_to_price['default'])

print(total)





###C###
N = int(input())
A = []*(N)
B = []*(N)
for i in range(N):
    A[i], B[i] = map(int, input().split())

def cal(a, b):
    return a*10**10 // (a+b) , a*10**10 % (a+b)

for i in range(N):
    sho, amari = cal(A[i], B[i])



##

N = int(input().strip())
players = []
for i in range(N):
    A, B = map(int, input().strip().split())
    players.append((A, A+B, i+1))

players.sort(key=lambda x: (-x[0]/x[1], x[2]))

for player in players:
    print(player[2], end=' ')


###D###

def dfs(grid, visited, i, j, k):
    # マス (i, j) が範囲外であるか、すでに訪れたことがある場合は終了
    if i < 0 or i >= H or j < 0 or j >= W :
        return False
    
    # マス (i, j) の文字が "snuke" の k 文字目に一致するか確認
    if grid[i][j] == "snuke"[k]:
        # 目的地に到達した場合は成功
        if k == 4 and i == H - 1 and j == W - 1:
            return True
        
        # マス (i, j) を訪れたとマークし、次の移動を試す
        visited[i][j] = True
        
        # 上下左右のマスに対して再帰的に探索を行う
        if dfs(grid, visited, i - 1, j, (k + 1) % 5) or dfs(grid, visited, i + 1, j, (k + 1) % 5) \
            or dfs(grid, visited, i, j - 1, (k + 1) % 5) or dfs(grid, visited, i, j + 1, (k + 1) % 5):
            return True
        
        # マス (i, j) の探索が終了したら未訪問に戻す
        visited[i][j] = False
    
    return False


# 入力を受け取る
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# 訪問済みマスを管理する配列
visited = [[False] * W for _ in range(H)]

# (1, 1) からスタートして深さ優先探索を実行
result = dfs(grid, visited, 0, 0, 0)

# 結果を出力する
if result:
    print("Yes")
else:
    print("No")





###E###








###F###





