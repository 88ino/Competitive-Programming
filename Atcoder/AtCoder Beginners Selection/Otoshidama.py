N, Y = map(int, input().split())
a = 10000
b = 5000
c = 1000
x = -1
y = -1
z = -1
for i in range (N+1):
    for j in range(N+1-i):
        k = N-i-j
        if a*i + b*j + c*k == Y:
            x = i
            y = j
            z = k
            break

print("{} {} {}".format(x, y, z) )