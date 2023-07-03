#241
a = list(map(int, input().split()))
t = a[a[a[0]]]
print(t)


#242
A, B, C, X = map(int, input().split())
if X <= A:
    print(1)
elif X <= B:
    print(C/(B-A))
else:
    print(0)


#243
V, A, B, C = map(int, input().split())
v = V%(A+B+C)
if v-A < 0:
    print("F")
elif v-A-B < 0:
    print("M")
else:
    print("T")


#244
N = int(input())
S = input()
print(S[-1])


#245
A, B, C, D = map(int, input().split())
if A < C:
    print("Takahashi")
elif A > C:
    print("Aoki")
else:
    if B <= D:
        print("Takahashi")
    else:
        print("Aoki")


#246
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
Xl = min(x1, x2, x3)
Xr = max(x1, x2, x3)
Ys = min(y1, y2, y3)
Yt = max(y1, y2, y3)
if x1+x2+x3 -Xl-Xr == Xl:
    x = Xr
else:
    x = Xl

if y1+y2+y3 -Ys-Yt == Ys:
    y = Yt
else:
    y = Ys
print(x, y)


#247
S = input()
T = "0" + S[0:3]
print(T)


#248
S = input()
A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
B = {int(i) for i in S}
print(list(A-B)[0])


#249
A, B, C, D, E, F, X = map(int, input().split())
ta = X//(A+C)
t1 = X%(A+C)
if t1>A:
    t1=A
a = A*B*ta + t1*B

tb = X//(D+F)
t2 = X%(D+F)
if t2>D:
    t2=D
b = D*E*tb + t2*E

if a > b:
    print("Takahashi")
elif a == b:
    print("Draw")
else:
    print("Aoki")


#250
H, W = map(int, input().split())
R, C = map(int, input().split())
if H == 1 and W == 1:
    print(0)
elif H == 1:
    if C == 1 or C == W:
        print(1)
    else:
        print(2)
elif W == 1:
    if R == 1 or R == H:
        print(1)
    else:
        print(2)
else:
    if (R==1 and C==1)or(R==1 and C==W)or(R==H and C==1)or(R==H and C==W):
        print(2)
    elif R==1 or R==H or C==1 or C==W:
        print(3)
    else:
        print(4) 

##
H, W = map(int, input().split())
R, C = map(int, input().split())
n = 4
if R==1: n-=1
if R==H: n-=1
if C==1: n-=1
if C==W: n-=1
print(n)


#251
S = input()
S = S*6
print(S[:6])


#252
N = int(input())
print(chr(N))


#253
a, b, c = map(int, input().split())
if min(a, c) <= b <= max(a, c):
    print("Yes")
else:
    print("No")


#254
N = int(input())
print(str(N%100).zfill(2))


#255
R, C = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
if R == 1:
    print(a1[C-1])
else:
    print(a2[C-1])



#256
N = int(input())
print(2**N)

##
N = int(input())
print(1<<N)


#257
N, X = map(int, input().split())
n = (X-1)//N
print( chr(ord("A") + n) )


#258
K =int(input())
h = 21 + K//60
m = K%60
print(f"{h}:" + str(m).zfill(2))

##
K =int(input())
h = 21 + K//60
m = K%60
print("{}:{:02}".format(h, m))


#259
N, M, X, T, D = map(int, input().split())
Birth_height = T - X*D
print(Birth_height + min(M, X)*D)


#260
S = input()
if S[0]==S[1] and S[2]!=S[1]:
    print(S[2])
elif S[1]==S[2] and S[0]!=S[2]:
    print(S[0])
elif S[0]==S[2] and S[1]!=S[0]:
    print(S[1])
elif S[0]!=S[1]!=S[2]:
    print(S[0])
else:
    print(-1)


