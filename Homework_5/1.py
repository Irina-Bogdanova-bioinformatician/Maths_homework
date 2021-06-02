import numpy as np

a = input("Нажмите enter, чтобы начать")
while True:
    x = np.random.randint(0, 37)
    print(x)
    b = input("Нажмите enter, чтобы продолжить. Введите stop для завершения программы.")
    if b == 'stop':
        break
