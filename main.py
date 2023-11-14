import PySimpleGUI as sg
from module import generate_random_numbers, calculate_average
from database import config

class NumberGenerator:
    def __init__(self, count):
        self.count = count

    def generate_numbers(self):
        return generate_random_numbers(self.count)

class AverageCalculator:
    @staticmethod
    def calculate(numbers):
        return calculate_average(numbers)

class FileHandler:
    @staticmethod
    def save_to_file(filename, numbers, avg):
        if not filename.lower().endswith(".txt"):
            filename += ".txt"

        with open(filename, "w") as file:
            file.write(f"Список випадкових чисел: {numbers}\n")
            file.write(f"Середнє арифметичне: {avg}\n")

def main():
    layout = [
        [sg.Text("Натисніть на кнопку, щоб згенерувати випадкові числа та обчислити середнє арифметичне.")],
        [sg.Button("Генерувати числа"), sg.Button("Export to File"), sg.Exit()],
        [sg.Output(size=(40, 10))]
    ]

    window = sg.Window("Графічний Інтерфейс", layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Генерувати числа":
            random_numbers = NumberGenerator(10).generate_numbers()
            average = AverageCalculator.calculate(random_numbers)
            print_results(random_numbers, average)
        elif event == "Export to File":
            save_to_file_window()

    window.close()

def print_results(numbers, average):
    print("Список випадкових чисел:", numbers)
    print("Середнє арифметичне:", average)
    print("\n" + "="*40 + "\n")

def save_to_file_window():
    filename = sg.popup_get_file("Зберегти у файл", save_as=True, default_extension=".txt")
    if filename:
        save_to_file(filename)

def save_to_file(filename):
    numbers = NumberGenerator(10).generate_numbers()
    average = AverageCalculator.calculate(numbers)
    FileHandler.save_to_file(filename, numbers, average)
    print(f"Дані успішно збережено в файлі: {filename}")

if __name__ == "__main__":
    main()