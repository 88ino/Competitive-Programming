
map(int, input().split())

list(map(int, input().split()))


###A
N = int(input())
xs = 0
ys = 0
for i in range(N):
    x, y = map(int, input().split())
    xs += x
    ys += y
if xs > ys:
    print("Takahashi")
elif xs == ys:
    print("Draw")
else:
    print("Aoki")


###B
def is_extended_abc_string(s):
    if not s:
        return "Yes"

    state = 0

    for char in s:
        if state == 0: # Aを探す
            if char == 'A':
                continue
            elif char == 'B':
                state = 1
            elif char == 'C':
                state = 2
            else:
                return "No"
        elif state == 1: # Bを探す
            if char == 'B':
                continue
            elif char == 'C':
                state = 2
            else:
                return "No"
        elif state == 2: # Cを探す
            if char != 'C':
                return "No"
    
    return "Yes"

s = input()
print(is_extended_abc_string(s))



###C
def determine_order(N, A):
    order = []

    next_person = {}

    for i in range(N):
        if A[i] == -1:
            order.append(i + 1)
            break

    for i in range(N):
        if A[i] != -1:
            next_person[A[i]] = i + 1

    current = order[0]
    while len(order) < N:
        next_p = next_person.get(current)
        if next_p:
            order.append(next_p)
            current = next_p

    return order

N = int(input())
A = list(map(int, input().split()))
print(*determine_order(N, A))


###D
def min_sequence(H, W, K, grid):
    def count_needed_dots(sequence, start, end):
        if 'x' in sequence[start:end]:
            return 10**6
        return sum(1 for i in range(start, end) if sequence[i] == '.')

    min_operations = 10**6

    for i in range(H):
        for j in range(W - K + 1):
            operations = count_needed_dots(grid[i], j, j + K)
            min_operations = min(min_operations, operations)

    for j in range(W):
        for i in range(H - K + 1):
            operations = count_needed_dots(''.join(grid[x][j] for x in range(H)), i, i + K)
            min_operations = min(min_operations, operations)

    return -1 if min_operations == 10**6 else min_operations

H, W, K = map(int, input().split())
grid = [input() for _ in range(H)]
print(min_sequence(H, W, K, grid))




###E
import sys
import math

def find_rotten_juice(N):
    M = math.ceil(math.log2(N))
    print(M)
    sys.stdout.flush()

    for i in range(M):
        juices = [j + 1 for j in range(N) if (j >> i) & 1]
        print(len(juices), *juices)
        sys.stdout.flush()

    S = input().strip()
    rotten_juice = 0
    for i, bit in enumerate(S):
        if bit == '1':
            rotten_juice |= 1 << i
    print(rotten_juice + 1)
    sys.stdout.flush()

N = int(input())
find_rotten_juice(N)





###F







