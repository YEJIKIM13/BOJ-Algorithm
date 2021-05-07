import math

A, B, V = map(int, input().split())
# 정상까지 올라갔다 밤에 미끄러지고 다시 올라가는 불상사 방지 
day = (V - B) / (A - B)  # 정상에 한 번 도달하면 밤에 미끄러지지 않는 것까지 미리 고려한 것, 미리 빼고 계산 -> V - B

print(math.ceil(day))