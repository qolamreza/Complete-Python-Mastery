first = [1, 2]
second = [3]
values = [*first, *second]
print(values)

first_dic = {"x": 1}
second_dic = {"x": 10, "y": 2}
combined = {**first_dic, **second_dic, "z": 1}
print(combined)