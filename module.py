import random

def generate_random_numbers(n):
    """Генерує список n випадкових чисел в діапазоні від 1 до 100."""
    return [random.randint(1, 100) for _ in range(n)]

def calculate_average(numbers):
    """Обчислює середнє арифметичне чисел у списку."""
    return sum(numbers) / len(numbers)
