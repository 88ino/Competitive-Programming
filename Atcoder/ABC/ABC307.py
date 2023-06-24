
###A###


N = int(input())
A = list(map(int, input().split()))

B=[]
for i in range(N):
    su = sum(A[i*7:(i+1)*7])
    B.append(su)


print(' '.join(map(str, B)))



###B###

N = int(input())
strings = [input() for _ in range(N)]

def is_palindrome(s):
    return s == s[::-1]

combinations = []
for i in range(len(strings)):
    for j in range(len(strings)):
        if i != j:  # 同じ文字列を2回連結しないようにする
            combinations.append(strings[i] + strings[j])

for combination in combinations:
    if is_palindrome(combination):
        print("Yes")
        break
else:
    print("No")


###C###

HA, WA = map(int, input().split())
A = [input() for _ in range(HA)]
HB, WB = map(int, input().split())
B = [input() for _ in range(HB)]
HX, WX = map(int, input().split())
X = [input() for _ in range(HX)]

def solve(HA, WA, A, HB, WB, B, HX, WX, X):
    black_cells_A = [(i, j) for i in range(HA) for j in range(WA) if A[i][j] == '#']
    black_cells_B = [(i, j) for i in range(HB) for j in range(WB) if B[i][j] == '#']
    black_cells_X = [(i, j) for i in range(HX) for j in range(WX) if X[i][j] == '#']

    for dx in range(HX):
        for dy in range(WX):
            # Shift cells of sheet A
            shifted_cells_A = [(x + dx, y + dy) for x, y in black_cells_A]
            # Combine cells of sheet A and sheet B
            for dx_b in range(HX):
                for dy_b in range(WX):
                    shifted_cells_B = [(x + dx_b, y + dy_b) for x, y in black_cells_B]
                    combined_cells_AB = shifted_cells_A + shifted_cells_B
                    if set(combined_cells_AB) == set(black_cells_X):
                        return 'Yes'
    return 'No'

print(solve(HA, WA, A, HB, WB, B, HX, WX, X))



###D###
N = int(input())
S = input()

# '(' と ')' を分離し、それぞれのインデックスを格納するリストを作成
open_indices = [i for i in range(N) if S[i] == '(']
close_indices = [i for i in range(N) if S[i] == ')']

result = list(S)  # 変更可能な形式にするために文字列をリストに変換
open_indices.append(10**10)
# それぞれの '(' に対して、それ以降の最初の ')' を見つける
for open_index in open_indices:
    for close_index in close_indices:
        if open_index == open_indices[-1]:
            break
            #次の'('が')' より先にきたらだめ
        if close_index > open_indices[open_indices.index(open_index) + 1] :
            break
        else:
            # 閉じ括弧が開き括弧より後ろにあれば削除
            if close_index > open_index:
                result[open_index] = ''
                result[close_index] = ''
                result[open_index+1:close_index] = ''
                close_indices.remove(close_index)
                break

# 空文字列を削除して結果を表示
print(''.join(result))





N = int(input())
S = input()

result = list(S)  # 変更可能な形式にするために文字列をリストに変換

# '(' のインデックスを格納するスタック
stack = []

# 各文字を順に処理
for i, ch in enumerate(result):
    if ch == '(':
        stack.append(i)
    elif ch == ')':
        if stack:
            # 対応する '(' がスタックに存在する場合は、')' を削除し、対応する '(' も削除
            opening_index = stack.pop()
            for j in range(opening_index, i+1):
                result[j] = ''

# 空文字列を削除して結果を表示
result = ''.join(result).replace('', '')
print(result)









###E###





