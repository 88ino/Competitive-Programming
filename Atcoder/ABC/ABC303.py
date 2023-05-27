



# A #

N = int(input())
S = input()
T = input()
def check(N, S, T):
    for i in range(N):
        if not(S[i]==T[i] or (S[i]=="1" and T[i]=="l")or (S[i]=="l" and T[i]=="1")or(S[i]=="0" and T[i]=="o")or(S[i]=="o" and T[i]=="0")):
            return False
    return True

if check(N, S, T):
    print("Yes")
else:
    print("No")







# B #
N, M = map(int, input().split())
a = []
for _ in range(M):
    a.append(list(map(int, input().split())))

def count_p(N, M, a):
    count = 0
    for i in range(1, N):
        for j in range(i+1, N+1):
            funaka = True
            for k in range(M):
                if abs(a[k][i-1] - a[k][j-1]) == 1:
                    funaka = False
                    break
            if funaka == True:
                count+=1
    return count

result = count_p(N, M, a)
print(result)

####
N, M = map(int, input().split())
a = []
for _ in range(M):
    a.append(list(map(int, input().split())))

def count_p(N, M, a):
    count = 0
    for i in range(1, N):
        for j in range(i+1, N+1):
            for k in range(M):
                if abs(a[k].index(i) - a[k].index(j)) == 1:
                    break
            else:
                count += 1
    return count

result = count_p(N, M, a)
print(result)




# C #
n, m, h, k = map(int, input().split())
s = input()
st = set()
for _ in range(m):
    x, y = map(int, input().split())
    st.add((x, y))
nx, ny = 0, 0
for i in range(n):
    dx, dy = 0, 0
    if s[i] == 'R':
        dx = 1
    if s[i] == 'L':
        dx = -1
    if s[i] == 'U':
        dy = 1
    if s[i] == 'D':
        dy = -1
    nx += dx
    ny += dy
    h -= 1
    if h < 0:
        print("No")
        exit()
    if h < k and (nx, ny) in st:
        h = k
        st.remove((nx, ny))
print("Yes")


###


N, M, H, K = map(int, input().split())
S = input()
items = {tuple(map(int, input().split())) for _ in range(M)}

x, y = 0, 0
directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

for move in S:
    dx, dy = directions[move]
    x += dx
    y += dy
    H -= 1
    if (x, y) in items and H < K:
        H = K

    if H <= 0:
        print("No")
        exit()

print("Yes")

####
N, M, H, K = map(int, input().split())
S = input()
items = {tuple(map(int, input().split())) for _ in range(M)}

x, y = 0, 0
directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

for i, move in enumerate(S):
    dx, dy = directions[move]
    x += dx
    y += dy
    H -= 1
    if (x, y) in items and H < K:
        H = K
    if H <= 0 and i < N - 1:
        print("No")
        exit()

print("Yes")




# D #

X, Y, Z = map(int, input().split())
S = input()

N = len(S)
INF = float('inf')

dp = [[INF, INF] for _ in range(N+1)]

dp[0][0] = 0

for i in range(N):
    if S[i] == 'a':
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + X, dp[i][1] + min(Y+Z, X+Z))
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + min(Y+Z, X+Z), dp[i][1] + Y)
    else:
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + Y, dp[i][1] + min(X+Z, Y+Z))
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + min(X+Z, Y+Z), dp[i][1] + X)

print(min(dp[N]))






# E #


from collections import defaultdict

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

degree = defaultdict(int)

for u, v in edges:
    degree[u] += 1
    degree[v] += 1

center = max(degree.keys(), key=lambda k: degree[k])
star_count = degree[center] - 1
star_level = sorted(degree.values(), reverse=True)[:star_count]

for level in star_level:
    print(level, end=" ")
print("")









# F #
import heapq

N, H = map(int, input().split())
spells = [list(map(int, input().split())) for _ in range(N)]

heap = [(-d/t, -d, (t, d)) for t, d in spells]
heapq.heapify(heap)


effect_ends = []

time = 0  

while H > 0:
   
    if not effect_ends:
        break
    _, damage, (t, d) = heapq.heappop(heap)
    H += damage * (effect_ends[0] - time) 
    time = effect_ends[0]
    heapq.heappop(effect_ends)

    if H <= 0:  
        break

    if heap:  
        
        _, damage, spell = heapq.heappop(heap)
        t, d = spell
        time += 1
        H += damage  
      
        heapq.heappush(effect_ends, time + t - 1)  
    if H <= 0:  
        break

print(time)








