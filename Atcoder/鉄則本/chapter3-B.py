#B11
import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = [None]*(Q)
for i in range(Q):
    X[i] = int(input())

A.sort()

for i in range(Q):
    ans = bisect.bisect_left(A, X[i])
    print(ans)

#B12
N = int(input())

def f(x):
    return (x*x*x + x)

#xは0以上10**2以下
left = 0.0
right = 100.0
while right - left > 0.001:
    M = (left + right) / 2
    val = f(M)

    if val > N:
        right = M
    else:
        left = M

print(right)

#B13
N, K = map(int, input().split())
A = list(map(int, input().split()))

S = [0]*(N+1)
for i in range(N):
    S[i+1] = S[i] + A[i]
def sum_price(l, r, S):
    return(S[r]-S[l-1])

R = [None]*(N+1)
R[0] = 0
for i in range(1, N+1):
    R[i] = R[i-1]
    while R[i] < N and sum_price(i, R[i] + 1, S) <= K:
        R[i] += 1

ans = 0
for i in range(1, N+1):
    ans += R[i] - i + 1
print(ans)

#B14
import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

def Enu(A):
    sumlist = []
    l = len(A)
    for i in range(2**l):
        sum_c = 0
        for j in range(l):
            wari = 2**j
            if (i//wari)%2 == 1:
                sum_c += A[j]
        sumlist.append(sum_c)
    return sumlist

L1 = A[0:(N//2)]
L2 = A[(N//2):]

sum1 = Enu(L1)
sum2 = Enu(L2)
sum1.sort()
sum2.sort()

for i in range(len(sum1)):
    pos = bisect.bisect_left(sum2, K-sum1[i])
    if pos < len(sum2) and sum2[pos] == K-sum1[i]:
        print("Yes")
        exit()
print("No")
