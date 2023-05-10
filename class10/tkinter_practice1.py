from tkinter import *

#가장 상위 레벨의 윈도우 창 생성
root = Tk()

#title 생성
root.title("SiSo")

#백그라운드 색상 지정
root.config(bg='skyblue')

#크기 조절
#root.geometry("300x200")

#크기조절 가능여부 설정
root.resizable(True, True)

#main_Frame
main_Frame = Frame(root, width=200, height=200, bg='blue')
main_Frame.grid(row=0, column=0, padx=10, pady=5)

main_Frame2 = Frame(root, width=200, height=200, bg='white').grid(row=0, column=1, padx=10, pady=5)

#윈도우 창을 윈도우가 종료될 때까지 실행
root.mainloop()