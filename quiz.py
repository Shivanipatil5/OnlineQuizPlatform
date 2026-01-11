import tkinter as tk
from tkinter import messagebox

# Quiz Questions
questions = [
    {
        "question": "Which of the following is a high-level programming language?",
        "options": ["Assembly" , "Machine Code" , "Python" , "Binary"],
        "answer": "python"
    },
    {
        "question": "What is the main purpose of a compiler?",
        "options": ["To execute the program line by line","To translate high-level code into machine code","To debug the program" ,"To manage memory"],
        "answer": "To translate high-level code into machine code"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Power Unit", "Core Processing Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which symbol is used to denote a single-line comment in Python?",
        "options": ["//" , "/* */" , "#" ,  "<!-- -->"],
        "answer": "#"
    },
    {
        "question": "Which data structure follows the FIFO (First In First Out) principle?",
        "options": ["Stack", "Queue","Tree", "Grapht"],
        "answer": "Queue"
    },
    {
        "question": "Which of the following is NOT an object-oriented programming concept??",
        "options": ["Inheritance","Polymorphism","Compilation","Encapsulation"],
        "answer": "Central Processing Unit"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz Platform")
        self.root.geometry("500x400")
        self.root.config(bg="#1e1e2f")

        self.q_index = 0
        self.score = 0

        self.question_label = tk.Label(
            root, text="", font=("Arial", 14, "bold"),
            bg="white", fg="black", wraplength=450, padx=10, pady=10
        )
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                root, text="", variable=self.var, value="",
                font=("Arial", 12),
                bg="#1e1e2f", fg="white",
                selectcolor="#6a5acd",
                activebackground="#1e1e2f",
                activeforeground="white"
            )
            rb.pack(anchor="w", padx=50)
            self.option_buttons.append(rb)

        self.next_btn = tk.Button(
            root, text="Next",
            font=("Arial", 12, "bold"),
            bg="#6a5acd", fg="white",
            command=self.next_question
        )
        self.next_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        self.var.set(None)
        q = questions[self.q_index]
        self.question_label.config(text=q["question"])

        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option, value=option)

    def next_question(self):
        if self.var.get() == "":
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        if self.var.get() == questions[self.q_index]["answer"]:
            self.score += 1

        self.q_index += 1

        if self.q_index < len(questions):
            self.load_question()
        else:
            messagebox.showinfo(
                "Quiz Completed",
                f"Your Score: {self.score}/{len(questions)}"
            )
            self.root.destroy()

# Run App
root = tk.Tk()
app = QuizApp(root)
root.mainloop()