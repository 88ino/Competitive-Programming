
map(int, input().split())

int(input())

###A
S = input()
N = len(S)
for i in range(N-1, -1, -1):
    if S[i] == ".":
        ans = S[i+1:]
        break
print(ans)


###B
def paint_grid(H, W, N):
    grid = [['.' for _ in range(W)] for _ in range(H)]

    x, y = 0, 0  
    dx, dy = -1, 0 

    for _ in range(N):
        if grid[x][y] == '.':
            grid[x][y] = '#'  
            dx, dy = dy, -dx
        else:
            grid[x][y] = '.' 
            dx, dy = -dy, dx
        
        x, y = (x + dx) % H, (y + dy) % W

    return [''.join(row) for row in grid]
H, W, N = map(int, input().split())
ans = paint_grid(H, W, N)
for i in range(H):
    print(ans[i])


###C
def cal_sum(N, A):
    cumulative_sum = 0
    min_cumulative_sum = 0

    for change in A:
        cumulative_sum += change
        min_cumulative_sum = min(min_cumulative_sum, cumulative_sum)

    initial_passengers = max(0, -min_cumulative_sum)

    current_passengers = cumulative_sum + initial_passengers

    return current_passengers

N = int(input())
A = list(map(int, input().split()))
print(cal_sum(N, A))


###D
###D
from collections import deque
def min_moves(N, grid):
    players = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 'P']

    queue = deque([(players[0], players[1], 0)])
    visited = set([(players[0], players[1])])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        pos1, pos2, moves = queue.popleft()

        if pos1 == pos2:
            return moves

        for dx, dy in directions:
            new_pos1 = (pos1[0] + dx, pos1[1] + dy) if 0 <= pos1[0] + dx < N and 0 <= pos1[1] + dy < N and grid[pos1[0] + dx][pos1[1] + dy] != '#' else pos1
            new_pos2 = (pos2[0] + dx, pos2[1] + dy) if 0 <= pos2[0] + dx < N and 0 <= pos2[1] + dy < N and grid[pos2[0] + dx][pos2[1] + dy] != '#' else pos2

            if (new_pos1, new_pos2) not in visited:
                visited.add((new_pos1, new_pos2))
                queue.append((new_pos1, new_pos2, moves + 1))

    return -1

N = int(input())
grid = [input() for _ in range(N)]
print(min_moves(N, grid))


###E
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

class SegTree:

    def __init__(self, init_val, segfunc, ide_ele):

        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):

        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):

        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    MAX = 5*(10**5)+5

    ide_ele = 0

    dp = SegTree([0] * MAX, segfunc=max, ide_ele=ide_ele)

    for i in range(N):
        a = A[i]
        l = max(0, a - K)
        r = min(MAX, a + K + 1)
        now = dp.query(l, r) + 1
        dp.update(a, now)

    print(dp.query(0, MAX))


if __name__ == "__main__":
    main()


###F
from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]
count_a = Counter(A)
ans = 0
E = set()
for i in range(N-1):
    for j in range(i+1, N):
        a = A[i]*A[j]
        if a in E:
            continue
        if a in count_a:
            bi = count_a[A[i]]
            bj = count_a[A[j]]
            aa = count_a[a]

            if A[i]==1 or A[j] == 1:
                if A[i] > A[j]:
                    bi -= 1
                else:
                    bj -= 1

            ans += 2*bi*bj*aa
            E.add(a)
print(ans)


