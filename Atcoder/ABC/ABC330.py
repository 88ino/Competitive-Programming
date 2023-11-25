
map(int, input().split())

list(map(int, input().split()))



###A
N, L = map(int, input().split())
A = list(map(int, input().split()))
count = 0
for a in A:
    if a >= L:
        count += 1
print(count)




###B
def closest(N, L, R, A):
    X = []  
    for a in A:
        if a < L:
            X.append(L)
        elif a > R:
            X.append(R)
        else:
            X.append(a)
    return X

N, L, R = map(int, input().split())
A = list(map(int, input().split()))
print(*closest(N, L, R, A))



###C
def min_difference(D):
    min_diff = D  

    x = 0
    while x*x <= D:
        y2 = D - x*x
        y = int(y2**0.5)
        
        for dy in [0, 1]:
            diff = abs(x*x + (y + dy)**2 - D)
            min_diff = min(min_diff, diff)

            if min_diff == 0:
                return min_diff
        x += 1

    return min_diff

D = int(input())
print(min_difference(D))





###D
def count(N, grid):
    rows_o_count = [0] * N
    cols_o_count = [0] * N
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':
                rows_o_count[i] += 1
                cols_o_count[j] += 1

    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':
                count += (rows_o_count[i] - 1) * (cols_o_count[j] - 1)

    return count

N = int(input())
grid = []

for _ in range(N):
    s = input()
    grid.append(s)

print(count(N, grid))



###E
def find_mex(arr):
    num_set = set(arr)
    mex = 0
    while mex in num_set:
        mex += 1
    return mex

N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = []

for _ in range(Q):
    i, x = map(int, input().split())
    A[i-1] = x
    mex = find_mex(A)
    print(mex)


######
import collections
import heapq

def process_queries(N, Q, A, queries):
    # Initialize a set to store missing elements (elements not in A)
    missing_elements = set(range(N + 1))
    # Initialize a heap with the missing elements
    heap = list(missing_elements)
    heapq.heapify(heap)

    results = []
    for i, x in queries:
        # Update the set and heap based on the query
        if x not in missing_elements:
            missing_elements.remove(x)
            while heap and heap[0] not in missing_elements:
                heapq.heappop(heap)
        else:
            missing_elements.discard(x)
            heapq.heappush(heap, x)

        # The mex is the smallest value not in A
        results.append(heap[0])

    return results



N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = []
for _ in range(Q):
    i, x = map(int, input().split())
    queries.append((i, x))

results = process_queries(N, Q, A, queries)
for r in results:
    print(r)



###
import collections
import heapq

N, Q = map(int, input().split())
A = list(map(int, input().split()))
c = collections.Counter(A)
d = [i for i in N]
B = set(d) - set(A)
B = heapq(B)

for _ in range(Q):
    i, x = map(int, input().split())
    c[A[i-1]] -= 1
    c[x] += 1
    if c[A[i-1]] == 0:
        heapq.heappush()
    if c[x] == 1:
        B.remove(x)

    print(min(B))

