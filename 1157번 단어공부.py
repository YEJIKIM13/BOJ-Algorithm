n = input()

def most_frequent(string):
    count = [0] * 26
    string_upper = string.upper()
    for i in string_upper:
        if i.isalpha():
            count_index = ord(i) - ord('A')
            count[count_index] += 1
    max_index = 0
    for i in range(len(count)):
        if count[i] > count[max_index]:
            max_index = i
    for j in range(len(count)):
        if max_index != j and count[max_index] == count[j]:
            return '?'
    return chr(max_index + ord('A'))


print(most_frequent(n))