N = int(input())
flag = 0
x_o=0
y_o=0
t_o=0
for _ in range(N):
    t, x, y = map(int, input().split())

    dis = abs(x-x_o) + abs(y-y_o)
    time = t-t_o

    t_o=t
    x_o=x
    y_o=y

    if time < dis:
        flag = 1
    elif time%2 != dis%2:
        flag = 1
if flag == 0:
    print("Yes")
else:
    print("No")