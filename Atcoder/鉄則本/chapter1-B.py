#B1
A, B = map(int, input().split())

print(A + B)

#B2
A, B = map(int, input().split())
for i in range(A, B+1):
    if 100 % i == 0:
        print("Yes")
        exit()
print("No")

#B3
N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if A[i] + A[j] + A[k] == 1000:
                print("Yes")
                exit()
print("No")

#B4
N = input()

ans = 0
for i in range(len(N)):
    if N[len(N)-i-1] == "1":
        ans += 2**i
print(ans)




