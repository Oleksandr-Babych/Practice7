import random

def generate_random_numbers(n):
    """Генерує список n випадкових чисел в діапазоні від 1 до 100."""
    return [random.randint(1, 100) for _ in range(n)]

def calculate_average(numbers):
    """Обчислює середнє арифметичне чисел у списку."""
    return sum(numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    # Calculate the standard deviation
    if len(numbers) < 2:
        return 0  # Standard deviation is not defined for less than 2 numbers

    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_deviation = math.sqrt(variance)

    return std_deviation