
list(map(int, input().split()))

map(int, input().split())



###A
A, B = map(int, input().split())
print(A**B+B**A)





###B
S = input()

def max_palindrome_length(s: str) -> int:
    n = len(s)
    res = 1  

    for i in range(n):
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            res = max(res, r - l + 1)
            l -= 1
            r += 1

    for i in range(n - 1):
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            res = max(res, r - l + 1)
            l -= 1
            r += 1

    return res
print(max_palindrome_length(S))

###C
M = int(input())
S1 = list(map(int, list(input())))*3
S2 = list(map(int, list(input())))*3
S3 = list(map(int, list(input())))*3
sec = []
for i in range(M):
    for j in range(i+1, M*2):
        if S2[j] == S1[i]:
            for k in range(j+1, M*3):
                if S3[k] == S1[i]:
                    sec.append(k)

for i in range(M):
    for j in range(i+1, M*2):
        if S3[j] == S1[i]:
            for k in range(j+1, M*3):
                if S2[k] == S1[i]:
                    sec.append(k)
                    
for i in range(M):
    for j in range(i+1, M*2):
        if S1[j] == S2[i]:
            for k in range(j+1, M*3):
                if S3[k] == S2[i]:
                    sec.append(k)

for i in range(M):
    for j in range(i+1, M*2):
        if S3[j] == S2[i]:
            for k in range(j+1, M*3):
                if S1[k] == S2[i]:
                    sec.append(k)

for i in range(M):
    for j in range(i+1, M*2):
        if S1[j] == S3[i]:
            for k in range(j+1, M*3):
                if S2[k] == S3[i]:
                    sec.append(k)            

for i in range(M):
    for j in range(i+1, M*2):
        if S2[j] == S3[i]:
            for k in range(j+1, M*3):
                if S1[k] == S3[i]:
                    sec.append(k)

if len(sec)==0:
    print(-1)
else:
    print(min(sec))

        

###D
from collections import defaultdict, deque

def find_coordinates(N, M, relations):
    graph = defaultdict(list)
    for a, b, x, y in relations:
        graph[a].append((b, x, y))
        graph[b].append((a, -x, -y))

    visited = set()
    coords = [(float('inf'), float('inf'))] * (N + 1)
    coords[1] = (0, 0)
    queue = deque([1])

    while queue:
        current = queue.popleft()
        x_current, y_current = coords[current]

        for neighbor, dx, dy in graph[current]:
            if neighbor in visited:
                if coords[neighbor] != (x_current + dx, y_current + dy):
                    return ["undecidable"] * N
            else:
                visited.add(neighbor)
                coords[neighbor] = (x_current + dx, y_current + dy)
                queue.append(neighbor)

    return coords[1:]

N, M = map(int, input().split())
relations = [tuple(map(int, input().split())) for _ in range(M)]
results = find_coordinates(N, M, relations)

for res in results:
    if res[0]==float('inf'):
        print("undecidable")
    else:
        print(res[0], res[1])


###E
from collections import deque
import heapq

def get_noodles_amount(N, M, events):
    noodles = [0] * N
    queue = deque(list(range(N)))  
    outside = {} 
    events = sorted(events, key=lambda x: x[0])

    for t, w, s in events:
        # Append back people who have returned till time t
        return_times = list(outside.keys())
        for return_time in sorted(return_times):
            if return_time <= t:
                queue.appendleft(outside.pop(return_time))  

        if queue:
            person = queue.popleft()
            noodles[person] += w
            outside[t + s] = person

    return noodles

N, M = map(int, input().split())
events = [tuple(map(int, input().split())) for _ in range(M)]

results = get_noodles_amount(N, M, events)

for res in results:
    print(res)




