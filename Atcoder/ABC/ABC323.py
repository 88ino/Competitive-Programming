
map(int, input().split())

list(map(int, input().split()))


###A
S = input()
for i in range(1, 16, 2):
    if S[i] == "1":
        print("No")
        exit()
print("Yes")


###B
def player_rankings(N, results):
    wins = [(s.count('o'), i) for i, s in enumerate(results, 1)]
    sorted_players = sorted(wins, key=lambda x: (-x[0], x[1]))
    ranking = [p[1] for p in sorted_players]
    return ranking

N = int(input())
results = [input() for _ in range(N)]
rankings = player_rankings(N, results)
print(*rankings)

###C
def min_to_win(N, M, scores, players_status):
    results = []
    total_scores = [sum(scores[i] for i, s in enumerate(status) if s == 'o') + (idx+1) for idx, status in enumerate(players_status)]
    
    for idx, status in enumerate(players_status):
        unsolved_scores = sorted([scores[i] for i, s in enumerate(status) if s == 'x'], reverse=True)
        max_other_score = max(total_scores[:idx] + total_scores[idx+1:])
        current_score = total_scores[idx]
        count = 0
        for score in unsolved_scores:
            if current_score > max_other_score:
                break
            current_score += score
            count += 1
        
        results.append(count)
    
    return results

N, M = map(int, input().split())
scores = list(map(int, input().split()))
players_status = [input() for _ in range(N)]

results = min_to_win(N, M, scores, players_status)
for res in results:
    print(res)

###D
import heapq

def min_slimes(N, slimes):

    heap = [size for size, count in slimes]
    heapq.heapify(heap)
    size_to_count = {size: count for size, count in slimes}

    result = 0
    while heap:
        size = heapq.heappop(heap)
        count = size_to_count[size]
        result += count % 2 
        new_count = count // 2
        
        if new_count == 0:  
            continue
        
        new_size = size * 2
        if new_size in size_to_count:
            size_to_count[new_size] += new_count
        else:
            size_to_count[new_size] = new_count
            heapq.heappush(heap, new_size)

    return result

state = []
N = int(input())
for _ in range(N):
    s, c = map(int, input().split())
    state.append([s, c])

result = min_slimes(N, state)
print(result)
    


###E




