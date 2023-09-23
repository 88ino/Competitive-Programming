
map(int, input().split())

list(map(int, input().split()))


###A

N = list(str(input()))
tmp = 10
for n in N:
    if int(n) >= tmp:
        print("No")
        exit()
    else:
        tmp = int(n)
print("Yes")



###B

N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(0, 101):
    B = A + [i]
    B.sort()
    B[0] = 0
    B[-1] = 0
    s = sum(B)
    if s >= X:
        print(i)
        exit()
print(-1)

###C


from collections import deque

def find_kth_321_like_number(k):

    q = deque(sorted([str(i) for i in range(1, 10)]))
    count = 0
    
    while q:
        current = q.popleft()
        count += 1
        if count == k:
            return current
        
        new_numbers = sorted([current + str(digit) for digit in range(int(current[-1]) - 1, -1, -1)])
        q.extend(new_numbers)

K = int(input())
print(find_kth_321_like_number(K))






###D
import bisect
N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
total = 0

cum_B = [0] * M
cum_B[0] = B[0]
for i in range(1, M):
    cum_B[i] = cum_B[i - 1] + B[i]

for ai in A:
    j = bisect.bisect_left(B, P - ai)
    if j == 0:
        s_p = 0
    else:
        s_p = cum_B[j-1]

    total += ai * j + s_p
    total += P * (M - j)

print(total)

###E







###F

