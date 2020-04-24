from tkinter import *
import math

def LeftClick(event):
    result = round(float(dataW.get()) / math.pow(float(dataH.get()) / 100, 2), 2)
    labelR.configure(text="ค่า BMI ของคุณ = " + str(result), fg="red")
    if result >= 30:
        labelT.configure(text="คุณอ้วนมาก!!", anchor=N)
    elif result >= 25:
        labelT.configure(text="คุณอ้วน!", anchor=N)
    elif result >= 23:
        labelT.configure(text="คุณมีน้ำหนักเกินมาตรฐาน", anchor=N)
    elif result >= 18.6:
        labelT.configure(text="คุณมีน้ำหนักปกติ", anchor=N)
    elif result < 18:
        labelT.configure(text="คุณผอมเกินไป!", anchor=N)

main = Tk ()
labelM = Label(main, text="โปรแกรมคำนวนค่า BMI ดัชนีมวลกาย", font="Helvetica 14 bold", anchor=S)
labelM.grid(row=0, column=0, columnspan=2)
labelH = Label(main, text="ส่วนสูง (ซม.)").grid(row=1, column=0)
dataH = Entry(main)
dataH.grid(row=1, column=1)
labelW = Label(main, text="น้ำหนัก (กก.)").grid(row=2, column=0)
dataW = Entry(main)
dataW.grid(row=2, column=1)
buttonR = Button(main, text="คำนวน", fg="green", width=10)
buttonR.grid(row=3, column=0, columnspan=2)
buttonR.bind('<Button-1>', LeftClick)
labelR = Label(main, text="-- ผลลัพธ์ --", fg="grey")
labelR.grid(row=4, column=0, columnspan=2)
labelT = Label(main)
labelT.grid(row=5, column=0, columnspan=2)
main.mainloop()