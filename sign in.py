from tkinter import *
from tkcalendar import *
from PIL import ImageTk


def hide():
    closeye.config(file='openeye.png')
    e5.config(show='')
    b3.config(command=show)
def show():
    closeye.config(file='closeye.png')
    e5.config(show='*')
    b3.config(command=hide)

'''   
def set_placeholder(event):
    if e3.get() == "DD/MM/YYYY":
        e3.delete(0,END)
        
    

def clear_placeholder(event):
    if not event.widget.get():
        event.widget.insert(0, "DD/MM/YYYY")
        event.widget.config(fg="grey")
'''

root=Tk()
root.state("zoomed")
root.title("CALENDER SIGN IN PAGE")
root.configure(bg="white")

def pick_date(event):
    global cal,date_window
    date_window=Toplevel()
    date_window.grab_set()
    date_window.title("choose date of birth")
    date_window.geometry("250x220+1400+420")
    cal=Calendar(date_window,selectmode="day",date_pattern="dd/mm/y")
    cal.place(x=0,y=0)
    btn=Button(date_window,text="Submit",command=grab_date)
    btn.place(x=80,y=190)

def grab_date():
    dob_entry.delete(0,END)
    dob_entry.insert(0,cal.get_date())
    date_window.destroy()
    



bgImage=ImageTk.PhotoImage(file="final.jpg")
bglabel=Label(root,image=bgImage)
bglabel.place(relx=0.5,rely=0.5,anchor="center")


l2=Label(text='First name : ',bg="white",font=("Monotype Corsiva",20))
l2.place(x=1240,y=300)
l3=Label(text='Last name : ',bg="white",font=("Monotype Corsiva",20))
l3.place(x=1240,y=360)
l4=Label(text='Date of birth : ',bg="white",font=("Monotype Corsiva",20))
l4.place(x=1240,y=410)
l5=Label(text='Email ID : ',bg="white",font=("Monotype Corsiva",20))
l5.place(x=1240,y=460)
l6=Label(text='Set a Password: ',bg="white",font=("Monotype Corsiva",20))
l6.place(x=1240,y=510)
l7=Label(text='Already have an account ? ',bg="white",fg="blue",font=("Monotype Corsiva",16))
l7.place(x=1250,y=640)

b1=Button(text="LOGIN",bg="white",fg="blue",font=("Times New Roman",13),cursor='hand2')
b2=Button(text="Sign in",fg="blue",bg="white",font=("Times New Roman",13),cursor='hand2')
openeye=PhotoImage(file='openeye.png')
closeye=PhotoImage(file='closeye.png')
b3=Button(root,image=closeye,bd=0,bg="white",activebackground="white",cursor='hand2',command=hide)




e1=Entry()
e1.place(x=1400,y=305)
e2=Entry()
e2.place(x=1400,y=365)
dob_entry=Entry()
dob_entry.place(x=1400,y=415)
e4=Entry()
e4.place(x=1400,y=465)
e5=Entry(show='*')
b3.place(x=1530,y=510)
e5.place(x=1400,y=515)


b1.place(x=1450,y=640)
b2.place(x=1350,y=570)
dob_entry.insert(5, "DD/MM/YYYY")
dob_entry.bind("<1>", pick_date)




root.mainloop()
