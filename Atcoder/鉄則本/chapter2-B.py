#B6
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

sum_A = [0]*(N+1)
for i in range(0, N):
    sum_A[i+1] = sum_A[i] + A[i]

for i in range(Q):
    L, R = map(int, input().split())
    atari = sum_A[R] - sum_A[L-1]
    hazure = (R-L+1)-atari
    if atari > hazure:
        print("win")
    elif atari == hazure:
        print("draw")
    else:
        print("lose")

#B7
T = int(input())
N = int(input())
L = [None]*(N)
R = [None]*(N)
for i in range(N):
    L[i], R[i] = map(int, input().split())

num = [0]*(T+1)
for i in range(N):
    num[L[i]] += 1
    num[R[i]] -= 1

sum_n = [0]*(T+1)
sum_n[0] = num[0]
for i in range(1, T+1):
    sum_n[i] = sum_n[i-1] + num[i]

for i in range(T):
    print(sum_n[i])

#B8
N = int(input())
X = [None]*(N)
Y = [None]*(N)
for i in range(N):
    X[i], Y[i] = map(int, input().split())
Q = int(input())
question = [ list(map(int, input().split())) for _ in range(Q) ]

S = [ [0]*(1501) for _ in range(1501) ]
for i in range(N):
    S[X[i]][Y[i]] += 1

T = [ [0]*(1501) for _ in range(1501) ]
for i in range(1, 1501):
    for j in range(1, 1501):
        T[i][j] = T[i][j-1] + S[i][j]

for j in range(1, 1501):
    for i in range(1, 1501):
        T[i][j] += T[i-1][j]

for a, b, c, d in question:
    ans = T[c][d]-T[c][b-1]-T[a-1][d]+T[a-1][b-1]
    print(ans)

#B9
N = int(input())
A = [None]*(N)
B = [None]*(N)
C = [None]*(N)
D = [None]*(N)
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

T = [ [0]*(1501) for _ in range(1501) ]
for i in range(N):
    T[A[i]][B[i]] += 1
    T[A[i]][D[i]] -= 1
    T[C[i]][B[i]] -= 1
    T[C[i]][D[i]] += 1    

for i in range(0, 1501):
    for j in range(1, 1501):
        T[i][j] += T[i][j-1]

for j in range(0, 1501):
    for i in range(1, 1501):
        T[i][j] += T[i-1][j]

Ans = 0
for i in range(1501):
    for j in range(1501):
        if T[i][j] >= 1:
            Ans += 1

print(Ans)