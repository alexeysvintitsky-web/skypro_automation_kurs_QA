import math

def square(side):

    area = side * side

    if not isinstance(side, int):
     area = math.ceil(area)

    return area

side1 = 5
result1 = square(side1)
print(f"Сторона: {side1}, Площадь: {result1}")

side2 = 4.3
result2 = square(side2)
print(f"Сторона: {side2}, Площадь: {result2}")

side3 = 3.5
result3 = square(side3)
print(f"Сторона: {side3}, Площадь: {result3}")