


###A
def filter(N, K, A):
    result = [a // K for a in A if a % K == 0]
    return ' '.join(map(str, result))

N, K = map(int, input().split())
A = list(map(int, input().split()))
print(filter(N, K, A))



###B
def unique_substrings(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return len(substrings)

S = input()
print(unique_substrings(S))



###C
def holidays_efficient(N, A, B, D):
    W = A + B
    D_mod = [d % W for d in D]
    D_mod = sorted(set(D_mod))  

    if len(D_mod) > A:  
        return "No"

    for i in range(len(D_mod) - 1):
        if D_mod[i + 1] - D_mod[i] > B:
            return "Yes"

    if D_mod[0] + W - D_mod[-1] > B:
        return "Yes"

    return "No"

N, A, B = map(int, input().split())
D = list(map(int, input().split()))
print(holidays_efficient(N, A, B, D))



###D
def find_X_Y(a, b, C):
    D = bin(C).count('1')

    for d in range(D + 1):
        remaining_a = a - d
        remaining_b = b - (D - d)
        if remaining_a == remaining_b >= 0:
            X = Y = 0
            for bit in range(60):
                if (C >> bit) & 1:
                    if d > 0:
                        X |= 1 << bit
                        d -= 1
                    else:
                        Y |= 1 << bit
                else:
                    if remaining_a > 0:
                        X |= 1 << bit
                        Y |= 1 << bit
                        remaining_a -= 1
            return X, Y

    return -1

a, b, C = map(int, input().split())
result = find_X_Y(a, b, C)
if result == -1:
    print(-1)
else:
    print(result[0], result[1])




###E
def process_queries_efficient(N, Q, queries):
    A = [0] * N  
    S = set()  
    updates = [0] * (N + 1)  
    
    current_size = 0
    
    for x in queries:
        if x in S:
            S.remove(x)
            current_size -= 1
        else:
            S.add(x)
            current_size += 1
        
        updates[x-1] += 1
    
    for i in range(N):
        if i+1 in S:
            A[i] = updates[i] + (current_size - 1) * Q 
        else:
            A[i] = updates[i] + current_size * Q  
    
    return ' '.join(map(str, A))

N, Q = map(int, input().split())
queries = list(map(int, input().split()))
print(process_queries_efficient(N, Q, queries))

