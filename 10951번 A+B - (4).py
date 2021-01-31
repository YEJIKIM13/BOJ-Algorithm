# 테스트 케이스 개수가 정해지지 않음
# 에러 처리 해줄 것

while(True):
    try: 
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
