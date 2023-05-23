#26
Q = int(input())
X = [0]*Q
for i in range(Q):
    X[i] = int(input())

def check(x):
    Y = int(x**0.5)
    for i in range(2, Y+1):
        if x%i == 0:
            return False
    return True

for i in range(Q):
    if check(X[i])==True:
        print("Yes")
    else:
        print("No")

#27
A, B = map(int, input().split())

C = max(A, B)
D = min(A, B)
while C!=0 and D!=0:
    E = C%D
    C = D
    D = E
print(C)

#28
N = int(input())
T = [None]*N
A = [None]*N
for i in range(N):
    T[i], A[i] = input().split()
    A[i] = int(A[i])

M = 0
for i in range(N):
    if T[i] == '+':
        M += A[i]
    elif T[i] == '-':
        M -= A[i]
    else:
        M *= A[i]
    
    if M < 0:
        M += 10000
    M = M%10000
    print(M)

#29
a, b = map(int, input().split())

def power(a, b, m):
    p = a
    Ans = 1
    for i in range(30):
        wari = 2**i
        if (b//wari)%2 == 1:
            Ans = (Ans*p)%m
        p = (p*p)%m
    return Ans

print(power(a, b, 10**9+7))

#30
n, r = map(int, input().split())

# a^bをmで割った余りを求める関数
def power(a, b, m):
    p = a
    Ans = 1
    for i in range(30):
        wari = 2**i
        if (b//wari)%2 == 1:
            Ans = (Ans*p)%m
        p = (p*p)%m
    return Ans

# x!をmで割った余りを求める関数
def kaijou(x, M):
    a = 1
    for i in range(1, x+1):
        a *= i
        a %= M
    return a

# a/bをmで割った余りを求める関数
def div(a, b, m):
    return ( (a*power(b, m-2, m))%m )

M = 10**9 + 7
a = kaijou(n, M)
b = kaijou(r, M)*kaijou(n-r, M)
print(div(a, b, M))

#31
N = int(input())
print(N//3 + N//5 - N//15)
    
#32
N, A, B = map(int, input().split())
dp = [None]*(N+1)

for i in range(N+1):
    if i>=A and dp[i-A]==False:
        dp[i] = True
    elif i>=B and dp[i-B]==False:
        dp[i] = True
    else:
        dp[i] = False

if dp[N] == True:
    print("First")
else:
    print("Second")

#33
N = int(input())
A = list(map(int, input().split()))

XOR = A[0]
for i in range(1, N):
    XOR = XOR^A[i]

if XOR == 0:
    print("Second")
else:
    print("First")

#34
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

grundy = [None]*(100001)
for i in range(100001):
    Trans = [False, False, False]
    if i >= X:
        Trans[grundy[i-X]] = True
    if i >= Y:
        Trans[grundy[i-Y]] = True
    if Trans[0] == False:
        grundy[i] = 0
    elif Trans[1] == False:
        grundy[i] = 1
    else:
        grundy[i] = 2

XOR = 0
for i in range(N):
    XOR = XOR^grundy[A[i]]

if XOR == 0:
    print("Second")
else:
    print("First")

#35
N = int(input())
A = list(map(int, input().split()))

dp = [[None]*(N+1) for _ in range(N+1)]

for j in range(1, N+1):
    dp[N][j] = A[j-1]

for i in range(N-1, 0, -1):
    for j in range(1, i+1):
        if i%2 == 1:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
        else:
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])
print(dp[1][1])

