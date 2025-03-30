from tkinter import*

root=Tk()
root.title("Calculator")
root.geometry("374x630")
root.configure(bg='#333333')

for i in range(6):  # 6 rows (0-5)
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

f_num=0
math_operation=""

disbar1=Entry(root,font=('Arial',40, 'bold'),justify='right',bd=2,relief='sunken',bg='#333333',fg='white')
disbar1.grid(row=0, column=0,padx=5,columnspan=4,pady=3,sticky="nsew",ipady=20)

def ClickC():
    disbar1.delete(0,END)

def ClickCE():
    disbar1.delete(0,END)
    global f_num
    global math_operation
    f_num=0
    math_operation=""

def ClickDel():
    current=disbar1.get()
    disbar1.delete(0,END)
    disbar1.insert(0,current[:-1])

def ClickPlMin():
    current = disbar1.get()
    disbar1.delete(0, END)
    if current and current[0] == '-':
        disbar1.insert(0, current[1:])
    else:
        disbar1.insert(0, '-' + current)

def Click(number):
    current=disbar1.get()
    disbar1.delete(0,END)
    disbar1.insert(0,current+str(number))


def add():
    first_number = disbar1.get()
    global f_num
    global math_operation
    math_operation = "addition"

    num = float(first_number)

    if num.is_integer():
        f_num = int(num)
        disbar1.delete(0, END)
        disbar1.insert(0, f"{f_num}+")
    else:
        f_num = num
        disbar1.delete(0, END)
        disbar1.insert(0, f"{f_num}+")

def sub():
    first_number = disbar1.get()
    global f_num
    global math_operation
    math_operation = "subtraction"

    num = float(first_number)

    if num.is_integer():
        f_num = int(num)
        disbar1.delete(0, END)
        disbar1.insert(0, f"{f_num}-")
    else:
        f_num = num
        disbar1.delete(0, END)
        disbar1.insert(0, f"{f_num}-")

def multi():
    first_number = disbar1.get()
    global f_num
    global math_operation
    math_operation = "multiplication"

    num = float(first_number)

    if num.is_integer():
        f_num = int(num)
        disbar1.delete(0, END)
        disbar1.insert(0, f"{f_num}*")
    else:
        f_num = num
        disbar1.delete(0, END)
        disbar1.insert(0, f"{f_num}*")

def div():
    first_number = disbar1.get()
    global f_num
    global math_operation
    math_operation = "division"

    num = float(first_number)

    if num.is_integer():
        f_num = int(num)
        disbar1.delete(0, END)
        disbar1.insert(0, f"{f_num}/")
    else:
        f_num = num
        disbar1.delete(0, END)
        disbar1.insert(0, f"{f_num}/")

def dot():
    current = disbar1.get()
    if '.' not in current:
        disbar1.delete(0, END)
        disbar1.insert(0, current + '.' if current else '0.')

def equals():
    second = disbar1.get()
    disbar1.delete(0, END)
    global f_num
    global math_operation

    try:
        if math_operation == "addition" and '+' in second:
            second_number = float(second.split("+")[1])
            result = f_num + second_number
        elif math_operation == "subtraction" and '-' in second:
            # Handle case where the number itself might be negative
            parts = second.split('-')
            if len(parts) > 2:  # Case like "5--3"
                second_number = -float(parts[2])
            else:
                second_number = float(parts[1])
            result = f_num - second_number
        elif math_operation == "multiplication" and '*' in second:
            second_number = float(second.split("*")[1])
            result = f_num * second_number
        elif math_operation == "division" and '/' in second:
            second_number = float(second.split("/")[1])
            if second_number == 0:
                disbar1.insert(0, "Error: Division by zero")
                return
            result = f_num / second_number
        else:
            return  # No operation to perform

        # Display integer if result is whole number, else float
        if result.is_integer():
            disbar1.insert(0, int(result))
        else:
            disbar1.insert(0, result)

    except (ValueError, IndexError):
        disbar1.insert(0, "Error")

