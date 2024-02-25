


###A
S = list(input())
a = S[0]
b = S[1]
c = S[2]
if a==b==c:
    flag =True
else:
    flag = False
if flag:
    for i in range(len(S)):
        if S[i] != a:
            print(i+1)
            exit()
else:
    if a==b:
        print(3)
    elif b==c:
        print(1)
    else:
        print(2)


###B
def process_queries(N, P, Q, queries):
    index_dict = {person: index for index, person in enumerate(P)}
    
    for A, B in queries:
        if index_dict[A] < index_dict[B]:
            print(A)
        else:
            print(B)

N = int(input())
P = list(map(int, input().split()))
Q = int(input())
queries = []
for _ in range(Q):
    a, b = map(int, input().split())
    queries.append((a, b))

process_queries(N, P, Q, queries)


###C
def replace_characters(N, S, Q, operations):
    replacement = {chr(ord('a') + i): chr(ord('a') + i) for i in range(26)}

    for c, d in operations:
        for key, value in replacement.items():
            if value == c:
                replacement[key] = d

    result = "".join(replacement[char] for char in S)
    return result

N = int(input())
S = input()
Q = int(input())
op = []
for _ in range(Q):
    c, d = input().split()
    op.append((c,d))

print(replace_characters(N, S, Q, op))



###D
from collections import defaultdict
from math import gcd

def prime_factors(n):
    factors = defaultdict(int)
    while n % 2 == 0:
        factors[2] += 1
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors[i] += 1
            n //= i
    if n > 2:
        factors[n] += 1
    return factors

def count_pairs(N, A):
    factor_counts = defaultdict(int)
    for a in A:
        factors = prime_factors(a)
        reduced_factors = tuple((p, e % 2) for p, e in factors.items())
        factor_counts[reduced_factors] += 1

    count = 0
    for c in factor_counts.values():
        count += c * (c - 1) // 2
    return count

N = int(input())
A = list(map(int, input().split()))
print(count_pairs(N, A))



###E
N, M = map(int, input().split())
st = []
for _ in range(M):
    l, d, k, c, A, B = map(int, input().split())
    st.append((l, d, k, c, A, B))



