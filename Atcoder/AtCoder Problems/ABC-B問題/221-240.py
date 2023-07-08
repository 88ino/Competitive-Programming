#221
S = input()
T = input()

if S == T:
    print("Yes")
    exit()
for i in range(len(S)-1):
    if S[:i] + S[i+1] +S[i] + S[i+2:] == T:
        print("Yes")
        exit()
    
print("No")

##
S = list(input())
T = list(input())
if S==T:
    print("Yes")
    exit()
for i in range(len(S)-1):
    S[i], S[i+1] = S[i+1], S[i]
    if S==T:
        print("Yes")
        exit()
    S[i], S[i+1] = S[i+1], S[i]
print("No")


#222
N, P = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for t in a:
    if t < P:
        count+=1
print(count)


#223
S = input()
A = []
for i in range(len(S)):
    A.append(S[i:] + S[:i])
print(min(A))
print(max(A))


#224
H, W = map(int, input().split())
A = [ list(map(int, input().split())) for _ in range(H)]
for i in range(H):
    for j in range(W):
        for s in range(i+1, H):
            for t in range(j+1, W):
                if not A[i][j] + A[s][t] <= A[s][j] + A[i][t]:
                    print("No")
                    exit()
print("Yes")


#225
N = int(input())
G = [ [] for _ in range(N+1) ]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in range(1, N+1):
    if len(G[i]) == N-1:
        print("Yes")
        exit()
print("No")


#226
N = int(input())
A = []
for _ in range(N):
    A.append(input())
print(len(set(A)))


#227
N = int(input())
S = list(map(int, input().split()))
count=0

for s in S:
    for a in range(1, 200):
        for b in range(1, 200):
            if s == 4*a*b + 3*a + 3*b:
                count+=1
                break
        else:
            continue
        break
print(N-count)

#228
N, X = map(int, input().split())
A = [0] + list(map(int, input().split()))
flag = [False]*(N+1)
a = X
while flag[a]==False:
    flag[a] = True
    a = A[a]
print(flag.count(True))


#229
A, B = map(int, input().split())
a = [ int(i) for i in str(A) ]
b = [ int(i) for i in str(B) ]
ans = "Easy"

for i in range(1, min(len(a), len(b))+1):
    if a[-i] + b[-i] >= 10:
        ans = "Hard"
        break
print(ans)

##
A, B = map(int, input().split())
while A > 0 and B > 0:
    if A%10 + B%10 >= 10:
        print("Hard")
        exit()
    else:
        A //= 10
        B //= 10
print("Easy")


#230
S = input()
T = "oxx"*10
if S in T:
    print("Yes")
else:
    print("No")


#231
import statistics

N = int(input())
A = []
for _ in range(N):
    A.append(input())
print(statistics.mode(A))

##
N = int(input())
vote = {}
for _ in range(N):
    s = input()
    if s in vote:
        vote[s] += 1
    else:
        vote[s] = 1
print(max(vote, key=vote.get))


#232
S = input()
T = input()
a = ord(S[0])
b = ord(T[0])
if b - a  < 0:
    a -= 26
for i in range(1, len(S)):
    c = ord(S[i])
    d  = ord(T[i])
    if d - c  < 0:
        c -= 26
    if d - c != b - a:
        print("No")
        exit()
print("Yes")

##
S = input()
T = input()
for i in range(len(S)-1):
    if (ord(T[i])-ord(S[i]))%26 != (ord(T[i+1])-ord(S[i+1]))%26:
        print("No")
        exit()
print("Yes")


#233
L, R = map(int, input().split())
S = input()
L -= 1
R -= 1
T = S[L:R+1]
T= T[::-1]
print(S[:L]+T+S[R+1:])


#234
N = int(input())
D = []*N
for _ in range(N):
    x, y = map(int, input().split())
    D.append((x, y))

def dis(D1, D2):
    return ((D2[0]-D1[0])**2 + (D2[1]-D1[1])**2 )**0.5

a = 0
for i in range(N):
    for j in range(i+1, N):
        a = max(a, dis(D[i], D[j]))

print(a)



#235
N = int(input())
H = list(map(int, input().split()))
place = H[0]
for i in range(N-1):
    if H[i] < H[i+1]:
        place = H[i+1]
    else:
        break
print(place)


#236
N = int(input())
A = list(map(int, input().split()))
B = {}
for i in A:
    if i in B:
        B[i] += 1
    else:
        B[i] = 1
print(min(B, key=B.get))


#237
H, W = map(int, input().split())
A = [ list(map(int, input().split())) for _ in range(H)]

for j in range(W):
    for i in range(H):
        print(A[i][j], end=" ")
    print("")


#238
N = int(input())
A = list(map(int, input().split()))
cut = []
cut.append(0)
cut.append(360)
p = 0
for i in range(N):
    cut.append((p+A[i])%360)
    p = (p+A[i])%360
cut.sort()
ans = 0
for i in range(len(cut)-1):
    ans = max(ans, cut[i+1]-cut[i])
print(ans)


#239
X = int(input())
print(X//10)


#240
N = int(input())
a = list(map(int, input().split()))
print(len(set(a)))