buttonCE=Button(root,text='CE',bg='#555F61',fg='white',font=("Arial",12),command=ClickCE)
buttonC=Button(root,text='C',bg='#555F61',fg='white',font=("Arial",12),command=ClickC)
buttonDel=Button(root,text='Del',bg='#555F61',fg='white',font=("Arial",12),command=ClickDel)
buttonsub=Button(root,text="/",bg='#555F61',fg="white",font=("Arial",12),command=div)
button7=Button(root,text="7",bg='#808588',fg='white',font=("Arial",12),command=lambda :Click(7))
button8=Button(root,text="8",bg='#808588',fg='white',font=("Arial",12),command=lambda :Click(8))
button9=Button(root,text="9",bg='#808588',fg='white',font=("Arial",12),command=lambda :Click(9))
buttonmulti=Button(root,text="*",bg='#555F61',fg="white",font=("Arial",12),command=multi)
button4=Button(root,text="4",bg='#808588',fg='white',font=("Arial",12),command=lambda :Click(4))
button5=Button(root,text="5",bg='#808588',fg='white',font=("Arial",12),command=lambda :Click(5))
button6=Button(root,text="6",bg='#808588',fg='white',font=("Arial",12),command=lambda :Click(6))
buttonminus=Button(root,text="-",bg='#555F61',fg="white",font=("Arial",12),command=sub)
button1=Button(root,text=1,bg='#808588',fg='white',font=("Arial",12),command=lambda :Click(1))
button2=Button(root,text="2",bg='#808588',fg='white',font=("Arial",12),command=lambda :Click(2))
button3=Button(root,text="3",bg='#808588',fg='white',font=("Arial",12),command=lambda :Click(3))
buttonplus=Button(root,text="+",bg='#555F61',fg="white",font=("Arial",12),command=add)
buttonplmin=Button(root,text='+/-',bg='#808588',fg='white',font=("Arial",12),command=ClickPlMin)
button0=Button(root,text="0",bg='#808588',fg='white',font=("Arial",12),command=lambda :Click(0))
buttondot=Button(root,text='.',bg='#808588',fg='white',font=("Arial",12),command=dot)
buttoneq=Button(root,text="=",bg='#555F61',fg="white",font=("Arial",12),command=equals)

buttonCE.grid(row=1,column=0,padx=2,pady=2,sticky="nsew",ipady=30)
buttonC.grid(row=1,column=1,padx=2,pady=2,sticky="nsew",ipady=30)
buttonDel.grid(row=1,column=2,padx=2,pady=2,sticky="nsew",ipady=30)
buttonsub.grid(row=1,column=3,padx=2,pady=2,sticky="nsew",ipady=30)
button7.grid(row=2,column=0,padx=2,pady=2,sticky="nsew",ipady=30)
button8.grid(row=2,column=1,padx=2,pady=2,sticky="nsew",ipady=30)
button9.grid(row=2,column=2,padx=2,pady=2,sticky="nsew",ipady=30)
buttonmulti.grid(row=2,column=3,padx=2,pady=2,sticky="nsew",ipady=30)
button4.grid(row=3,column=0,padx=2,pady=2,sticky="nsew",ipady=30)
button5.grid(row=3,column=1,padx=2,pady=2,sticky="nsew",ipady=30)
button6.grid(row=3,column=2,padx=2,pady=2,sticky="nsew",ipady=30)
buttonminus.grid(row=3,column=3,padx=2,pady=2,sticky="nsew",ipady=30)
button1.grid(row=4,column=0,padx=2,pady=2,sticky="nsew",ipady=30)
button2.grid(row=4,column=1,padx=2,pady=2,sticky="nsew",ipady=30)
button3.grid(row=4,column=2,padx=2,pady=2,sticky="nsew",ipady=30)
buttonplus.grid(row=4,column=3,padx=2,pady=2,sticky="nsew",ipady=30)
buttonplmin.grid(row=5,column=0,padx=2,pady=2,sticky="nsew",ipady=30)
button0.grid(row=5,column=1,padx=2,pady=2,sticky="nsew",ipady=30)
buttondot.grid(row=5,column=2,padx=2,pady=2,sticky="nsew",ipady=30)
buttoneq.grid(row=5,column=3,padx=2,pady=2,sticky="nsew",ipady=30)

root.mainloop()