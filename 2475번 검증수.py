num_list = list(map(int, input().split()))
r_sum = 0
for i in num_list:
    r_sum += i*i
print(r_sum % 10)