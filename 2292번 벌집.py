N = int(input())

rooms = 1
count = 1
while N > rooms:
    rooms += 6 * count
    count += 1

print(count)