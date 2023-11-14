import PySimpleGUI as sg
from module import generate_random_numbers, calculate_average
from database import config

def main():
    # Оновлений макет з додаванням кнопки "Export to File"
    layout = [
        [sg.Text("Натисніть на кнопку, щоб згенерувати випадкові числа та обчислити середнє арифметичне.")],
        [sg.Button("Генерувати числа"), sg.Button("Export to File"), sg.Exit()],
        [sg.Output(size=(40, 10))]
    ]

    # Створення вікна з новим макетом
    window = sg.Window("Графічний Інтерфейс", layout, resizable=True)

    while True:
        # Очікування подій вікна
        event, values = window.read()

        # Обробка подій
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Генерувати числа":
            # Генерація чисел та обчислення середнього
            random_numbers = generate_random_numbers(10)
            average = calculate_average(random_numbers)

            # Виведення результатів у вікно
            print("Список випадкових чисел:", random_numbers)
            print("Середнє арифметичне:", average)
            print("\n" + "="*40 + "\n")
        elif event == "Export to File":
            # Виклик функції для збереження результатів у файл
            save_to_file(random_numbers, average)

    # Закриття вікна при виході з циклу
    window.close()

def save_to_file(numbers, avg):
    # Вивід діалогового вікна для отримання імені файлу
    filename = sg.popup_get_file("Зберегти у файл", save_as=True, default_extension=".txt")

    if filename:
        # Додаємо розширення .txt, якщо воно відсутнє
        if not filename.lower().endswith(".txt"):
            filename += ".txt"

        # Запис результатів у вказаний файл
        with open(filename, "w") as file:
            file.write("Список випадкових чисел: {}\n".format(numbers))
            file.write("Середнє арифметичне: {}\n".format(avg))
        print("Дані успішно збережено в файлі: {}".format(filename))

if __name__ == "__main__":
    main()