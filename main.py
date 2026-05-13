import tkinter as tk
from tkinter import ttk

questions = [
    {
        "question": "What is the default Python library used for creating GUI applications in this project?",
        "options": ["PyQt", "Tkinter", "Kivy", "wxPython"],
        "answer": "Tkinter"
    },
    {
        "question": "Which Git command is used to download a repository from GitHub?",
        "options": ["git push", "git clone", "git commit", "git pull"],
        "answer": "git clone"
    },
    {
        "question": "What does the 'git pull origin main' command do?",
        "options": [
            "Uploads code to GitHub",
            "Downloads latest changes from GitHub",
            "Creates a new branch",
            "Deletes the repository"
        ],
        "answer": "Downloads latest changes from GitHub"
    },
    {
        "question": "In Tkinter, which widget is used to display text in this app?",
        "options": ["Entry", "Label", "Text", "Canvas"],
        "answer": "Label"
    },
    {
        "question": "What function is used to start the Tkinter event loop?",
        "options": ["window.loop()", "tk.start()", "window.mainloop()", "tk.run()"],
        "answer": "window.mainloop()"
    },
    {
        "question": "Which command shows the current branch name in Git?",
        "options": ["git branch", "git status", "git log", "git checkout"],
        "answer": "git branch"
    },
    {
        "question": "What does 'tk.StringVar()' do in this code?",
        "options": [
            "Stores a string variable for the selected answer",
            "Creates a new window",
            "Defines a button",
            "Imports the math library"
        ],
        "answer": "Stores a string variable for the selected answer"
    },
    {
        "question": "Which of the following is a version control system used in our project?",
        "options": ["SVN", "Mercurial", "Git", "CVS"],
        "answer": "Git"
    },
    {
        "question": "What does the 'pack()' method do in Tkinter?",
        "options": [
            "Places widgets in a block-like structure",
            "Destroys the widget",
            "Changes font size",
            "Opens a file dialog"
        ],
        "answer": "Places widgets in a block-like structure"
    },
    {
        "question": "In Git, what is the purpose of '.gitignore' file?",
        "options": [
            "To ignore certain files from being tracked",
            "To delete the repository",
            "To rename the branch",
            "To merge two branches"
        ],
        "answer": "To ignore certain files from being tracked"
    }
]

current_q = 0
score = 0
answer_status = [False] * len(questions)

def update_progress():
    percent = (current_q / len(questions)) * 100
    progress_bar['value'] = percent
    percent_label.config(text=f"{int(percent)}%")

def load_question():
    q = questions[current_q]
    question_label.config(text=q["question"])
    var.set(None)
    for i in range(4):
        options[i].config(text=q["options"][i], value=q["options"][i])
    update_progress()

def next_question():
    global current_q, score

    if var.get() == questions[current_q]["answer"]:
        score += 1
        answer_status[current_q] = True
    else:
        answer_status[current_q] = False

    if current_q < len(questions) - 1:
        current_q += 1
        load_question()
    else:
        show_result()

def back_question():
    global current_q, score

    if current_q > 0:
        if answer_status[current_q]:
            score -= 1
            answer_status[current_q] = False

        current_q -= 1
        load_question()

def clear_answer():
    var.set(None)

def show_result():
    question_label.config(text=f"Your Final Score: {score}/{len(questions)}")
    for i in options:
        i.pack_forget()
    button_next.pack_forget()
    button_back.pack_forget()
    button_clear.pack_forget()
    progress_bar.pack_forget()
    percent_label.pack_forget()

window = tk.Tk()
window.title("Quiz App")
window.geometry("500x400")

question_label = tk.Label(window, text="", font=("Arial", 14), wraplength=450)
question_label.pack(pady=20)

var = tk.StringVar()

options = []
for i in range(4):
    rb = tk.Radiobutton(window, text="", variable=var, value="", font=("Arial", 12))
    rb.pack(anchor="w", padx=20)
    options.append(rb)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

button_back = tk.Button(button_frame, text="Back", command=back_question, bg="orange", fg="white")
button_back.pack(side="left", padx=5)

button_clear = tk.Button(button_frame, text="Clear Answer", command=clear_answer, bg="gray", fg="white")
button_clear.pack(side="left", padx=5)

button_next = tk.Button(button_frame, text="Next", command=next_question, bg="green", fg="white")
button_next.pack(side="left", padx=5)

progress_frame = tk.Frame(window)
progress_frame.pack(pady=20, fill="x", padx=20)

progress_bar = ttk.Progressbar(progress_frame, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(side="left", padx=5)

percent_label = tk.Label(progress_frame, text="0%", font=("Arial", 10))
percent_label.pack(side="left")

load_question()
window.mainloop()
