from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("350x500")
root.resizable(0,0)
root.title("Calculator")
root.iconbitmap("Icons/icon2.ico")

val = ""
operator = ""
A = 0

#=============================Logic for Application============================
def entered(event):
    butt_C.config(bg="red")

def left(event):
    butt_C.config(bg="indianred1")

def entered_(event):
    butt_DEL.config(bg="yellow")

def left_(event):
    butt_DEL.config(bg="yellow2")

def button_click(number):
    global val
    val = val + str(number)
    data.set(val)

def button_clear():
    global A,operator,val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def button_del():
    global A,operator,val
    v = val[-1]
    val = val[:len(val)-1]
    if v in ['+','-','*','/']:
        operator = ""
    operator = ""
    data.set(val)

def button_decimal():
    global val
    val = val + "."
    data.set(val)

def button_power():
    global A
    global operator,val
    A = float(val)
    operator = "^"
    val = val + "^"
    data.set(val)

def button_add():
    global A
    global operator,val
    A = float(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def button_subtract():
    global A
    global operator,val
    A = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def button_multiply():
    global A
    global operator,val
    A = float(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def button_divide():
    global A
    global operator,val
    A = float(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def button_equal():
    global A,operator,val
    val2 = val
    if operator == "+":
        x = float((val2.split("+")[1]))
        C = A + x
        val = str(C)
        data.set(val)
    elif operator == "-":
        x = float((val2.split("-")[1]))
        C = A - x
        val = str(C)
        data.set(val)
    elif operator == "*":
        x = float((val2.split("*")[1]))
        C = A * x
        val = str(C)
        data.set(val)
    elif operator == "/":
        x = float((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = A / x
            val = str(C)
            data.set(val)
    elif operator == "^":
        x = float((val2.split("^")[1]))
        C = A ** x
        val = str(C)
        data.set(val)
    else:
        #print(1)
        if '+' in val2 or '-' in val2 or '*' in val2 or '/' in val2 or '^' in val2:
            return
        #print(2)
        x=float(val2)
        C = x * x
        val = str(C)
        data.set(val)

#====================================UI of application===================================
data = StringVar()
e = Entry(root,text = "Label", justify = RIGHT, font = ("Verdana", 20),textvariable = data,background = "white",fg = "black")
e.insert(0,0)
e.pack(expand = True, fill = "both")


buttons_row_0 = Frame(root)
buttons_row_1 = Frame(root)
buttons_row_2 = Frame(root)
buttons_row_3 = Frame(root)
buttons_row_4 = Frame(root)

buttons_row_0.pack(expand = True, fill = "both")
buttons_row_1.pack(expand = True, fill = "both")
buttons_row_2.pack(expand = True, fill = "both")
buttons_row_3.pack(expand = True, fill = "both")
buttons_row_4.pack(expand = True, fill = "both")


butt_C = Button(buttons_row_0, text = "C", relief = "groove", border = 0, bg = "indianred1", font = ("Verdana", 22), command = button_clear)
butt_C.bind("<Enter>",entered)
butt_C.bind("<Leave>", left)

butt_DEL = Button(buttons_row_0, text = "DEL", relief = "groove", border = 0, bg = "yellow2", font = ("Verdana", 13), command = button_del)
butt_DEL.bind("<Enter>",entered_)
butt_DEL.bind("<Leave>", left_)

butt_SQ = Button(buttons_row_0, text = "sq", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = button_equal)
butt_POW = Button(buttons_row_0, text = "^", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = button_power)

butt_7 = Button(buttons_row_1, text = "7", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = lambda: button_click(7))
butt_8 = Button(buttons_row_1, text = "8", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = lambda: button_click(8))
butt_9 = Button(buttons_row_1, text = "9", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = lambda: button_click(9))
butt_add = Button(buttons_row_1, text = "+", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = button_add)

butt_4 = Button(buttons_row_2, text = "4", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = lambda: button_click(4))
butt_5 = Button(buttons_row_2, text = "5", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = lambda: button_click(5))
butt_6 = Button(buttons_row_2, text = "6", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = lambda: button_click(6))
butt_subt = Button(buttons_row_2, text = "-", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = button_subtract)

butt_1 = Button(buttons_row_3, text = "1", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = lambda: button_click(1))
butt_2 = Button(buttons_row_3, text = "2", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = lambda: button_click(2))
butt_3 = Button(buttons_row_3, text = "3", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = lambda: button_click(3))
butt_multi = Button(buttons_row_3, text = "*", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = button_multiply)

butt_decimal = Button(buttons_row_4, text = ".", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = button_decimal)
butt_0 = Button(buttons_row_4, text = "0", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = lambda: button_click(0))
butt_equal = Button(buttons_row_4, text = "=", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = button_equal)
butt_div = Button(buttons_row_4, text = "/", relief = "groove", border = 0, bg = "snow", font = ("Verdana", 22), command = button_divide)


butt_C.pack(expand = True, fill = "both", side = "left")
butt_DEL.pack(expand = True, fill = "both", side = "left")
butt_SQ.pack(expand = True, fill = "both", side = "left")
butt_POW.pack(expand = True, fill = "both", side = "left")

butt_7.pack(expand = True, fill = "both", side = "left")
butt_8.pack(expand = True, fill = "both", side = "left")
butt_9.pack(expand = True, fill = "both", side = "left")
butt_add.pack(expand = True, fill = "both", side = "left")

butt_4.pack(expand = True, fill = "both", side = "left")
butt_5.pack(expand = True, fill = "both", side = "left")
butt_6.pack(expand = True, fill = "both", side = "left")
butt_subt.pack(expand = True, fill = "both", side = "left")

butt_1.pack(expand = True, fill = "both", side = "left")
butt_2.pack(expand = True, fill = "both", side = "left")
butt_3.pack(expand = True, fill = "both", side = "left")
butt_multi.pack(expand = True, fill = "both", side = "left")

butt_decimal.pack(expand = True, fill = "both", side = "left")
butt_0.pack(expand = True, fill = "both", side = "left")
butt_equal.pack(expand = True, fill = "both", side = "left")
butt_div.pack(expand = True, fill = "both", side = "left")


root.mainloop()
