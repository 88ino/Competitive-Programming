# 281
S = list(input())
n = len(S)
flag = True
if n != 8:
    print("No")
    exit()
if S[0].isdecimal() or S[-1].isdecimal():
    flag = False
for i in range(1, n-1):
    if S[i].isdecimal() == False:
        flag = False
        break
if S[1] == "0":
    flag = False

print("Yes") if flag else print("No")


# 282
N, M = map(int, input().split())
S = []
for _ in range(N):
    s = input()
    S.append(s)
ans = 0

for i in range(N-1):
    for j  in range(i+1, N):
        flag = True
        for k in range(M):
            if S[i][k] == "x" and S[j][k] == "x":
                flag = False
        if flag:
            ans += 1
print(ans)


# 283
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    q0, *q = map(int, input().split())
    if q0 == 1:
        A[q[0]-1] = q[1]
    else:
        print(A[q[0]-1])


# 284
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A[i] %2 == 1 for i in range(N)))


# 285
N = int(input())
S = input()

for i in range(1, N):
    a = 0
    for k in range(N-i):
        if S[k] == S[i+k]:
            break
        a = k + 1 
    print(a)
    

# 286
N = int(input())
S = list(input())
T = []
for i in range(N):
    if i >= 1 and T[-1] == "n" and S[i] == "a":
        T.append("y")
    T.append(S[i])

ans = "".join(T)
print(ans)


# 287
N, M = map(int, input().split())
S = []
T = []
for _ in range(N):
    s = input()
    S.append(s[3:])
for _ in range(M):
    t = input()
    T.append(t)

count = 0
for s in S:
    for t in set(T):
        if s == t:
                count += 1
print(count)


# 288
N, K = map(int, input().split())
S = [input() for _ in range(K)]
S.sort()
for s in S:
    print(s)


# 289
N, M = map(int, input().split())
a = set(list(map(int, input().split())))
B = []
i = 1
while i <= N:
    l = i
    r = i
    if r in a:
        for rr in range(i+1, N+1):  
            r = rr
            if rr not in a:
                break
    for j in range(r, l-1, -1):
        B.append(j)
    i = r+1

print(*B)


# 290
N, K = map(int, input().split())
S = input()
T = []
count = 0
for i in range(N):
    if S[i] == "o":
        if count >= K:
            T.append("x")
        else:
            T.append("o")
            count += 1
    else:
        T.append("x")
print("".join(T))


# 291



# 292



# 293



# 294



# 295



# 296



# 297



# 298



# 299



# 300



