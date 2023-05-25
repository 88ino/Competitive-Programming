#36
N, K = map(int, input().split())

if  K>=2*N-2 and K%2==0:
    print("Yes")
else:
    print("No")

#37
N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

sum_t = 0
for i in range(N):
    sum_t += A[i]*M
sum_t += B*N*M
for i in range(M):
    sum_t += C[i]*N
print(sum_t)

#38
D, N = map(int, input().split())
L = [None]*N
R = [None]*N
H = [None]*N
for i in range(N):
    L[i], R[i], H[i] = map(int, input().split())

lim = [24]*(D+1)
lim[0] = 0
for i in range(N):
    for j in range(L[i], R[i]+1):
        lim[j] = min(lim[j], H[i])

print(sum(lim))

#39
N = int(input())
A = []
for _ in range(N):
    l, r = map(int, input().split())
    A.append([r, l])
# 終了時刻でソート
A.sort()

count = 0
time = 0
for i in range(N):
    # 今の時間が開始時刻より前のとき
    if time <= A[i][1]:
        # 時間を終了時刻に更新
        time = A[i][0]
        count += 1

print(count)

#40
N = int(input())
A = list(map(int, input().split()))

c = [0]*101
for i in range(N):
    c[A[i]] += 1

Ans = 0
for i in range(1, 101):
    Ans += c[i]*(c[i]-1)*(c[i]-2)//6
print(Ans)

#41
N = int(input())
S = input()

for i in range(N-2):
    if S[i]==S[i+1]==S[i+2]:
        print("Yes")
        exit()
print("No")

#42
N, K = map(int, input().split())
A = [None]*(N)
B = [None]*(N)
for i in range(N):
    A[i], B[i] = map(int, input().split())

def Get(a, b, A, B, K):
    count = 0
    for i in range(N):
        if a<=A[i] and A[i]<=a+K and b<=B[i] and B[i]<=b+K:
            count += 1
    return count

Ans = 0
for a in range(1, 101):
    for b in range(1, 101):
        Ans = max(Ans, Get(a, b, A, B, K))

print(Ans)        

#43
N, L =  map(int, input().split())
A = [None]*N
B = [None]*N
for i in range(N):
    A[i], B[i] = input().split()
    A[i] = int(A[i])

Ans = 0
for i in range(N):
    if B[i] == "E":
        Ans = max(Ans, L-A[i])
    else:
        Ans = max(Ans, A[i])
print(Ans)

#44
N, Q = map(int, input().split())
A = list(range(0, N+1))

state = 1
for i in range(Q):
    Query = input().split()
    Query[0] = int(Query[0])

    if Query[0] == 1:
        Query[1] = int(Query[1])
        Query[2] = int(Query[2])

        if state == 1:
            A[Query[1]] = Query[2]
        else:
            A[N-Query[1]+1] = Query[2]

    if Query[0] == 2:
        state *= -1
    
    if Query[0] == 3:
        Query[1] = int(Query[1])
        if state == 1:
            print(A[Query[1]])
        else:
            print(A[N-Query[1]+1])

#45
N, C = input().split()
N = int(N)
A = input()

score = 0
for i in range(N):
    if A[i] == "W":
        score += 0
    if A[i] == "B":
        score += 1
    if A[i] == "R":
        score += 2

if score%3==0 and C=="W":
    print("Yes")
elif score%3==1 and C=="B":
    print("Yes")
elif score%3==2 and C=="R":
    print("Yes")
else:
    print("No")
