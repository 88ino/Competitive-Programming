
map(int, input().split())

list(map(int, input().split()))

N = int(input())

###A###
T = int(input())

def check(S, N):
    A = [ord(c) -ord('a') for c in S] +[0]*5
    for i in range(1, N):
        if A[i] > A[0]:
            return True
        elif A[i] == A[0] and i!=N:
            for j in range(1, i):
                if i+j > N:
                    return False

                #最後まで同じで長さが後ろの方が大きい場合
                if j == i-1 and i+j < N:
                    if A[j] == A[i+j]:
                        return True
                    
                if A[j] == A[i+j]:
                    continue

                if A[j] > A[i+j]:
                    break
                #途中で大きくなる場合
                if A[j] < A[i+j]:
                    return True

    return False

for _ in range(T):
    N = int(input())
    S = input()
    F = check(S, N)
    if F:
        print("Yes")
    else:
        print("No")

    



###B###
import heapq

# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))

l = A[0]
r = A[1]
B = A[2:]

B.sort()

count = 0
M_counter = 0
outside = []

# 左側から範囲に入るものを加えていく
while B and B[0] <= r:
    b = B.pop(0)
    if b >= l:
        M_counter += 1
    else:
        count += l - b
        M_counter += 1

# 右側から範囲に入るものを加えていく
while B and B[-1] >= l:
    b = B.pop(-1)
    if b <= r:
        M_counter += 1
    else:
        heapq.heappush(outside, (abs(b - l), abs(b - r)))

# 範囲外から範囲に入るものを加えていく
while outside and M_counter < M:
    l_diff, r_diff = heapq.heappop(outside)
    if l_diff <= r_diff:
        count += l_diff
        l += l_diff
    else:
        count += r_diff
        r += r_diff
    M_counter += 1

print(count)




