

###A
def find_score(N, scores):
    total_score = sum(scores)
    
    last_player_score = -total_score
    
    return last_player_score

N = int(input())
A = list(map(int, input().split()))
print(find_score(N, A))


###B
def is_good(S):
    from collections import Counter
    
    char_count = Counter(S)
    
    freq_count = Counter(char_count.values())
    
    for count in freq_count.values():
        if count != 2 and count != 0:
            return "No"
    
    return "Yes"

S = input()
print(is_good(S))


###C
def is_airport_code(S, T):
    from collections import defaultdict
    import bisect

    index_map = defaultdict(list)
    for i, char in enumerate(S):
        index_map[char].append(i)

    T = T.upper()
    n = len(S)
    
    if T[2] == 'X':
        T = T[:2]  
    
    def can_form(t):
        if t[0].lower() not in index_map:
            return False
        possible_starts = index_map[t[0].lower()]
        
        for start in possible_starts:
            if len(t) > 1 and t[1].lower() in index_map:
                pos = bisect.bisect_right(index_map[t[1].lower()], start)
                if pos < len(index_map[t[1].lower()]):
                    second_pos = index_map[t[1].lower()][pos]
                    if len(t) == 3 and t[2].lower() in index_map:
                        pos2 = bisect.bisect_right(index_map[t[2].lower()], second_pos)
                        if pos2 < len(index_map[t[2].lower()]):
                            return True
                    elif len(t) == 2:  # 2文字だけでOKの場合
                        return True
        return False

    # 3文字目がXの場合、2文字のみで判定
    if T.endswith('X'):
        return "Yes" if can_form(T[:-1]) else "No"
    
    return "Yes" if can_form(T) else "No"

S = input()
T = input()
print(is_airport_code(S, T))



###D
def subsequences(L, R):
    results = []
    max_power = 60  # 2^60 まで考慮
    while L < R:
        # 使える最大のべき乗を見つける
        power_used = False
        for i in range(max_power, -1, -1):
            power = 1 << i
            if L + power <= R and L % power == 0:
                results.append((L, L + power))
                L += power
                power_used = True
                break
        # 見つからなかった場合、最小の適合するべき乗で進める
        if not power_used:
            # 次の2のべき乗にLを合わせる
            next_power = 1 << (L.bit_length())
            if L & (next_power - 1) != 0:
                next_power >>= 1
            results.append((L, L + next_power))
            L += next_power

    return len(results), results

L, R = map(int, input().split())

m, segments = subsequences(L, R)
print(m)
for l, r in segments:
    print(l, r)


###E
def has_winner(board, player):
    p = player
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == p:
            return True
        if board[0][i] == board[1][i] == board[2][i] == p:
            return True
    if board[0][0] == board[1][1] == board[2][2] == p:
        return True
    if board[0][2] == board[1][1] == board[2][0] == p:
        return True
    return False

def minimax(board, depth, is_maximizing, scores, current_score_t, current_score_a):
    if has_winner(board, 'T'):
        return 10
    if has_winner(board, 'A'):
        return -10
    if depth == 9:
        return current_score_t - current_score_a
    
    best_score = -float('inf') if is_maximizing else float('inf')
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  
                board[i][j] = 'T' if is_maximizing else 'A'
                score = minimax(board, depth+1, not is_maximizing, scores, 
                                current_score_t + (scores[i][j] if is_maximizing else 0),
                                current_score_a + (scores[i][j] if not is_maximizing else 0))
                board[i][j] = 0
                if is_maximizing:
                    best_score = max(best_score, score)
                else:
                    best_score = min(best_score, score)
                    
    return best_score

def determine_winner(scores):
    board = [[0]*3 for _ in range(3)]
    result = minimax(board, 0, True, scores, 0, 0)
    return "Takahashi" if result > 0 else "Aoki"

import sys
input = sys.stdin.read
data = input().split()
scores = [list(map(int, data[i*3:(i+1)*3])) for i in range(3)]

winner = determine_winner(scores)
print(winner)

###F
