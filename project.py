import random
import string
import tkinter as tk


def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_label.config(text=password)


root = tk.Tk()
root.title("Генератор паролей")

length_label = tk.Label(root, text="Длина пароля:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()
