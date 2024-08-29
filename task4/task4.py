user_input = input("Введите числа через пробел: ")
numbers = list(map(int, user_input.split()))

def calculate_minimum_moves(nums):
    nums.sort()  # сортируем массив для поиска медианы
    n = len(nums)

    # находим медиану
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = (nums[n // 2 - 1] + nums[n // 2]) // 2

    # считаем количество ходов
    moves = sum(abs(x - median) for x in nums)

    return moves

result = calculate_minimum_moves(numbers)

print(f"Минимальное количество ходов: {result}")
