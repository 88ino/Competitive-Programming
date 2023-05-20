#1
N = int(input())
print(N**2)

#2
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range (N):
    if A[i] == X:
        print("Yes")
        exit()
print("No")

#3
N, K = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
for i in range (N):
    for j in range (N):
        if P[i] + Q[j] == K:
            print("Yes")
            exit()
print("No")

#4
N =int(input())
for i in range (9,-1, -1):
    w = 2 ** i
    print((N//w)%2, end="")
print("")

#5
N, K = map(int, input().split())
count = 0
for i in range (1, N+1):
    for j in range (1, N+1):
        l = K-i-j
        if 1<= l <= N:
            count += 1
print(count)
