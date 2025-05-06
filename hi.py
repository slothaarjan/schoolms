import tkinter as tk

# ----- Quiz Data -----
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["5", "8", "10", "6"],
        "answer": "8"
    }
]

# ----- App State -----
current_question = 0
score = 0

# ----- Functions -----
def load_question():
    question_label.config(text=questions[current_question]["question"])
    for i, option in enumerate(questions[current_question]["options"]):
        option_buttons[i].config(text=option, state=tk.NORMAL)

def check_answer(selected_option):
    global current_question, score
    selected = option_buttons[selected_option].cget("text")
    correct = questions[current_question]["answer"]
    
    if selected == correct:
        score_label.config(text=f"✅ Correct! Score: {score + 1}")
        score += 1
    else:
        score_label.config(text=f"❌ Wrong! Score: {score}")
    
    for btn in option_buttons:
        btn.config(state=tk.DISABLED)
    
    next_button.config(state=tk.NORMAL)

def next_question():
    global current_question
    current_question += 1
    if current_question < len(questions):
        load_question()
        score_label.config(text="")
        next_button.config(state=tk.DISABLED)
    else:
        question_label.config(text=f"🎉 Quiz Finished! Final Score: {score}/{len(questions)}")
        for btn in option_buttons:
            btn.pack_forget()
        next_button.pack_forget()

# ----- UI Setup -----
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x300")
root.config(bg="#f4f4f4")

question_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#f4f4f4")
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", width=20, font=("Arial", 12), command=lambda i=i: check_answer(i))
    btn.pack(pady=5)
    option_buttons.append(btn)

score_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f4f4f4")
score_label.pack(pady=10)

next_button = tk.Button(root, text="Next", state=tk.DISABLED, command=next_question)
next_button.pack()

load_question()
root.mainloop()