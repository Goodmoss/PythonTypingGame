import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = [
    "tree",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
    "javascript",
    "html",
    "css3",
]

words = [
    "eter",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
    "iscjavptia",
    "tmhl",
    "s3cs",
]


num =  random.randrange(0, len(words), 1)

class wordgame:
    def __init__(self):
        root = tkinter.Tk()
        root.geometry("350x400+400+300")
        root.title("기말고사 과제")
        root.configure(background = "black")


        TopAddNew = Frame(root, width=600, height=100, bd=1, relief=SOLID)      #프레임 설정
        TopAddNew.pack(side=TOP, pady=20)
        lbl_text = Label(TopAddNew, text="단어를 추측해보세요", font=('Consolas', 18), width=600)
        lbl_text.pack(fill=X)

        global lbl
        lbl = Label(root, text = "Your here",font = ("굴림체", 18), bg = "#E91E63",fg = "#FFFFFF")
        lbl.pack(pady = 30,ipady=10,ipadx=10)


        ans1 = StringVar()
        global e1
        e1 = Entry(root,font = ("굴림체", 16),textvariable = ans1)
        e1.pack(ipady=5,ipadx=5)

        #########
        #########
        btncheck = Button(root,text = "Check",font = ("굴림체", 16),width = 16,bg = "#4c4b4b",fg = "#6ab04c",relief = GROOVE, command = checkans)
        btncheck.pack(pady = 40)

        btnreset = Button(root,text = "Reset",font = ("굴림체", 16),width = 16,bg = "#4c4b4b",fg = "#EA425C",relief = GROOVE, command = res)
        btnreset.pack()

        default()
        root.mainloop()

def default():
    global words,answers,num
    lbl.config(text = words[num])

def res():
    global words, answers, num
    num = random.randrange(0, len(words), 1)
    lbl.config(text = words[num])
    e1.delete(0, END)


def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
            messagebox.showinfo("Success", "정답입니다")
            res()
    else:
            messagebox.showerror("Error", "오답입니다")
            e1.delete(0, END)


wordgame()
