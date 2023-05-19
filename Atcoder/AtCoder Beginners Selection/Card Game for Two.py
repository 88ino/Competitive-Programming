N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
sum_A = 0
sum_B = 0
for i in range (0, N, 2):
    sum_A += A[i]
    if not ((N%2 == 1) and (i==N-1)):
        sum_B += A[i+1]
result = sum_A - sum_B
print(result)