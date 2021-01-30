import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    R, S = sys.stdin.readline().split()
    S_list = list(S)
    R = int(R)
    for i in range(len(S_list)):
        S_list[i] = (S_list[i]) * R
    print(''.join(S_list))