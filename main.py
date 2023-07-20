import tkinter as tk
from tkinter import filedialog

def advanced_char_counter(text):
    char_count = len(text)
    letter_count = sum(1 for char in text if char.isalpha())
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace())
    punctuation_count = char_count - letter_count - digit_count - space_count
    
    char_frequency = {}
    for char in text:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    return {
        "Total Characters": char_count,
        "Letters": letter_count,
        "Digits": digit_count,
        "Spaces": space_count,
        "Punctuation and Others": punctuation_count,
        "Character Frequency": char_frequency
    }








def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            result = advanced_char_counter(text)
            display_results(result)

def display_results(result):
    result_window = tk.Toplevel(root)
    result_window.title("Результаты подсчета символов")

    for key, value in result.items():
        tk.Label(result_window, text=f"{key}: {value}").pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Продвинутый счетчик символов")

    open_file_button = tk.Button(root, text="Открыть файл", command=open_file_dialog)
    open_file_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    text = input("Введите текст для подсчета символов: ")
    result = advanced_char_counter(text)
    print("\nРезультаты подсчета:")
    for key, value in result.items():
        print(f"{key}: {value}")
