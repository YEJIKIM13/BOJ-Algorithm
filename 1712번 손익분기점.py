A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))

# A+B*n = C*n 일 때 수입과 비용이 같아진다.
# B>=C 일 경우에 손익분기점이 나타나지 않게 되므로 먼저 걸러낸다.
# 따라서, A/(C-B) 대 생산했을 때 수입과 비용이 같아지니까 그 이상이 되려면 +1 해줘야 함.

