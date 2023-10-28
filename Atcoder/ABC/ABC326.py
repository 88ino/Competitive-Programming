
int(input())

map(int, input().split())

list(map(int, input().split()))

[list(map(int, input().split())) for _ in range()]

###A
X, Y = map(int, input().split())
if 0 <= Y-X <= 2 or 0 >= Y-X >= -3:
    print("Yes")
else:
    print("No")




###B
N = int(input())
for i in range(N, 1000):
    a = i//100
    b = (i-a*100)//10
    c = i%10
    if a*b == c:
        print(i)
        exit()



###C
from typing import List

def max_presents(N, M, presents):
    presents.sort() 
    
    max_count = 0 
    left = 0
    right = 0
    
    while right < N: 

        if presents[right] < presents[left] + M:
            right += 1
        else: 
            max_count = max(max_count, right - left)
            left += 1
    
    max_count = max(max_count, right - left)
    
    return max_count
N, M = map(int, input().split())
A = list(map(int, input().split()))
print(max_presents(N, M, A))

###D
N = int(input())
R = list(input())
C = list(input())
grid = []
for i in range(N):
    grid_i = []
    for j in range(3):
        m = ['.']*N
        m[j] = R[i]
        grid_i.append(m)
    grid.append(grid_i)

for j in range(N):
    for i in range(3):
        if grid[i][j]





