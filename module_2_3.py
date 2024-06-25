my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
plus_numder = []
i = 0


while i < len(my_list):
    if my_list[i] == 0:
        i += 1
        continue
    if my_list[i] <= 0:
        break
    plus_numder.append(my_list[i])
    i += 1

print(plus_numder)
