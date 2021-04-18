from itertools import combinations

N, M = map(int, input().split())

L = list(map(int, input().split()))
    
sum_list = []
for i in combinations(L, 3):
    a = sum(i)
    if a <= M:
        sum_list.append(a)

print(max(sum_list))