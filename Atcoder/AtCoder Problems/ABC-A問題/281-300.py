#281
N = int(input())
for i in range(N, -1, -1):
    print(i)


#282
K = int(input())
for i in range(K):
    print(chr(ord("A") + i), end="")


#283
A, B = map(int, input().split())
print(A**B)


#284
N = int(input())
S = [None]*N
for i in range(N):
    S[i] = input()
for i in range(N-1, -1, -1):
    print(S[i])


#285
a, b = map(int, input().split())
if a*2 == b or a*2+1 == b:
    print("Yes")
else:
    print("No")


#286
N, P, Q, R, S = map(int, input().split())
A = [0] + list(map(int, input().split()))
print(*(A[1:P]+A[R:S+1]+A[Q+1:R]+A[P:Q+1]+A[S+1:]))


#287
N = int(input())
Agree = 0
for _ in range(N):
    s = input()
    if s == "For":
        Agree += 1
if Agree > N//2:
    print("Yes")
else:
    print("No")


#288
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(a+b)


#289
s = input()
ans = ""
for c in s:
    if c == "0":
        ans += "1"
    else:
        ans += "0"
print(ans)

##
s = input()
print(s.replace("0", "a").replace("1", "0").replace("a", "1"))


#290
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
s = 0
for i in range(M):
    s += A[B[i]-1]
print(s)


#291
S=input()
for i in range(len(S)):
    if ord("A") <= ord(S[i]) and ord(S[i]) <= ord("Z"):
        print(i+1)
        exit()

#292
S=input()
print(S.upper())


#293
S=input()
ans = []
for i in range(0, len(S), 2):
    ans.append(S[i+1])
    ans.append(S[i])

print("".join(ans))

#294
N=int(input())
A=list(map(int, input().split()))
ans = []
for a in A:
    if a%2 == 0:
        ans.append(a)
print(*ans)

##
N=int(input())
A=list(map(int, input().split()))
for a in A:
    if a%2==0:
        print(a, end=" ")


#295
N=int(input())
W = list(input().split())
moji = ["and", "not", "that", "the", "you"]
for w in W:
    if w in moji:
        print("Yes")
        exit()
print("No")


#296
N=int(input())
S=input()
for i in range(N-1):
    if S[i]==S[i+1]:
        print("No")
        exit()
print("Yes")


#297
N,D = map(int, input().split())
T = list(map(int, input().split()))
for i in range(N-1):
    if T[i+1] - T[i] <= D:
        print(T[i+1])
        exit()
print(-1)


#298
N=int(input())
S=list(input())
if "o" in S and not "x" in S:
    print("Yes")
else:
    print("No")


#299
N=int(input())
S=input()
left=False
for i in range(N):
    if left == True and S[i]=="|":
        print("out")
        exit()
    if left == True and S[i]=="*":
        print("in")
        exit()
    if S[i]=="|":
        left = True

##
N=int(input())
S=input()
if S.index("|") < S.index("*") < S.rindex("|"):
    print("in")
else:
    print("out")


#300
N, A, B = map(int, input().split())
C = list(map(int, input().split()))
print(C.index(A+B) +1 ) 
