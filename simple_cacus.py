from tkinter import*

root= Tk()

root.title("simple calculator")

e=Entry(root,width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3, padx=10,pady=10)

def my_click(number):
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    

def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "Addition"
    f_num = int(first_num)
    e.delete(0,END)


def button_equal():
    if math == "Addition":
        second_num = e.get()
        e.delete(0,END)
        e.insert(0, f_num + int(second_num))    
    if math == "subtraction":
        second_num = e.get()
        e.delete(0,END)
        e.insert(0, f_num - int(second_num))   
    if math == "multiplication":
         second_num = e.get()
         e.delete(0,END)
         e.insert(0, f_num * int(second_num))  
    if math == "division":
         second_num = e.get()
         e.delete(0,END)
         e.insert(0, f_num / int(second_num))   

def button_clear():
    e.delete(0, END)
  


def button_subtract():
     first_num = e.get()
     global f_num
     global math
     math = "subtraction"
     f_num = int(first_num)
     e.delete(0,END)



def button_multiply():
     first_num = e.get()
     global f_num
     global math
     math = "multiplication"
     f_num = int(first_num)
     e.delete(0,END)

def button_divide():
     first_num = e.get()
     global f_num
     global math
     math = "division"
     f_num = int(first_num)
     e.delete(0,END)



button_1 = Button(root,text="1",padx=40,pady=20, command=lambda:my_click(1))
button_2 = Button(root,text="2",padx=40,pady=20, command=lambda:my_click(2))
button_3 = Button(root,text="3",padx=40,pady=20, command=lambda:my_click(3))
button_4 = Button(root,text="4",padx=40,pady=20, command=lambda:my_click(4))
button_5 = Button(root,text="5",padx=40,pady=20, command=lambda:my_click(5))
button_6 = Button(root,text="6",padx=40,pady=20, command=lambda:my_click(6))
button_7 = Button(root,text="7",padx=40,pady=20, command=lambda:my_click(7))
button_8 = Button(root,text="8",padx=40,pady=20, command=lambda:my_click(8))
button_9 = Button(root,text="9",padx=40,pady=20, command=lambda:my_click(9))
button_0 = Button(root,text="0",padx=40,pady=20, command=lambda:my_click(0))

buttonadd = Button(root,text="+",padx=40,pady=20, command=button_add)
buttonequal = Button(root,text="=",padx=87,pady=20, command=button_equal)
buttonclear = Button(root,text="clear",padx=79,pady=20, command=button_clear)
buttonsubtract = Button(root,text="-",padx=41,pady=20, command=button_subtract)
buttonmultiply = Button(root,text="x",padx=40,pady=20, command=button_multiply)
buttondivide= Button(root,text="/",padx=40,pady=20, command=button_divide)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

buttonadd.grid(row=5, column=0)
buttonequal.grid(row=4, column=1, columnspan=2)
buttonclear.grid(row=5,column=1, columnspan=2)
 
buttonsubtract.grid(row=6 ,column=0)
buttonmultiply.grid(row=6, column=1)
buttondivide.grid(row=6, column=2)

root.mainloop()