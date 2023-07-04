#261
L1, R1, L2, R2 = map(int, input().split())

print(min(R1, R2) - max(L1, L2) if min(R1, R2) - max(L1, L2) >=0 else 0)


#262
Y = int(input())
for i in range(4):
    if (Y+i)%4 == 2:
        print(Y+i)
        exit()


#263
a, b, c, d, e = map(int, input().split())
m = min(a, b, c, d, e)
M = max(a, b, c, d, e)
if (M*2 + m*3 == a+b+c+d+e or M*3 + m*2 == a+b+c+d+e) and {a,b,c,d,e}=={m, M}:
    print("Yes")
else:
    print("No")


#264
L, R = map(int, input().split())
S = "atcoder"
print(S[L-1:R])


#265
X, Y, N = map(int, input().split())
a = N//3
b = N%3
print(min(a*Y+b*X, N*X))


#266
S = input()
print(S[ len(S)//2 ])


#267
S = input()
D = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for i in range(5):
    if S == D[i]:
        print(5-i)


#268
A = set( map(int, input().split()) )
print(len(A))


#269
a, b, c, d = map(int, input().split())
print((a+b)*(c-d))
print("Takahashi")


#270
def check(a, B):
    for b in B:
        if a == b:
            return True
    return False

A, B = map(int, input().split())
ans=0
if A%2==1 or B%2==1:
    ans += 1
if check(A, [2,3,6,7]) == True or check(B, [2,3,6,7]) == True:
    ans += 2
if check(A, [4,5,6,7]) == True or check(B, [4,5,6,7]) == True:
    ans += 4
print(ans)

##
A, B = map(int, input().split())
print(A|B)


#271
N = int(input())
a = N//16
b = N%16
c = ["A", "B", "C", "D", "E", "F"]
x=str(a)
y=str(b)
if a >=10:
    x = c[a-10]
if b>=10:
    y = c[b-10]
print("{}{}".format(x, y))

##
N = int(input())
print("{:02X}".format(N))


#272
N = int(input())
A = list(map(int, input().split()))
print(sum(A))


#273
N = int(input())
ans = 1

for i in range(1, N+1):
    ans *= i
print(ans)


#274
A, B = map(int, input().split())
print("{:.3f}".format((B/A)))


#275
N = int(input())
H = list(map(int, input().split()))
print(H.index(max(H))+1)


#276
S = input()
for i in range(-1, -len(S)-1, -1):
    if S[i] == "a":
        print(len(S)+i+1)
        exit()
print(-1)


#277
N, X = map(int, input().split())
P = list(map(int, input().split()))
for i in range(N):
    if P[i] == X:
        print(i+1)


#278
N, K = map(int, input().split())
A = list(map(int, input().split()))
K = min(K, N)
B = A[K:]+[0]*K
print(*B)


#279
S = input()
v = S.count("v")
w = S.count("w")
print(v+w*2)


#280
H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())
ans = 0
for i in range(H):
    ans += S[i].count("#")
print(ans)

