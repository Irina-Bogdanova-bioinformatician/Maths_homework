import math

R, alpha = input("Введите значение полярных координат R и alpha (в градусах) через запятую: ").split(",")
R, alpha = int(R), int(alpha)
x = R * math.cos(math.radians(alpha))
y = R * math.sin(math.radians(alpha))
print(f"Декартовы координаты (x, y): ({x}:{y})")
