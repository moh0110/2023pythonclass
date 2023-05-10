from tkinter import *

root = Tk()
root.title("Button")

def btncmd() :
    print("버튼을 클릭하였습니다")

btn = Button(root, text="버튼", padx=10, pady=10, command=btncmd)
btn.pack()

root.mainloop()