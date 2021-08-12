from tkinter import*

calc=Tk()
calc.title("Simple Calculator")
calc.configure(background="black")
calc.iconbitmap("calculator.ico")
calc.geometry("410x535")
calc.resizable(0,0)


entry=Entry(calc,width=31, borderwidth=30, bg="grey", fg="blue", font="Courier" "Bold", justify="right")

entry.grid(row=0, column=0, padx=5, pady=5, columnspan=4)


def click(num):
    string=entry.get()
    entry.delete(0,END)
    entry.insert(0, string + str(num))


def all_clear():
    entry.delete(0,END)


def sum():
    global first_num
    first_num=entry.get()
    global arithmetic
    arithmetic="add"
    entry.delete(0,END)


def difference():
    global first_num
    first_num = entry.get()
    global arithmetic
    arithmetic = "subtract"
    entry.delete(0, END)


def product():
    global first_num
    first_num = entry.get()
    global arithmetic
    arithmetic = "multiply"
    entry.delete(0, END)


def division():
    global first_num
    first_num=entry.get()
    global arithmetic
    arithmetic = "divide"
    entry.delete(0,END)
    

def square():
    global first_num
    first_num=entry.get()
    global arithmetic
    arithmetic="square"
    entry.delete(0,END)


def equal():
    second_num=entry.get()
    entry.delete(0,END)
    if arithmetic=="add":
        entry.insert(0, int(first_num)+int(second_num))
    if arithmetic=="subtract":
        entry.insert(0, int(first_num)-int(second_num))
    if arithmetic=="multiply":
        entry.insert(0, int(first_num)*int(second_num))
    if arithmetic=="divide":
        entry.insert(0, int(first_num)/int(second_num))
    if arithmetic=="square":
        entry.insert(0, int(first_num)**int(second_num))


zero=Button(calc, text="0",padx=30, pady=20, bg="white",font="Helluva" "30" "Bold",command=lambda:click(0))
zero.grid(row=5, column=0, padx=5, pady=5)

one=Button(calc, text="1", padx=30, pady=20, bg="white", font="Helluva" "30" "Bold",command=lambda:click(1))
one.grid(row=4, column=0,padx=5, pady=5)

two=Button(calc, text="2",padx=30, pady=20, bg="white", font="Helluva" "30" "Bold",command=lambda:click(2))
two.grid(row=4, column=1,padx=5, pady=5)

three=Button(calc, text="3",padx=30, pady=20, bg="white", font="Helluva" "30" "Bold",command=lambda:click(3))
three.grid(row=4, column=2,padx=5, pady=5)

four=Button(calc, text="4",padx=30, pady=20, bg="white", font="Helluva" "30" "Bold",command=lambda:click(4))
four.grid(row=3, column=0,padx=5, pady=5)

five=Button(calc, text="5",padx=30, pady=20, bg="white", font="Helluva" "30" "Bold",command=lambda:click(5))
five.grid(row=3, column=1,padx=5, pady=5)

six=Button(calc, text="6",padx=30, pady=20, bg="white", font="Helluva" "30" "Bold",command=lambda:click(6))
six.grid(row=3, column=2,padx=5, pady=5)

seven=Button(calc, text="7", padx=30, pady=20, bg="white", font="Helluva" "30" "Bold", command=lambda:click(7))
seven.grid(row=2, column=0,padx=5, pady=5)

eight=Button(calc, text="8", padx=30, pady=20, bg="white", font="Helluva" "30" "Bold",command=lambda:click(8))
eight.grid(row=2, column=1,padx=5, pady=5)

nine_button=Button(calc, text="9", padx=30, pady=20, bg="white", font="Helluva" "30" "Bold",command=lambda:click(9))
nine_button.grid(row=2, column=2,padx=5, pady=5)



add=Button(calc, text="+", padx=27, pady=20, bg="white", font="Helluva" "30" "Bold",fg="blue", command=sum)
add.grid(row=4, column=3)

subtract_button=Button(calc, text="-", padx=29, pady=20, font="Helluva" "30" "Bold",bg="white", fg="blue", command=difference)
subtract_button.grid(row=3,column=3,padx=5, pady=5)

multiply=Button(calc, text="*", padx=29, pady=20, bg="white", font="Helluva" "30" "Bold",fg="blue", command=product)
multiply.grid(row=2, column=3,padx=5, pady=5)

divide=Button(calc, text="/", padx=30, pady=20, bg="white",font="Helluva" "30" "Bold", fg="blue", command=division)
divide.grid(row=1, column=3,padx=5, pady=5)

square=Button(calc, text="^", padx=31,pady=20, bg="white",fg="blue",font="Helluva" "30" "Bold", command=square)
square.grid(row=1,column=2,padx=5, pady=5)


equal=Button(calc, text="=", width=21,padx=27, pady=20, bg="white",fg="blue",font="Helluva" "30" "Bold", command= equal)
equal.grid(row=5, column=1, columnspan=3)


clear=Button(calc, text="AC", width=13,padx=22, pady=20, bg="white", fg="blue",font="Helluva" "28" "Bold",command=all_clear)
clear.grid(row=1, column=0, columnspan=2)

calc.mainloop()