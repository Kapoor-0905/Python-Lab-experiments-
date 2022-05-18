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
entry = Entry(root)
def show_name():
    username = entry.get()
    label = Label(root,text=username)
    label.grid(row=6,column=1)
def func():
    rdo = Label(root,text="You have clicked"+" "+str(var.get())).grid(row=6,column=2)

var=IntVar()
f= Radiobutton(root, text="first choice", value=1, command=func, variable=var)
f.grid(row=1, column=0)

s= Radiobutton(root, text="second choice", value=2, command=func, variable=var)
s.grid(row=1, column=1)

th= Radiobutton(root, text="third choice", value=3, command=func, variable=var)
th.grid(row=1, column=2)
            
btn = Button(root,text="Show",command=show_name)
btn.grid()
entry.grid(row=2,column=1)
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

