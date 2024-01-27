

map(int, input().split())

list(map(int, input().split()))

###A
S = input()
if S[0].isupper() and (len(S)==1 or S[1:].islower()):
    print("Yes")
else:
    print("No")



###B
def most_frequent_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_freq = max(char_count.values())
    most_frequent_chars = [char for char, count in char_count.items() if count == max_freq]

    return min(most_frequent_chars)

S = input()
print(most_frequent_char(S))


###C
def max_meals(N, Q, A, B):
    max_a_meals = [q // a if a != 0 else float('inf') for q, a in zip(Q, A)]
    max_b_meals = [q // b if b != 0 else float('inf') for q, b in zip(Q, B)]

    max_total_meals = 0
    for a_meals in range(min(max_a_meals) + 1):
        b_meals = min((Q[i] - A[i] * a_meals) // B[i] if B[i] != 0 else float('inf') for i in range(N))
        max_total_meals = max(max_total_meals, a_meals + b_meals)

    return max_total_meals

N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(max_meals(N, Q, A, B))



###D
def min_tour(N, M, X):
    def direct_distance(a, b):
        return min(abs(a - b), N - abs(a - b))

    bridge_count = {i: 0 for i in range(1, N + 1)}

    total_distance = 0
    for i in range(M - 1):
        distance = direct_distance(X[i], X[i + 1])
        total_distance += distance
        if X[i] < X[i + 1]:
            for j in range(X[i], X[i + 1]):
                bridge_count[j] += 1
        else:
            for j in range(X[i + 1], X[i]):
                bridge_count[j] += 1

    least_crossed_bridge = min(bridge_count, key=bridge_count.get)

    def direct_distance_2nd(a, b):
        if ( (abs(a - b) < N - abs(a - b)) and (min(a, b) <= least_crossed_bridge < max(a, b)) or ((abs(a - b) < N - abs(a - b)) and not (min(a, b) <= least_crossed_bridge < max(a, b)) )):
            return max(abs(a - b), N - abs(a - b))
        
        else:
            return min(abs(a - b), N - abs(a - b))

    total_distance = 0
    for i in range(M - 1):
        distance = direct_distance_2nd(X[i], X[i + 1])
        total_distance += distance

    return total_distance



def min_tour(N, M, X):

    bridge_count = {i: 0 for i in range(1, N + 1)}
    for i in range(M - 1):
        if abs(X[i] - X[i+1]) <= N - abs(X[i] - X[i+1]):
            if X[i] < X[i + 1]:
                for j in range(X[i], X[i + 1]):
                    bridge_count[j] += 1
            else:
                for j in range(X[i + 1], X[i]):
                    bridge_count[j] += 1
        else:
            for j in range(max(X[i], X[i+1]), N+1):
                bridge_count[j] += 1
            for j in range(1, min(X[i], X[i+1])):
                bridge_count[j] += 1

    least_crossed_bridge = min(bridge_count, key=bridge_count.get)
    def direct_distance(a, b):
        if (min(a, b) <= least_crossed_bridge < max(a, b) and abs(a - b) <= N - abs(a - b)) or (not (min(a, b) <= least_crossed_bridge < max(a, b)) and abs(a - b) > N - abs(a - b)):
            return max(abs(a - b), N - abs(a - b))
        else:
            return min(abs(a - b), N - abs(a - b))

    total_distance = 0
    for i in range(M - 1):
        distance = direct_distance(X[i], X[i + 1])
        total_distance += distance

    return total_distance

N, M = map(int, input().split())
X = list(map(int, input().split()))

print(min_tour(N, M, X))


###E
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def sum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

def intersection(N, chords):
    endpoints = []
    for a, b in chords:
        if a > b:
            a, b = b, a
        endpoints.append((a, -1))  
        endpoints.append((b, a))  

    endpoints.sort()
    fenwick = FenwickTree(2 * N)

    for point, ref in endpoints:
        if ref == -1:  
            fenwick.add(point, 1)
        else: 
            fenwick.add(ref, -1)
            if fenwick.sum(point - 1) - fenwick.sum(ref) > 0:
                return "Yes"
    
    return "No"

N = int(input())
G = []
for _ in range(N):
    a, b = map(int, input().split())
    G.append((a, b))

print(intersection(N, G))

