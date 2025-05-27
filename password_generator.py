from PIL import Image, ImageTk
import tkinter as tk
import random
import string

window = tk.Tk()
window.title("Random Password Generator")
window.geometry("600x400")
window.resizable(False, False)

bg_image = Image.open("password_generator-main/ranger-4df6c1b6.png").resize((600, 400))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(window, text="Password length (max 30):", font=("Segoe UI", 11, "bold"), fg="#333")
label.pack(pady=10)

entry = tk.Entry(window, width=10, justify="center", font=("Segoe UI", 14), fg="#222")
entry.pack()


result_label = tk.Label(window, text="", font=("Courier New", 10, "bold"), fg="#111")
result_label.pack(pady=5)

def generate_password():
    try:
        length = int(entry.get())
        if length > 30:
            result_label.config(text="Max 30 characters!")
            return
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
        window.clipboard_clear()
        window.clipboard_append(password)
    except ValueError:
        result_label.config(text="Please enter a valid number!")

def pulse_button(btn, color1="#2196F3", color2="#FFD700", pulses=3, delay=150):
    def _pulse(count=0):
        if count >= pulses * 2:
            btn.config(bg=color1)  
            return
        
        btn.config(bg=color2 if count % 2 == 0 else color1)
        btn.after(delay, _pulse, count + 1)
    _pulse()

def copy_password():
    password = result_label.cget("text")
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        pulse_button(copy_button)
        copy_button.config(text="Copied to clipboard")
    window.after(1500, lambda: copy_button.config(text="Copy Password"))

button = tk.Button(
    window, text="Generate Password", command=generate_password,
    bg="#4CAF50", fg="white", relief='flat', highlightthickness=0,
    font=("Segoe UI", 11, "bold"), padx=10, pady=5
)
button.config(bg="#4CAF50", fg="white", font=("Segoe UI", 11, "bold"), activebackground="#FFA500")
button.pack(pady=(0, 20))


copy_button = tk.Button(
    window, text="Copy Password", command=copy_password,
    bg="#2196F3", fg="white", relief='flat', highlightthickness=0,
    font=("Segoe UI", 11, "bold"), padx=10
)
copy_button.pack(pady=(0, 15), ipady=10)


def on_validate(P):
    return len(P) <= 2 and (P.isdigit() or P == "")

vcmd = window.register(on_validate)
entry.config(validate="key", validatecommand=(vcmd, '%P'))

message = tk.Label(window, text= "Made by Adam de Haseth with Python and VS Code.", font=("Segoe UI", 9, "italic"), bg=window["bg"], fg="#000", borderwidth=0, highlightthickness=0)
message.place(relx=0.5, rely=0.95, anchor="center")
window.mainloop()









































window.mainloop()
