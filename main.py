import tkinter as tk

questions = [
    {
        "question": "What is the capital of Egypt?",
        "options": ["Cairo", "Alex", "Giza", "Aswan"],
        "answer": "Cairo"
    },
    {
        "question": "3 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "5"
    },
    {
        "question": "What is 10 / 2?",
        "options": ["2", "5", "10", "20"],
        "answer": "5"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["Python", "HTML", "CSS", "SQL"],
        "answer": "Python"
    },
    {
        "question": "Sun rises from?",
        "options": ["West", "East", "North", "South"],
        "answer": "East"
    }
]

current_q = 0
score = 0

def load_question():
    q = questions[current_q]
    question_label.config(text=q["question"])
    var.set(None)

    for i in range(4):
        options[i].config(
            text=q["options"][i],
            value=q["options"][i]
        )

def next_question():
    global current_q, score

    if var.get() == questions[current_q]["answer"]:
        score += 1

    current_q += 1

    if current_q < len(questions):
        load_question()
    else:
        question_label.config(text=f"Your Score: {score}/{len(questions)}")
        for i in options:
            i.pack_forget()
        button.pack_forget()

window = tk.Tk()
window.title("Quiz App")

question_label = tk.Label(window, text="", font=("Arial", 14))
question_label.pack(pady=10)

var = tk.StringVar()

options = []
for i in range(4):
    rb = tk.Radiobutton(window, text="", variable=var, value="", font=("Arial", 12))
    rb.pack(anchor="w")
    options.append(rb)

button = tk.Button(window, text="Next", command=next_question)
button.pack(pady=10)

load_question()

window.mainloop()
