#201
N = int(input())
mount = []
for _ in range(N):
    s, t = input().split()
    t = int(t)
    mount.append((t, s))

mount.sort(reverse=True)
print(mount[1][1])


#202
S = input()
S2 = S[::-1]
S2 = S2.replace("6", "x").replace("9", "6").replace("x", "9")
print(S2)


#203
N, K = map(int, input().split())
print( K*100*(N+1)*N//2 + N*(K+1)*K//2)


#204
N = int(input())
A = list(map(int, input().split()))
Sum = 0
for i in range(N):
    if A[i] > 10:
        Sum += A[i] - 10
print(Sum)


#205
N = int(input())
A = list(map(int, input().split()))
if len(set(A)) == N:
    print("Yes")
else:
    print("No")


#206
N = int(input())
i = 0
while 1:
    if i*(i+1)//2 >= N:
        print(i)
        break
    i += 1 


#207
a, b, c, d = map(int, input().split())
if d*c-b < 1:
    print(-1)
else:
    print(a//(d*c - b)  +1 if a%(d*c - b) != 0 else a//(d*c - b))


#208
P = int(input())
money = []
money.append(1)
for i in range(2, 11):
    money.append(money[i-2]*i)
money = money[::-1]

count = 0
p = P
# money[0] is 3628800, so money[0]*100 > 10**7 >= P 
for m in money:
        count += p//m
        p = p%m
        if p == 0:
            break
print(count)


#209
N, X = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) - N//2 <= X:
    print("Yes")
else:
    print("No")


#210
N = int(input())
S = input()
a = S.index("1")
if a%2 == 0:
    print("Takahashi")
else:
    print("Aoki")


#211
A = []
for _ in range(4):
    s = input()
    A.append(s)
if len(set(A)) == 4:
    print("Yes")
else:
    print("No")


#212
X = input()
for i in range(3):
    if not (X[0]==X[1]==X[2]==X[3] or str(X[i+1]) == str(int(X[i])+1) or X[i+1] == "0" and X[i] == "9"):
        print("Strong")
        exit()
print("Weak")


#213
N = int(input())
A = list(map(int, input().split()))

B = set(A)
ans = sorted(B)[-2]

print(A.index(ans)+1)


#214
S, T = map(int, input().split())
count = 0
for a in range(0, S+1):
    for b in range(0, S+1-a):
        for c in range(0, S+1-a-b):
            if a*b*c <= T:
                count += 1
print(count)


#215
N = int(input())
two_k = 1
for k in range(61):
    two_k *= 2
    if two_k > N:
        print(k)
        break


#216
N = int(input())
people = []
for _ in range(N):
    s = input()
    people.append(s)
if len(set(people)) == N:
    print("No")
else:
    print("Yes")


#217
contests = ["ABC", "ARC", "AGC", "AHC"]
contests.remove(input())
contests.remove(input())
contests.remove(input())
print(*contests)


#218
P = list(map(int, input().split()))
S = ""
for i in range(26):
    S += chr(ord("a") + P[i] - 1)
print(S)


#219
S1 = input()
S2 = input()
S3 = input()
T = input()
ans = ""
for i in T:
    if i == "1":
        ans += S1
    elif i == "2":
        ans += S2
    else:
        ans += S3
print(ans)


#220
K = int(input())
A, B = input().split()
print(int(A, K)*int(B, K))


