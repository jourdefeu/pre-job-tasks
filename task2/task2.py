def read_circle_data():
    circle_data = input("Координаты центра окружности через пробел: ")
    center_x, center_y = map(float, circle_data.split())
    radius = float(input("Радиус окружности: "))
    return (center_x, center_y), radius
  
def read_points_data():
    points = []
    
    print("Координаты точек (каждая точка в формате 'x y', завершить ввод можно пустой строкой):")
    while True:
        line = input()
        if line.strip() == "":  # Проверяем, если строка пустая, прерываем цикл
            break
        x, y = map(float, line.split())
        points.append((x, y))
    
    return points

def position_relative_to_circle(circle_center, radius, points):
    results = []
    cx, cy = circle_center
    for x, y in points:
        distance_squared = (x - cx) ** 2 + (y - cy) ** 2
        if distance_squared < radius ** 2:
            results.append(1)  # Точка внутри
        elif distance_squared > radius ** 2:
            results.append(2)  # Точка снаружи
        else:
            results.append(0)  # Точка лежит на окружности
    return results

# считываем данные о круге и точках
circle_center, radius = read_circle_data()
points = read_points_data()
results = position_relative_to_circle(circle_center, radius, points)

for result in results:
    print(result)
