from _ast import Lambda
from tkinter import *
from tkinter import ttk

def userinfo_page():
    window.destroy()
    import invoice

def sign_page():
    window.destroy()
    import LoginAndRegistrationPage

def cart_page():
    window.destroy()
    import Cart

def indoor_page():
    window.destroy()
    import IndoorPlants

def air_page():
    window.destroy()
    import AirPurifyingPlants

def flowering_page():
    window.destroy()
    import FloweringPlants

def outdoor_page():
    window.destroy()
    import OutdoorPlants

def Redhibi_page():
    window.destroy()
    import RedHibi

def Redrose_page():
    window.destroy()
    import RedRose

def pink_page():
    window.destroy()
    import PinkDwarf

def adenium_page():
    window.destroy()
    import Adenium

def bonsai_page():
    window.destroy()
    import Bonsai

def mur_page():
    window.destroy()
    import Murraya

#MAIN WINDOW
window = Tk()
window.title("Grow Green")
window.config(background= 'light yellow')

bgImage=PhotoImage(file='home.png')
bgLabel=Label(window,image=bgImage)
bgLabel.grid(row=0,column=0)




# BUTTONS
myButton = Button(window, text=" SignIn " , font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown',command=sign_page)
myButton.place(x=970,y=160)

myButton = Button(window, text="  Cart  ",font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown',command=cart_page)
myButton.place(x=885,y=160)

myButton = Button(window, text="  Admin  ",font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown',command=userinfo_page)
myButton.place(x=746,y=160)

myButton = Button(window, text=" Indoor Plants ",font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown',command=indoor_page)
myButton.place(x=10,y=160)

myButton = Button(window, text=" Outdoor Plants ",font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown',command=outdoor_page)
myButton.place(x=170,y=160)

myButton = Button(window, text=" AirPurifying Plants ",font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown',command=air_page)
myButton.place(x=345,y=160)

myButton = Button(window, text=" Flowering Plants ",font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown',command=flowering_page)
myButton.place(x=555,y=160)


def open():

 top = Toplevel()
 lbl = Label(top, text=" Hibiscus Plant ").place()

hibi_btn = PhotoImage(file='hibi.png')
img_label= Label(image=hibi_btn)
btn = Button(window, image=hibi_btn,bd=0, command=Redhibi_page).place(x=150,y=220)
#my_img = ImageTk.Photoimage(Image.open(""))

def open():
    top=Toplevel()
    lbl = Label(top,text="money").place()
money_btn = PhotoImage(file='Red Rose.png')
img_label= Label(image=money_btn)
btn=Button(window,image=money_btn,bd=0, command=Redrose_page)
btn.place(x=420,y=220)

def open():

 top = Toplevel()
 lbl = Label(top, text="Ixora pink dwarf Plant ").place()

pink_btn = PhotoImage(file='pink.png')
img_label= Label(image=pink_btn)
btn = Button(window, image=pink_btn,bd=0, command=pink_page).place(x=700,y=220)

def open():

 top = Toplevel()
 lbl = Label(top, text="Beautifully Adenium").place()

BA_btn = PhotoImage(file='plant1.png')
img_label= Label(image=BA_btn)
btn = Button(window, image=BA_btn,bd=0, command=adenium_page).place(x=150,y=460)
#my_img = ImageTk.Photoimage(Image.open(""))

def open():
    top=Toplevel()
    lbl = Label(top,text="Bonsai").place()
Bon_btn = PhotoImage(file='plant2.png')
img_label= Label(image=Bon_btn)
btn=Button(window,image=Bon_btn,bd=0, command=bonsai_page)
btn.place(x=420,y=460)

def open():

 top = Toplevel()
 lbl = Label(top, text="Exotica ").place()

Exo_btn = PhotoImage(file='plant3.png')
img_label= Label(image=Exo_btn)
btn = Button(window, image=Exo_btn,bd=0, command=mur_page).place(x=700,y=460)

window.mainloop()