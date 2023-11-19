import PySimpleGUI as sg
from module import generate_random_numbers, calculate_average
from database import config

def create_layout():
    return [
        [sg.Text("Натисніть на кнопку, щоб згенерувати випадкові числа та обчислити середнє арифметичне.")],
        [sg.Button("Генерувати числа"), sg.Button("Export to File"), sg.Exit()],
        [sg.Output(size=(40, 10))]
    ]

def main():
    layout = create_layout()
    window = sg.Window("Графічний Інтерфейс", layout, resizable=True)
    
    random_numbers = []  

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Генерувати числа":
            random_numbers = generate_random_numbers(10)
            average = calculate_average(random_numbers)
            print("Список випадкових чисел:", random_numbers)
            print("Середнє арифметичне:", average)
            print("\n" + "="*40 + "\n")
        elif event == "Export to File":
            try:
                save_to_file(random_numbers, average)
            except Exception as e:
                print(f"Error saving to file: {e}")

    window.close()

def save_to_file(numbers, avg):
    filename = sg.popup_get_file("Зберегти у файл", save_as=True, default_extension=".txt", file_types=(("Text Files", "*.txt"),))

    if filename:
        if not filename.lower().endswith(".txt"):
            filename += ".txt"

        with open(filename, "w") as file:
            file.write("Список випадкових чисел: {}\n".format(numbers))
            file.write("Середнє арифметичне: {}\n".format(avg))
        print("Дані успішно збережено в файлі: {}".format(filename))

if __name__ == "__main__":
    main()