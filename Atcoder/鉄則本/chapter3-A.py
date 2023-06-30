#11
N, X = map(int, input().split())
A = list(map(int, input().split()))

def search(A, X):
    L = 0
    R = N-1
    while L <= R:
        M = (L+R)//2
        if X > A[M]:
            L = M+1
        if X == A[M]:
            return M
        if X < A[M]:
            R = M-1
    return -1

Ans = search(A, X)
print(Ans+1)

#12
N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(x, N, K, A):
    sum_A = 0  # x秒のときに印刷されている枚数の総和
    for i in range(N):
        sum_A += x//A[i]
    if sum_A >= K:
        return True
    return False
    
L = 1
R = 10**9
while L < R:
    M = (L+R)//2
    Ans = check(M, N, K, A)
    if Ans == True:
        R = M
    else:
        L = M+1
print(L)

#13
N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [None]*N

for i in range(N-1):
    if i == 0:
        R[i] = 0
    else:
        R[i] = R[i-1]

    while (R[i] < N-1) and (A[R[i]+1]-A[i] <= K):
        R[i] += 1

Ans = 0
for i in range(N-1):
    Ans += (R[i]-i)
print(Ans)

#14
import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

P = []
Q = []
for i in range (N):
    for j in range(N):
        tem = A[i]+B[j]
        P.append(tem)
for i in range (N):
    for j in range(N):
        tem = C[i]+D[j]
        Q.append(tem)
Q.sort()

for i in range(N*N):
    # QにK-P[i]と等しい数字があるか2分探索
    q_index = bisect.bisect_left(Q, K-P[i])
    if q_index < N*N and Q[q_index] == K-P[i]:
        print("Yes")
        exit()
print("No")

#15
import bisect
N = int(input())
A = list(map(int, input().split()))

X = list(set(A))
X.sort()

B = [None]*N
for i in range (N):
    B[i] = bisect.bisect_left(X, A[i])

for i in range (len(B)):
    print(B[i]+1, end=" ")
print("")
