import sys

n = int(sys.stdin.readline())
sum_score = 0
count = 1

for _ in range(n):
    list_input = list(sys.stdin.readline())
    for i in range(len(list_input)):
        if i == 0 and list_input[i] == 'O':
            sum_score += count
        elif list_input[i-1] == 'O' and list_input[i] == 'O':
            count += 1
            sum_score += count
        elif list_input[i-1] == 'X' and list_input[i] == 'O':
            count = 1
            sum_score += count

    print(sum_score)
    sum_score = 0
    count = 1  # count와 sum_score을 초기화해야 반복문 다시 돌려도 잘 돌아감! 