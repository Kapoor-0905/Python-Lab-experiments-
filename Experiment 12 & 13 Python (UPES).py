#Q1

from tkinter import *
root = Tk()
root.geometry("500x500")
def click():
    mylabel = Label(root,text="Button was clicked").pack()

btn = Button(root,text="Click Me",fg="blue",bg="green",command=click)
label = Label(root,text="Hello")

label.pack()
btn.pack()
root.mainloop()

#-----------------------------------------------------------------------------

#Q2

from tkinter import *
root = Tk()
root.title("Click")
#root.geometry("600x400")
entry = Entry(root)
entry.grid()
def print_data():
    label = Label(root,text=entry.get())
    label.grid()
def position():
    pos = "You selected first"
    label.config(text=pos)
    label.grid()
def position2():
    pos = "You selected second"
    label.config(text=pos)
    label.grid()
def position3():
    pos = "You selected third"
    label.config(text=pos)
    label.grid()
radio = IntVar()
btn = Button(root,text="display",bg="Yellow",fg="red",command=print_data)
r = Radiobutton(root,text="first",variable = radio,value = 1,command = position)
r.grid(row=2,column=10)

r1 = Radiobutton(root,text="second",variable = radio,value = 2,command = position2)
r1.grid(row=2,column=12)

r2 = Radiobutton(root,text="third",variable = radio,value = 3,command = position3)
r2.grid(row=2,column=14)

label = Label(root)
btn.grid()
root.mainloop()


#------------------------------------------------------------------------------------

#Q3

from tkinter import *
root = Tk()              
root.title("Exp12-3")   

label_name = Label(root, text="Name").grid(row=0, column=0)
name= Text(root, width=30, height=1,padx=10,pady=10)
name.grid(row=0, column=1,pady=30)

g=StringVar()
m= Radiobutton(root, text="Male",variable=g,value="male")
f =Radiobutton(root, text="Female",variable=g,value="female")

m.grid(row=6,column=0)
f.grid(row=6,column=1)

label1= Label(root, text="Qualifications:")
label1.grid(row=1, column=0)
qualifications= Listbox(root, width=30, height=5)
qualifications.grid(row=1, column=1)
qualifications.insert(1, "MSc")
qualifications.insert(2, "BTech")
qualifications.insert(3, "BSc")
qualifications.insert(4, "MBA")

marks_Label= Label(root, text="Marks:")
marks_Label.grid(row=2, column=0)
m1= Text(root, width=10, height=1,padx=5,pady=5)
m1.grid(row=3, column=0)
m2= Text(root, width=10, height=1,padx=5,pady=5)
m2.grid(row=3, column=1)
m3= Text(root, width=10, height=1,padx=5,pady=5)
m3.grid(row=3, column=2)

def calc():
    m1_value=m1.get("1.0",END)
    m2_value=m2.get("1.0",END)
    m3_value=m3.get("1.0",END)
    prcnt.delete(1.0,END)
    prcnt.insert(END,"Student's Name is: "+name.get("1.0",END)+"\n")
    if g.get()=="male":
        prcnt.insert(END,"He got "+str((int(m1_value)+int(m2_value)+int(m3_value))/3))
    elif g.get()=="female":
        prcnt.insert(END,"She got "+str((int(m1_value)+int(m2_value)+int(m3_value))/3))

my_button = Button(root, text="Calculate", command=calc).grid(row=4, column=1)

prcnt= Text(root, width=30, height=3,padx=5,pady=5)
prcnt.grid(row=5, column=1,pady=10)


root.mainloop()

