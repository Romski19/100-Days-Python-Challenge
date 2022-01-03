from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizller")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score = 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, sticky="EW")

        self.canvas = Canvas(width=300, height=250, bg="#FFFFFF")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     font=("Arial", 18, "italic"),
                                                     text="Click the bubbles that are multiples of two.",
                                                     fill=THEME_COLOR,
                                                     width=260)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50, sticky="EW")

        self.true_image = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_image, highlightthickness=0, command=self.get_true_answer)
        self.true_btn.grid(column=0, row=2)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_image, highlightthickness=0, command=self.get_false_answer)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the line! Final score: {self.quiz.score}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def get_true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def get_false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



