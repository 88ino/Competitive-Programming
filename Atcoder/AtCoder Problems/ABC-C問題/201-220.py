#201
S = input()
A = []
B = []
for i in range(10):
    if S[i] == "o":
        A.append(str(i))
    elif S[i] == "?":
        B.append(str(i))
num = [str(i).zfill(4) for i in range(10000)]
ans = 0
for n in num:
    flag = True
    for i in range(4):
        if not(n[i] in A or n[i] in B):
            flag = False
    for j in range(len(A)):
        if not A[j] in n:
            flag = False
    if flag:
        ans += 1

print(ans)


#202
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

count = [0]*(N+1)
ans = 0
for j in range(N):
    count[B[C[j]-1]] += 1
for i in range(N):
    ans += count[A[i]]
print(ans)


#203
N, K = map(int, input().split())
T = []
for i in range(N):
    a, b = map(int, input().split())
    T.append((a, b))
T.sort()
m = K
#もらえるお金の総和を求める
for i in range(N):
    last = T[i][0]
    #その村までの距離が所持金の分より遠い
    if m-last<0:
        break
    #その村に行けるならお金は貰える
    else:
        m += T[i][1]
print(m)


#204
from ast import Mod
import imp
from itertools import permutations
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
G = [ [] for _ in range(N) ]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)

def dfs(v):
    if temp[v]:
        return
    temp[v] = True
    for i in G[v]:
        dfs(i)

ans = 0
for i in range(N):
    temp = [False]*N
    dfs(i)
    ans += temp.count(True)

print(ans)
    

#205
A, B, C = map(int, input().split())
if C%2==0:
    if abs(A) > abs(B):
        print(">")
    elif abs(A) < abs(B):
        print("<")
    else:
        print("=")
else:
    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("=")


#206
N = int(input())
A = list(map(int, input().split()))
c = {}
#Aの出現回数を求める
for a in A:
    if a in c:
        c[a] += 1
    else:
        c[a] = 1
ans = 0
#Aの残りの回数を減らしながら、右側の自身と異なる個数を足し合わせる
for i in range(N):
    c[A[i]] -= 1
    ans += N-i-1-c[A[i]]
print(ans)


#207
N = int(input())
K = []
for _ in range(N):
    t, l, r = map(int, input().split())
    if t == 2:
        r -= 0.01
    if t == 3:
        l += 0.01
    if t == 4:
        l += 0.01
        r -= 0.01
    K.append((l, r))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        if max(K[i][0], K[j][0]) <= min(K[i][1], K[j][1]):
            ans += 1
print(ans)


#208
N, K = map(int, input().split())
a = list(map(int, input().split()))
k = K//N
m = K%N
B = []
for i in range(N):
    B.append((a[i], i))
B.sort()
C = []
for i in range(m):
    C.append(B[i][1])

C = set(C)
for i in range(N):
    if i in C:
        ans = k+1
    else:
        ans = k
    print(ans)


#209
N = int(input())
C = list(map(int, input().split()))
MOD = 10**9 + 7
M = max(C)
if M < N:
    print(0)
    exit()
C.sort()
ans = 1
for i in range(N):
    ans = ans*(C[i] - i)%MOD
print(ans)


#210
from collections import Counter

N, K = map(int, input().split())
c = list(map(int, input().split()))

counts = Counter(c[:K])
unique_counts = [len(counts)]

for i in range(K, N):
    counts[c[i-K]] -= 1
    if counts[c[i-K]] == 0:
        del counts[c[i-K]]

    counts[c[i]] += 1
    unique_counts.append(len(counts))

print(max(unique_counts))


#211
S = input()
MOD = 10**9+7
N = len(S)
c = "chokudai"
dp = [ [0]*9 for _ in range(N+1) ]
for i in range(N):
    dp[i][0] = 1
for j in range(1, 9):
    dp[0][j] = 0

