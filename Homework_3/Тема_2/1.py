import math

vector = []
while len(vector) == 0:
    new_vector = input("Введите координаты вектора (x, y, z) без скобок через запятую: ").split(",")
    try:
        vector = [int(i) for i in new_vector]
        if len(vector) == 3:
            a, b, c = vector
            vector_length = math.sqrt(a**2 + b**2 + c**2)
            print(f"Длина вектора равна {vector_length}")
        else:
            print("Необходимо ввести 3 числа (x, y, z). Повторите ввод, пожалуйста.")
            vector = []
    except ValueError:
        print("Вы ввели посторонний символ. Повторите ввод, пожалуйста.")
