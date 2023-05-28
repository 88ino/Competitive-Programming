

# A #
from collections import Counter
N = int(input())
A = list(map(int, input().split()))

A.sort()

def count_most_frequent(lst):
    counter = Counter(lst)
    most_common = counter.most_common(1)
    return most_common[0][1]

def get_most_frequent(lst):
    counter = Counter(lst)
    most_common = counter.most_common(1)
    return most_common[0][0]

result = count_most_frequent(A)
num = get_most_frequent(A)
if result <= N//2:
    print("Yes")
elif result == N//2 + 1:
    if num == A[0]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
    


### 
### 奇数が隣り合う偶数より小さいように並べる
### ソートし、半分を昇順に並べ、間にもう半分を入れる？
###



# B #
def find_max_binary(N):
    count_of_1 = bin(N).count('1')  # Nの2進表記に含まれる1の数を数える

    while count_of_1 != 3:
        if count_of_1 < 3:
            N -= 1
        else:
            rightmost_1_bit = N & -N  # Nの最も右の1ビットを抽出する
            N ^= rightmost_1_bit  # 最も右の1ビットを0に反転する
        count_of_1 = bin(N).count('1')

    return N

T = int(input())  # テストケースの数を読み込む
for _ in range(T):
    N = int(input())  # テストケースを読み込む
    if N <= 6:
        print(-1)
    else:
        print(find_max_binary(N))  # 結果を出力する




# C #










# D # 





