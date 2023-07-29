
list(map(int, input().split()))
map(int, input().split())

###A
S = input()
a = ["ACE", "BDF","CEG" ,"DFA", "EGB", "FAC", "GBD"]
if S in a:
    print("Yes")
else:
    print("No")


###B
N, M = map(int, input().split())
s = [input() for _ in range(N)]
result = []
for i in range(N-8):
    for j in range(M-8):
        if ( s[i][j] == "#" and s[i][j+1] == "#" and s[i][j+2] == "#" and s[i][j+3] == "." 
            and s[i+1][j] == "#" and s[i+1][j+1] == "#" and s[i+1][j+2] == "#" and s[i+1][j+3] == "."
            and s[i+2][j] == "#" and s[i+2][j+1] == "#" and s[i+2][j+2] == "#" and s[i+2][j+3] == "."
            and s[i+3][j] == "." and s[i+3][j+1] == "." and s[i+3][j+2] == "." and s[i+3][j+3] == "."
            and s[i+5][j+5] == "." and s[i+5][j+6] == "." and s[i+5][j+7] == "." and s[i+5][j+8] == "."
            and s[i+6][j+5] == "." and s[i+6][j+6] == "#" and s[i+6][j+7] == "#" and s[i+6][j+8] == "#"
            and s[i+7][j+5] == "." and s[i+7][j+6] == "#" and s[i+7][j+7] == "#" and s[i+7][j+8] == "#"
            and s[i+8][j+5] == "." and s[i+8][j+6] == "#" and s[i+8][j+7] == "#" and s[i+8][j+8] == "#" ):
            result.append([i+1, j+1])
for i, j in result:
    print(i, j)


###C
from bisect import bisect_right, bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 10**10
A.sort()
B.sort()
for i in range(N):
    X = A[i]
    numA = i+1
    numB = M - bisect_left(B, X)
    if numA >= numB:
        ans = min(ans, X)
if A[0] < B[-1]:
    ans = B[-1]+1
print(ans)


