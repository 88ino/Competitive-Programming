#221
A, B = map(int, input().split())
print(32**(A-B))


#222
N = int(input())
S = str(N)
for _ in range(4-len(S)):
    S = "0" + S
print(S)


#223
X = int(input())
if X >= 100 and X%100==0:
    print("Yes")
else:
    print("No")


#224
S = input()
if S[-2:] == "er":
    print("er")
else:
    print("ist")


#225
S = input()
n = len(set(S))
if n==3:
    print(6)
elif n== 2:
    print(3)
else:
    print(1)


#226
X = float(input())
Y = int(X*10)
if Y%10 >= 5:
    X += 1
    print(int(X))
else:
    print(int(X))

##
X = float(input())
print(int( round(X + 0.0001, 0) ))


#227
N, K, A = map(int, input().split())
if N==1:
    print(1)
    exit()
if K%N + A - 1 <= N:
    print( K%N + A - 1)
else:
    print( K%N + A - 1 - N)

##
N, K, A = map(int, input().split())
ans = (A+K-1)%N
print(ans if not ans==0 else N)


#228
S, T, X = map(int, input().split())
if S>=T:
    if S<=X or X<T:
        print("Yes")
    else:
        print("No")
elif S<T:
    if S<=X<T:
        print("Yes")
    else:
        print("No")


#229
S1 = input()
S2 = input()

if (S1[0]=="." and S2[1]==".") or (S1[1]=="." and S2[0]=="."):
    print("No")
else:
    print("Yes")


#230
N = int(input())

if N >= 42:
    N += 1 
print( "AGC" + str(N).zfill(3) )


#231
D = int(input())
print(D/100)


#232
S = input()
print(int(S[0])*int(S[2]))


#233
X, Y = map(int, input().split())
if X >= Y:
    print(0)
else:
    if (Y-X)%10==0:
        print((Y-X)//10)
    else:
        print((Y-X)//10 + 1)


#234
t = int(input())
def f(x):
    return x*x + 2*x +3

print( f(f(f(t) + t) + f(f(t))))


#235
S = input()
s = [int(i) for i in S ]
print(100*s[0]+10*s[1]+s[2] + 100*s[1]+10*s[2]+s[0] + 100*s[2]+10*s[0]+s[1])


#236
S = input()
a, b = map(int, input().split())
S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
print(S)


#237
N = int(input())
if -2**31 <= N < 2**31:
    print("Yes")
else:
    print("No")


#238
n = int(input())
if n==1 or n>=5:
    print("Yes")
else:
    print("No")


#239
H = int(input())
print((H*(12800000+H))**0.5)


#240
a, b = map(int, input().split())
if b-a == 1 or b-a == 9:
    print("Yes")
else:
    print("No")


