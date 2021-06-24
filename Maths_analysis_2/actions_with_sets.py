A = {1, 2, 3, "hello", 14}
B = {1, 2, 0.25, "k", 79}
C = {1/3, 2, 3, "maths"}
U = {1, 2, 3, "hello", 14, 0.25, "k", 79, 1/3, "maths"}

print("Дополнение A:", U - A)
print("Дополнение B:", U - B)
print("Дополнение С:", U - C)

print("Объединение A и B:", A.union(B))
print("Объединение A и C:", A.union(C))
print("Объединение C и B:", C.union(B))

print("Пересечение A и B:", A.intersection(B))
print("Пересечение A и C:", A.intersection(C))
print("Пересечение C и B:", C.intersection(B))

print("Разность A и B:", A.difference(B))
print("Разность B и A:", B.difference(A))
print("Разность A и C:", A.difference(C))
print("Разность С и А:", C.difference(A))
print("Разность C и B:", C.difference(B))
print("Разность В и С:", B.difference(C))

print("Симметрическая разность A и B:", A.symmetric_difference(B))
print("Симметрическая разность A и C:", A.symmetric_difference(C))
print("Симметрическая разность C и B:", C.symmetric_difference(B))
