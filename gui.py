import tkinter as tk
from voice import take_command
from commands import process_command

def start_assistant(text_area):
    command = take_command()
    text_area.insert(tk.END, "You: " + command + "\n")
    process_command(command)

def create_gui():
    root = tk.Tk()
    root.title("AI Assistant")
    root.geometry("500x500")

    text_area = tk.Text(root, height=15, width=50)
    text_area.pack(pady=10)

    button = tk.Button(
        root,
        text="Start Listening",
        command=lambda: start_assistant(text_area)
    )
    button.pack(pady=20)

    root.mainloop()