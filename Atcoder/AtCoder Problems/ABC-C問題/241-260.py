# 241
def cal(x, y, dx, dy):
    count = 0
    for i in range(6):
        if min(x, y) < 0 or max(x, y) >= N:
            return  False
        if S[x][y] == "#":
            count += 1
        x += dx
        y += dy

    return count >= 4

N = int(input())
S = [input() for _ in range(N)]
direction = [(0, 1), (1, 0), (1, 1), (-1, 1)]
for a in direction:
    dx, dy = a
    for x in range(N):
        for y in range(N):
            if cal(x, y, dx, dy):
                print("Yes")
                exit()
print("No")


# 242



# 243



# 244



# 245



# 246



# 247



# 248



# 249



# 250



# 251



# 252



# 253



# 254



# 255



# 256



# 257



# 258



# 259



# 260



