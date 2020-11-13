
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("250x400+300+300")
root.title("Calculator")
# root.resizable(0,0)
root.minsize(250, 400)
data = StringVar()
data1 = StringVar()
value = ""
a = 0
operator = ""


def btn_plus_clicked():
    global a, operator, value
    a = int(value)
    operator = "+"
    value += "+"
    data.set(value)


def btn_minus_clicked():
    global a, operator, value
    a = int(value)
    operator = "-"
    value += "-"
    data.set(value)


def btn_multiply_clicked():
    global a, operator, value
    a = int(value)
    operator = "*"
    value += "*"
    data.set(value)


def btn_div_clicked():
    global a, operator, value
    a = int(value)
    operator = "/"
    value += "/"
    data.set(value)


def btn_c_clicked():
    global a, operator, value
    a = 0,
    value = ""
    operator = ""
    data.set(value)


def calculate_result():
    global a, operator, value
    data1.set(a)
    data1.set(operator)
    data1.set(value)
    value2 = value
    if operator == "+":
        new_value = int(value2.split("+")[1])
        result1 = a + new_value
        data.set(result1)
        value = str(result1)

    elif operator == "-":
        new_value = int(value2.split("-")[1])
        result1 = a - new_value
        data.set(result1)
        value = str(result1)

    elif operator =="*":
        new_value = int(value2.split("*")[1])
        result1 = a * new_value
        data.set(result1)
        value = str(result1)

    elif operator == "/":
        new_value = int(value2.split("/")[1])
        if new_value == 0:
            messagebox.showinfo("Error","Divison by 0 is not allowed")
            a = ""
            value = ""
            data.set(value)
        else:
            r = float(a / new_value)
            result1 = round(r,3) # presion for float with 3 decimal
            data.set(result1)
            value = str(result1)


def btn1_clicked():
    global value
    value += "1"
    data.set(value)


def btn2_clicked():
    global value
    value += "2"
    data.set(value)


def btn3_clicked():
    global value
    value += "3"
    data.set(value)


def btn4_clicked():
    global value
    value += "4"
    data.set(value)


def btn5_clicked():
    global value
    value += "5"
    data.set(value)


def btn6_clicked():
    global value
    value += "6"
    data.set(value)


def btn7_clicked():
    global value
    value += "7"
    data.set(value)


def btn8_clicked():
    global value
    value += "8"
    data.set(value)


def btn9_clicked():
    global value
    value += "9"
    data.set(value)


def btn0_clicked():
    global value
    value += "0"
    data.set(value)

details = Label(root, textvariable=data1, anchor=SE, font=("Verdana", 20), fg="black")
details.pack(expand=True, fill="both")

result = Label(root, textvariable=data, anchor=SE, font=("Verdana", 20), background="white", fg="black")
result.pack(expand=True, fill="both")

brow1 = Frame(root)
brow1.pack(expand=True, fill="both")
brow2 = Frame(root)
brow2.pack(expand=True, fill="both")
brow3 = Frame(root)
brow3.pack(expand=True, fill="both")
brow4 = Frame(root)
brow4.pack(expand=True, fill="both")

btn1 = Button(brow1, text="1", font=("Verdana", 22), relief=GROOVE, border=0, command=btn1_clicked)
btn1.pack(side="left", expand=True, fill="both", )
btn2 = Button(brow1, text="2", font=("Verdana", 22), relief=GROOVE, border=0, command=btn2_clicked)
btn2.pack(side="left", expand=True, fill="both")
btn3 = Button(brow1, text="3", font=("Verdana", 22), relief=GROOVE, border=0, command=btn3_clicked)
btn3.pack(side="left", expand=True, fill="both")
btn4 = Button(brow1, text="+", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_plus_clicked)
btn4.pack(side="left", expand=True, fill="both")

btn1 = Button(brow2, text="4", font=("Verdana", 22), relief=GROOVE, border=0, command=btn4_clicked)
btn1.pack(side="left", expand=True, fill="both")
btn2 = Button(brow2, text="5", font=("Verdana", 22), relief=GROOVE, border=0, command=btn5_clicked)
btn2.pack(side="left", expand=True, fill="both")
btn3 = Button(brow2, text="6", font=("Verdana", 22), relief=GROOVE, border=0, command=btn6_clicked)
btn3.pack(side="left", expand=True, fill="both")
btn4 = Button(brow2, text="-", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_minus_clicked)
btn4.pack(side="left", expand=True, fill="both")

btn1 = Button(brow3, text="7", font=("Verdana", 22), relief=GROOVE, border=0, comman=btn7_clicked)
btn1.pack(side="left", expand=True, fill="both")
btn2 = Button(brow3, text="8", font=("Verdana", 22), relief=GROOVE, border=0, command=btn8_clicked)
btn2.pack(side="left", expand=True, fill="both")
btn3 = Button(brow3, text="9", font=("Verdana", 22), relief=GROOVE, border=0, command=btn9_clicked)
btn3.pack(side="left", expand=True, fill="both")
btn4 = Button(brow3, text="*", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_multiply_clicked)
btn4.pack(side="left", expand=True, fill="both")

btn1 = Button(brow4, text="c", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_c_clicked)
btn1.pack(side="left", expand=True, fill="both")
btn2 = Button(brow4, text="0", font=("Verdana", 22), relief=GROOVE, border=0, command=btn0_clicked)
btn2.pack(side="left", expand=True, fill="both")
btn3 = Button(brow4, text="=", font=("Verdana", 22), relief=GROOVE, border=0, command=calculate_result)
btn3.pack(side="left", expand=True, fill="both")
btn4 = Button(brow4, text="/", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_div_clicked)
btn4.pack(side="left", expand=True, fill="both")


root.mainloop()
