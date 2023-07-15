
map(int, input().split())

list(map(int, input().split()))

[ [] for _ in range() ]

N = int(input())

###A
N, P , Q = map(int, input().split())
D = list(map(int, input().split()))
print(min(P, min(D)+Q))






###B

N, M =  map(int, input().split())
products = []
for _ in range(N):
    P, C, *F = map(int, input().split())
    products.append((P, set(F)))

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        Pi, Fi = products[i]
        Pj, Fj = products[j]

        if Pi >= Pj and Fi <= Fj and (Pi > Pj or Fi < Fj ):
            print("Yes")
            exit()
print("No")

        
###C
N = int(input().strip())
unique_strings = set()
for _ in range(N):
    S = input().strip()
    unique_strings.add(min(S, S[::-1]))
print(len(unique_strings))




###D
N, T, M = map(int, input().split())
C = []
for _ in range(M):
    a, b = map(int, input().split())
    C.append((a,b))

def stirling(n, k):
    if n == k == 0:
        return 1
    if n > 0 and k == 0:
        return 0
    if n == 0 and k > 0:
        return 0
    if k > n:
        return 0
    return k * stirling(n-1, k) + stirling(n-1, k-1)
total = stirling(N, T)
bad = 0

    
####


N, T, M = map(int, input().split())

pairs = []
for _ in range(M):
    a, b = map(int, input().split())
    pairs.append((a,b))
    
#i人目まで考慮してjチーム作る方法dp[i][j]
dp = [[0]*(T+1) for _ in range(N)]
for i in range(N):
    dp[i][0] = 0
    dp[i][1] = 1 if M==0 else 0
for j in range(T):
    dp[0][j] = 0

for i in range(1, N):
    for j in range(1, T+1):
        dp[i][j] = dp[i-1][j] # i番目の選手を新たなチームに所属させない場合
        dp[i][j] += dp[i-1][j-1] # i番目の選手を新たなチームに所属させる場合
        dp[i][j] %= (10**9 + 7)

print(dp[N-1][T])



###E






###F

N = int(input())
A = list(map(int, input().split()))
MOD = 998244353








