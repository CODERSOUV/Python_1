from tkinter import *

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def sclear():
    global expression 
    expression=expression[0:len(expression)-1]
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("ERROR")
        expression = ""


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x270")
    root.title("My first calculator")
    equation = StringVar()
    entry = Entry(root, textvariable=equation, bg="black", fg="white", font="Arial 24 bold")
    entry.grid(columnspan=4, ipadx=50, ipady=20, row=0, column=0)
    root.configure(background="black")

    Button(root, text="1", command=lambda: press(1), fg="white", bg="black", height=2, width=2).grid(row=1, column=0)
    Button(root, text="2", command=lambda: press(2), bg="black", fg="white", height=2, width=2).grid(row=1, column=1)
    Button(root, text="3", command=lambda: press(3), bg="black", fg="white", height=2, width=2).grid(row=1, column=2)
    Button(root, text="AC", command=lambda: clear(), bg="yellow", fg="black", height=2, width=2).grid(row=1, column=3)
    Button(root, text="4", command=lambda: press(4), bg="black", fg="white", height=2, width=2).grid(row=2, column=0)
    Button(root, text="5", command=lambda: press(5), bg="black", fg="white", height=2, width=2).grid(row=2, column=1)
    Button(root, text="6", command=lambda: press(6), bg="black", fg="white", height=2, width=2).grid(row=2, column=2)
    Button(root, text="+", command=lambda: press("+"), bg="yellow", fg="black", height=2, width=2).grid(row=2, column=3)
    Button(root, text="7", command=lambda: press(7), bg="black", fg="white", height=2, width=2).grid(row=3, column=0)
    Button(root, text="8", command=lambda: press(8), bg="black", fg="white", height=2, width=2).grid(row=3, column=1)
    Button(root, text="9", command=lambda: press(9), bg="black", fg="white", height=2, width=2).grid(row=3, column=2)
    Button(root, text="-", command=lambda: press("-"), bg="yellow", fg="black", height=2, width=2).grid(row=3, column=3)
    Button(root, text="/", command=lambda: press("/"), bg="yellow", fg="black", height=2, width=2).grid(row=4, column=0)
    Button(root, text="*", command=lambda: press("*"), bg="yellow", fg="black", height=2, width=2).grid(row=4, column=1)
    Button(root, text="=", command=lambda: equal(), bg="yellow", fg="black", height=50, width=2).grid(row=4, column=2)
    Button(root, text="DEL", command=lambda: sclear(), bg="yellow", fg="black", height=50, width=2).grid(row=4, column=3)
    root.mainloop()