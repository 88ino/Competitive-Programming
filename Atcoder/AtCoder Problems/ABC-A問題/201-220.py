#201
A = list(map(int, input().split()))
A.sort()
if A[2]-A[1] == A[1]-A[0]:
    print("Yes")
else:
    print("No")


#202
a, b, c = map(int, input().split())
print(7*3-a-b-c)


#203
a, b, c = map(int, input().split())
if a==b:
    print(c)
elif b==c:
    print(a)
elif c==a:
    print(b)
else:
    print(0)


#204
x, y = map(int, input().split())
if x==y:
    print(x)
else:
     a = list({0, 1, 2} - {x, y})
     print(a[0])


#205
A, B = map(int, input().split())
print(B*A/100)


#206
N = int(input())
p = int(N*1.08)
if p<206:
    print("Yay!")
elif p==206:
    print("so-so")
else:
    print(":(")


#207
A, B, C = map(int, input().split())


#208
A, B = map(int, input().split())
if A <= B <= 6*A:
    print("Yes")
else:
    print("No")


#209
A, B = map(int, input().split())
if B-A+1 > 0:
    print(B-A+1)
else:
    print(0)


#210
N, A, X, Y = map(int, input().split())
price = 0
if N > A:
    print(X*A+Y*(N-A))
else:
    print(X*N)
    

#211
A, B = map(int, input().split())
print((A-B)/3+B)


#212
A, B = map(int, input().split())
if 0<A and B==0:
    print("Gold")
elif A==0 and 0<B:
    print("Silver")
else:
    print("Alloy")


#213
A, B = map(int, input().split())
for c in range(256):
    if c == A^B:
        print(c)
        break


#214
N = int(input())
if N<=125:
    print(4)
elif N<=211:
    print(6)
else:
    print(8)


#215
S = input()
if S == "Hello,World!":
    print("AC")
else:
    print("WA")


#216
X, Y = map(int, input().split("."))
if Y<=2:
    print(X, end="-")
elif Y<=6:
    print(X)
else:
    print(X, end="+")


#217
S, T = input().split()
if S < T:
    print("Yes")
else:
    print("No")


#218
N = int(input())
S = input()
if S[N-1]=="o":
    print("Yes")
else:
    print("No")


#219
X = int(input())
if X>=90:
    print("expert")
else:
    if X<40:
        print(40-X)
    elif X<70:
        print(70-X)
    else:
        print(90-X)

#220
A, B, C = map(int, input().split())
for i in range(0, 1001, C):
    if A<=i<=B:
        print(i)
        exit()
print(-1)

