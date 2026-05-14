import tkinter as tk

questions = [
    {"question": "What is the name of the library we used to create the window?", "options": ["tkinter", "pygame", "django", "flask"], "answer": "tkinter"},
    {"question": "Which command creates the main window?", "options": ["tk.Window()", "tk.Tk()", "tk.Frame()", "tk.Canvas()"], "answer": "tk.Tk()"},
    {"question": "What widget shows text on the screen?", "options": ["Button", "Entry", "Label", "Text"], "answer": "Label"},
    {"question": "What function starts the app and keeps it running?", "options": ["window.start()", "window.run()", "window.mainloop()", "window.show()"], "answer": "window.mainloop()"},
    {"question": "What do we use to store the user's answer?", "options": ["tk.IntVar()", "tk.StringVar()", "tk.DoubleVar()", "tk.BooleanVar()"], "answer": "tk.StringVar()"},
    {"question": "What widget do we use for multiple choice (like this quiz)?", "options": ["Checkbutton", "Radiobutton", "Button", "Listbox"], "answer": "Radiobutton"},
    {"question": "What does the pack() function do?", "options": ["Deletes widget", "Hides widget", "Places widget on screen", "Changes color"], "answer": "Places widget on screen"},
    {"question": "What function changes widget properties?", "options": ["edit()", "change()", "config()", "set()"], "answer": "config()"},
    {"question": "What is the correct way to set window title?", "options": ["window.text()", "window.title()", "window.name()", "window.label()"], "answer": "window.title()"},
    {"question": "What does the command parameter in Button do?", "options": ["Changes color", "Sets size", "Calls a function when clicked", "Adds image"], "answer": "Calls a function when clicked"}
]

current = 0
score = 0

def load():
    q = questions[current]
    label.config(text=q["question"])
    var.set(None)
    for i in range(4):
        options[i].config(text=q["options"][i], value=q["options"][i])

def next():
    global current, score
    if var.get() == questions[current]["answer"]:
        score = score + 1
    if current < len(questions) - 1:
        current = current + 1
        load()
    else:
        label.config(text=f"Your Score: {score}/{len(questions)}")
        for i in options:
            i.pack_forget()
        button.pack_forget()

window = tk.Tk()
window.title("Quiz App")
window.geometry("500x400")

label = tk.Label(window, text="", font=("Arial", 14), wraplength=450)
label.pack(pady=20)

var = tk.StringVar()

options = []
for i in range(4):
    rb = tk.Radiobutton(window, text="", variable=var, value="", font=("Arial", 12))
    rb.pack(anchor="w", padx=20)
    options.append(rb)

button = tk.Button(window, text="Next", command=next, bg="green", fg="white")
button.pack(pady=20)

load()
window.mainloop ()
