import sys
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a==0 and b==0 and c==0:
        break
    else:
        tri_len = [a, b, c]
        max_num = max(tri_len)
        tri_len.remove(max_num)
        
        if max_num**2 == tri_len[0]**2 + tri_len[1]**2:
            print('right')
        else:
            print('wrong')
        
