import sys
n = int(sys.stdin.readline())

group_word = 0

for _ in range(n):
    string = sys.stdin.readline()
    error_count = 0
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            new_string = string[i+1:]
            if new_string.count(string[i]) != 0:
                error_count += 1
    if error_count == 0:
        group_word += 1 

print(group_word)
