for _ in range(int(input())):
    H, W, N = map(int, input().split())
    
    floor = N % H
    number = (N // H) + 1
    
    if floor == 0:
        floor = H
        number = N // H
        
    print((100 * floor) + number)