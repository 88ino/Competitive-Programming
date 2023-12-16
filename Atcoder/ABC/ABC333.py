
###A
N = int(input())
ans = ''
for _ in range(N):
    ans += f'{N}' 
print(ans)



###B
def is_equal_length(s1, s2, t1, t2):
    points = "ABCDE"

    def are_adjacent(p1, p2):
        return (points.index(p1) - points.index(p2)) % 5 == 1 or (points.index(p2) - points.index(p1)) % 5 == 1

    return "Yes" if are_adjacent(s1, s2) == are_adjacent(t1, t2) else "No"

a = input()
b = input()
s1 = a[0]
s2 = a[1]
t1 = b[0]
t2 = b[1]

print(is_equal_length(s1, s2, t1, t2))


###C
def find_repunits(n):
    repunits = [int("1" * i) for i in range(1, 15)]

    sums = set()
    for i in repunits:
        for j in repunits:
            for k in repunits:
                sums.add(i + j + k)

    return sorted(sums)[n - 1]

N = int(input())
print(find_repunits(N))




###D
from collections import deque

N = int(input())
G = [ list() for i in range(N + 1) ]
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dist = [ -1 ] * (N + 1)
dist[1] = 0
Q = deque()
Q.append(1)

while len(Q) >= 1:
	pos = Q.popleft() # キュー Q の先頭要素を取り除き、その値を pos に代入する
	for nex in G[pos]:
		if dist[nex] == -1:
			dist[nex] = dist[pos] + 1
			Q.append(nex)

dis = [ (dist[i], i) for i in range(1, N+1) ]
dis.sort(reverse=True)

num = [1]*(N+1)
end = []
for i in range(N):
     end += [dis[i][1]]
     nex = G[dis[i][1]]
     for j in nex:
          if j in end:
               continue
          num[j] += num[dis[i][1]]

if len(G[1])==1:
     print(1)
     exit()

a = G[1]
ans = 10**10
for p in a:
     ans = min(ans, num[p])
print(ans+1)


###E
N = int(input())
adv = []
for _ in range(N):
    t, x= map(int, input().split())
    adv.append((t, x))

