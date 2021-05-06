X = int(input())

line = 0  # 사선라인
max_num = 0  # 입력 숫자라인에서 가장 큰 수 (번호 기준)

while X > max_num:
    line += 1
    max_num += line
    
diff = max_num - X  # 번호 기준, 차이가 클 수록 앞 번호
if line % 2 == 0:  # 짝수라인은 분모에 수가 큰 것부터 시작 
    top = line - diff
    under = diff + 1
else: 
    top = diff + 1
    under = line - diff

print(f'{top}/{under}')    