from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.win=Tk()
        self.win.title("Qizzler")
        self.win.config(padx=20,pady=20,bg=THEME_COLOR)

        self.txt=Label(text="Score:0",bg=THEME_COLOR,fg="white")
        self.txt.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_txt=self.canvas.create_text(150,125,text="Amazon Accuqured",font=("arial",15,"italic"),fill=THEME_COLOR,width=280)

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.timg=PhotoImage(file=r"C:\Users\linge\Desktop\python 100 days\projects\pr-34\images\true.png")
        self.fimg=PhotoImage(file=r"C:\Users\linge\Desktop\python 100 days\projects\pr-34\images\false.png")
        self.tbut=Button(image=self.timg,highlightthickness=0,command=self.true)
        # self.tbut.config(padx=20,pady=20)
        self.tbut.grid(column=0,row=2)
        self.fbut=Button(image=self.fimg,highlightthickness=0,command=self.false)
        # self.fbut.config(padx=20,pady=20)
        self.fbut.grid(column=1,row=2)

        self.get_nxt_ques()


        self.win.mainloop()
    
    def get_nxt_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.txt.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_txt,text=q_text)
        else:
            self.canvas.itemconfig(self.question_txt,text=f"You'e REACHED THE END OF THE QUIZ\nYour Total Score is: {self.quiz.score}")
            self.tbut.config(state="disabled")
            self.fbut.config(state="disabled")

    def true(self):
        ans=self.quiz.check_answer("True")
        self.give_feedback(ans)
        # print(ans)

    def false(self):
        # ans=
        self.give_feedback(self.quiz.check_answer("False"))
        # print(ans)

    def give_feedback(self,ans):
        if ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.win.after(1000,self.get_nxt_ques)
        