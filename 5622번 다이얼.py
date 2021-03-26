n = input()
count = 0
num_list = []

for letter in n:
    if ord('A') <= ord(letter) <= ord('C'):
        num_list.append(3)
    elif ord('D') <= ord(letter) <= ord('F'):
        num_list.append(4)
    elif ord('G') <= ord(letter) <= ord('I'):
        num_list.append(5)
    elif ord('J') <= ord(letter) <= ord('L'):
        num_list.append(6)
    elif ord('M') <= ord(letter) <= ord('O'):
        num_list.append(7)
    elif ord('P') <= ord(letter) <= ord('S'):
        num_list.append(8)
    elif ord('T') <= ord(letter) <= ord('V'):
        num_list.append(9)
    elif ord('W') <= ord(letter) <= ord('Z'):
        num_list.append(10)
        
print(sum(num_list))