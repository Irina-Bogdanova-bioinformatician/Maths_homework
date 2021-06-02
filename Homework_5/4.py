import itertools

permutations_list_1 = []
for p in itertools.permutations("012345", 3):
    permutations_list_1.append("".join(str(x) for x in p))
number_1 = 6 * 5 * 4
print(f"Число размещений 3 объектов из 6 равно {number_1}.")
print(f"Список размещений 3 объектов из 6: {permutations_list_1}")
permutations_list_2 = []
for p in itertools.permutations("01234", 5):
    permutations_list_2.append("".join(str(x) for x in p))
number_2 = 5 * 4 * 3 * 2 * 1
print(f"Число перестановок 5 объектов равно {number_2}.")
print(f"Список перестановок 5 объектов: {permutations_list_2}")
combinations_list = []
for p in itertools.combinations("01234", 3):
    combinations_list.append("".join(str(x) for x in p))
number_3 = (5 * 4 * 3 * 2 * 1) / 12
print(f"Число сочетаний 3 объектов из 5 равно {number_3}.")
print(f"Список сочетаний 3 объектов из 5: {combinations_list}")
