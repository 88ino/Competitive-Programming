#51
from collections import deque

Q = int(input())

Query = [input().split() for i in range(Q)]

S = deque()
for q in Query:
    if q[0] == "1":
        S.append(q[1])    
    if q[0] == "2":
        print(S[-1])
    if q[0] == "3":
        S.pop()

#52
from collections import deque
Q = int(input())
query = [input().split() for _ in range(Q)]

Sq = deque()
for q in query:
    if q[0] == "1":
        Sq.append(q[1])
    if q[0] == "2":
        print(Sq[0])
    if q[0] == "3":
        Sq.popleft()

#53
import heapq
Q = int(input())
query = [input().split() for _ in range(Q)]
T = []
for q in query:
    if q[0] == "1":
        heapq.heappush(T, int(q[1]))
    if q[0] == "2":
        print(T[0])
    if q[0] == "3":
        heapq.heappop(T)

#54
Q = int(input())
query = [input().split() for _ in range(Q)]

M = {}
for q in query:
    if q[0] == "1":
        M[q[1]] = q[2]
    if q[0] == "2":
        print(M[q[1]])

#56
N, Q = map(int, input().split())
S = input()
queries = [list(map(int, input().split())) for _ in range(Q)]

T = list(map(lambda c: ord(c) - ord('a') + 1, S))
Mod = 2147483647
p100 = [None]*(N+1)
p100[0] = 1
for i in range(N):
    p100[i+1] = (p100[i] * 100) % Mod

H = [None]*(N+1)
H[0] = 0
for i in range(N):
    H[i+1] = (H[i]*100 + T[i]) % Mod

def hash(l, r):
    return(  (H[r] - H[l-1]*p100[r-l+1]) % Mod)
for a, b, c, d in queries:
    hash1 = hash(a, b)
    hash2 = hash(c, d)
    if hash1 == hash2:
        print("Yes")
    else:
        print("No")

#57
N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

dp = [[None]*(N) for _ in range(30)]
for i in range(N):
    dp[0][i] = A[i] - 1

for d in range(1, 30):
    for i in range(N):
        dp[d][i] = dp[d-1][dp[d-1][i]]

for X, Y in queries:
    now = X - 1
    for d in range(29, -1, -1):
        if ((Y>>d)&1) == 1:
            now = dp[d][now]
    print(now+1)

#58
N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]

class segtree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.dat = [0]*(self.size*2)
    
    def update(self, pos, x):
        pos += self.size
        self.dat[pos] = x
        while pos >= 2:
            pos //= 2
            self.dat[pos] = max(self.dat[pos*2], self.dat[pos*2 + 1])
    
    def Max(self, l, r, a, b, u):
        if r<=a or b<=l:
            return -10**10
        if l<=a and b<=r:
            return self.dat[u]
        m = (a+b)//2
        ans1 = self.Max(l, r, a, m, u*2)
        ans2 = self.Max(l, r, m, b, u*2+1)
        return max(ans1, ans2)

Z = segtree(N)
for q in queries:
    tp, *cont = q
    if tp == 1:
        pos, x = cont
        Z.update(pos-1, x)
    if tp == 2:
        l, r = cont
        ans = Z.Max(l-1, r-1, 0, Z.size, 1)
        print(ans)

#59
N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]

class segtree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.dat = [0]*(self.size*2)
    
    def update(self, pos, x):
        pos += self.size
        self.dat[pos] = x
        while pos >= 2:
            pos //= 2
            self.dat[pos] =self.dat[pos*2] + self.dat[pos*2 + 1]
    
    def Sum(self, l, r, a, b, u):
        if r<=a or b<=l:
            return 0
        if l<=a and b<=r:
            return self.dat[u]
        m = (a+b)//2
        ans1 = self.Sum(l, r, a, m, u*2)
        ans2 = self.Sum(l, r, m, b, u*2+1)
        return ( ans1 + ans2 )

Z = segtree(N)
for q in queries:
    tp, *cont = q
    if tp == 1:
        pos, x = cont
        Z.update(pos-1, x)
    if tp == 2:
        l, r = cont
        ans = Z.Sum(l-1, r-1, 0, Z.size, 1)
        print(ans)

#60
from collections import deque
N = int(input())
A = list(map(int, input().split()))

Ans = [None]*(N)
lev = deque()

for i in range(N):
    if i >= 1:
        lev.append((i, A[i-1]))
        while len(lev) >= 1:
            price = lev[-1][1]
            if price <= A[i]:
                lev.pop()
            else:
                break
    if len(lev) >= 1:
        Ans[i] = lev[-1][0]
    else:
        Ans[i] = -1
        
print(*Ans)




