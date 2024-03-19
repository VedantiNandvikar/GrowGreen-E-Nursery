import tkinter
from tkinter import *
from tkinter import Label

window = Tk()
window.title("Grow Green")
window.config(background='light yellow')
window.geometry("1078x768")

orLabel: Label = Label(text="Flowering Plants  ", font=('Nova Oval Bold', 35), bg='light yellow', justify="center")
orLabel.config(justify="center")
orLabel.place(x=340, y=20)

def home_page():
    window.destroy()
    import HomePage

def adenium_page():
    window.destroy()
    import Adenium

def pink_page():
    window.destroy()
    import PinkDwarf

def Redrose_page():
    window.destroy()
    import RedRose

def Redhibi_page():
    window.destroy()
    import RedHibi

def Boug_page():
    window.destroy()
    import Boug



hibi_btn = PhotoImage(file='Adenium.png')
img_label = Label(image=hibi_btn)
btn = Button(window, image=hibi_btn, bd=0, command=adenium_page).place(x=50, y=100, height=270, width=270)

orLabel: Label = Label(text="Beautifully Adenium", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=100, y=380)




def open():
    top = Toplevel()
    lbl = Label(top, text="Red Rose").place()


money_btn = PhotoImage(file='Red Rose.png')
img_label = Label(image=money_btn)
btn = Button(window, image=money_btn, bd=0, command=Redrose_page)
btn.place(x=375, y=100, height=270, width=270)

orLabel: Label = Label(text="Red Rose Plant", font=('Nova Oval Bold', 15), bg='light blue', justify="left")
orLabel.place(x=435, y=380)



def open():
    top = Toplevel()
    lbl = Label(top, text="pink dwarf Plant").place()


pink_btn = PhotoImage(file='Pink Dwarf.png')
img_label = Label(image=pink_btn)
btn = Button(window, image=pink_btn, bd=0, command=pink_page).place(x=700, y=100, height=270, width=270)

orLabel: Label = Label(text="Ixora Pink Dwarf", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=750, y=380)

def open():
    top = Toplevel()
    lbl = Label(top, text="Red Hibiscus").place()


Red_btn = PhotoImage(file='Red Hibiscus.png')
img_label = Label(image=Red_btn)
btn = Button(window, image=Red_btn, bd=0, command=Redhibi_page)
btn.place(x=500, y=435, height=270, width=270)

orLabel: Label = Label(text="Red Hibiscus Plant", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=550, y=720)

def open():
    top = Toplevel()
    lbl = Label(top)


Blue_btn = PhotoImage(file='Bouganvillea.png')
img_label = Label(image=Blue_btn)
btn = Button(window, image=Blue_btn, bd=0, command=Boug_page)
btn.place(x=150, y=435, height=270, width=270)

orLabel: Label = Label(text="Beautiful Bouganvillea Plant", font=('Nova Oval Bold', 15), bg='light blue', justify="left")
orLabel.place(x=160, y=720)

myButton = Button(window, text="X", font=('Times Roman', 14, 'bold'), bg='Orange Red4', fg='beige', bd=0,
                  activeforeground='beige', activebackground='brown', command=home_page)
myButton.place(x=1050, y=0, height=30, width=30)

window.mainloop()
