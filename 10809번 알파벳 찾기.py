S = input()
answer = [-1] * 26

# 필요한 게 뭔지 생각해보기!
# S의 인덱스 i에 해당하는 알파벳이 _니까
# answer 배열의 _의 인덱스화된 인덱스에 i가 들어가야 한다는 것

for i in range(len(S)):
    answer_i = ord(S[i]) - ord('a')
    if answer[answer_i] == -1:
        answer[answer_i] = i

for i in range(len(answer)):
    print(answer[i], end=' ')