for i in range(1, N+1):
    for j in range(1, 9):
        if S[i-1] == c[j-1]:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j]
        dp[i][j] %= MOD
print(dp[N][8])


#212
import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
result = []
for i in range(N):
    pos = bisect.bisect_left(B, A[i])
    if pos != 0 and pos != M:
        a = min(abs(A[i]-B[pos]), abs(A[i]-B[pos-1]))  
    elif pos == M:
        a = abs(A[i]-B[M-1])
    else:
        a = abs(A[i]-B[0])
    result.append(a)
print(min(result))


#213
H, W, N = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

#A,Bの要素がそれぞれ何番目に小さい数か
As = sorted(list(set(A)))
Bs = sorted(list(set(B)))

#A,Bの要素の順番を辞書で保存、キーを与えたら圧縮後の値を返す
As_d = { As[i]: i+1 for i in range(len(As))}
Bs_d = { Bs[i]: i+1 for i in range(len(Bs))}

for i in range(N):
    ai = As_d[A[i]]
    bi = Bs_d[B[i]]
    print(ai, bi)


#214
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

start = T.index(min(T))
ans = {i:None for i in range(1, N+1) }
c = 0
i = start
a = T[i]
ans[i+1] = a
while c < N+1:
    i += 1
    if i >= N:
        i = 0
        a = min(T[i], a + S[-1])
    else:
        a = min(T[i], a + S[i-1])
    ans[i+1] = a
    c += 1

for i in range(1, N+1):
    print(ans[i])


#215
from itertools import permutations
S, K = input().split()
K = int(K)
st = set()
for s in permutations(S):
    st.add("".join(s))
ans = list(st)
ans.sort()
print(ans[K-1])


#216
N = int(input())
m = N
ans = []
while m >= 1:
    if m%2==0:
        m //= 2
        ans.append("B")
    else:
        m -= 1
        ans.append("A")
p = "".join(ans)[::-1]
print(p)


#217
N = int(input())
p = list(map(int, input().split()))
a = {p[i]:i+1 for i in range(N)}
q = []
for i in range(N):
    q.append(a[i+1])
print(*q)


#218
N = int(input())

def data():
    A = set()
    for y in range(N):
        l = input()
        for x in range(N):
            if l[x] == "#":
                A.add((x, y))
    return A
S = data()
T = data()
flag = False

for _ in range(4):
    mx, my = min(S)
    S = set((x-mx, y-my) for x, y in S)
    mx, my = min(T)
    T = set((x-mx, y-my) for x, y in T)

    if S==T:
        flag = True
    T = set((y, -x) for x, y in T)

if flag:
    print("Yes")
else:
    print("No")


#219
X = input()
N = int(input())
S = []
for _ in range(N):
    S.append(list(input()))
X_order = {X[i]:chr(ord("a")+i) for i in range(26)}
X_return = {chr(ord("a")+i) :X[i] for i in range(26)}

for i in range(N):
    for j in range(len(S[i])):
        S[i][j] = X_order[S[i][j]]
S.sort()
for i in range(N):
        for j in range(len(S[i])):
            S[i][j] = X_return[S[i][j]]
for i in range(N):
    print("".join(S[i]))

##
X = input()
N = int(input())
S = []
for _ in range(N):
    S.append(input())

pos = [0]*26
for i in range(26):
    pos[ord(X[i])-ord("a")] = i

S.sort(key=lambda s: (tuple(pos[ord(c)-ord("a")] for c in s), len(s)))
for s in S:
    print(s)

#
X = input()
N = int(input())
order = {X[i]: i for i in range(26)}
S = [input() for _ in range(N)]

S.sort(key=lambda s: [order[c] for c in s])

for s in S:
    print(s)


#220
N = int(input())
A = list(map(int, input().split()))
X = int(input())
M = X//sum(A)
m = X%sum(A)
count = 0
for i in range(N):
    m -= A[i]
    if m < 0:
        break

print(M*N + i+1)

