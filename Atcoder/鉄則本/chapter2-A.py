#6
N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = []
R = []
for i in range (Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
su = [0]*(N+1)

for i in range (N):
    su[i+1] = su[i] + A[i]

for j in range (Q):
    S = su[R[j]] - su[L[j]-1]
    print(S)

#7
D = int(input())
N = int(input())
L = [None]*N
R = [None]*N
for i in range (N):
    L[i], R[i] = map(int, input().split())

B = [0]*(D+2)
for i in range (N):
    B[L[i]] += 1
    B[R[i]+1] -= 1

Ans = [0]*(D+2)
for j in range(1, D+1):
    Ans[j] = Ans[j-1] +B[j]
    print(Ans[j])

#8
H, W = map(int, input().split())
X = [None]*H
for i in range (H):
    X[i] = list(map(int, input().split()))
Q = int(input())
A = [None]*Q
B = [None]*Q
C = [None]*Q
D = [None]*Q
for i in range(Q):
    A[i], B[i], C[i], D[i] =  map(int, input().split())

Z = [ [0]*(W+1) for i in range(H+1) ]

for i in range(1, H+1):
    for j in range(1, W+1):
        Z[i][j] = Z[i][j-1] + X[i-1][j-1]
for j in range (1, W+1):
    for i in range(1, H+1):
        Z[i][j] += Z[i-1][j]

for i in range(Q):
    print(Z[C[i]][D[i]]-Z[C[i]][B[i]-1]-Z[A[i]-1][D[i]]+Z[A[i]-1][B[i]-1])

#9
H, W, N = map(int, input().split())
A = [0]*N
B = [0]*N
C = [0]*N
D = [0]*N
for i in range(N):
    A[i], B[i], C[i], D[i] =  map(int, input().split())

X = [ [0]*(W+2) for _ in range (H+2)]
Z = [ [0]*(W+2) for _ in range (H+2)]

for i in range (N):
    X[A[i]][B[i]] += 1
    X[A[i]][D[i]+1] -= 1
    X[C[i]+1][B[i]] -= 1
    X[C[i]+1][D[i]+1] += 1

for i in range (1, H+1):
    for j in range (1, W+1):
        Z[i][j] = Z[i][j-1] + X[i][j]
for j in range (1, W+1):
    for i in range (1, H+1):
        Z[i][j] += Z[i-1][j]

for i in range (1, H+1):
    for j in range (1, W+1):
        print(Z[i][j], end=" ")
    print("")

#10
N = int(input())
A = list(map(int, input().split()))
D = int(input())
L = [None]*D
R = [None]*D
for i in range(D):
    L[i], R[i] = map(int, input().split())

P = [0]*(N)
P[0] = A[0]
Q = [0]*(N)
Q[N-1] = A[N-1]

for i in range (1, N):
    P[i] = max(P[i-1], A[i])

for i in range (N-2, -1, -1):
    Q[i] = max(Q[i+1], A[i])

for i in range (D):
    print(max(P[L[i]-1-1], Q[R[i]+1-1]))
