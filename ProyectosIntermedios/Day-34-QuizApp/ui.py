from tkinter import *
from quiz_brain import QuizBrain



THEME_COLOR = "#375362"


class QuizGUI():
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quzzier")
        self.window.config(padx=30, pady=20, bg=THEME_COLOR)
        
        self.score_display = Label(text="Score: 0", fg="white", background=THEME_COLOR)
        self.score_display.grid(row=0, column=1)
        
        
        self.canvas = Canvas(width=300,height=300, bg="white")
        self.question_text = self.canvas.create_text(
            150, 150, text="Question", fill=THEME_COLOR,
            width=280,
            font=("Arial", 16, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        
        true_image = PhotoImage(file="ProyectosIntermedios/Day-34-QuizApp/images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0, command=  self.true_press )
        self.true_button.grid(row=2,column=0)
        
        false_image = PhotoImage(file="ProyectosIntermedios/Day-34-QuizApp/images/false.png")
        self.false_image = Button(image=false_image,highlightthickness=0, command=self.false_press)
        self.false_image.grid(row=2,column=1)    
        
        self.get_next_question()
        
           
        
        self.window.mainloop()
        
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)
        
        
    def true_press(self):
        self.quiz.check_answer("True")  
    
        
    def false_press(self):
        self.quiz.check_answer("False")