import tkinter
from tkinter import *
from tkinter import Label

window = Tk()
window.title("Grow Green")
window.config(background='light yellow')
window.geometry("1078x768")

orLabel: Label = Label(text="Indoor Plants", font=('Nova Oval Bold', 35), bg='light yellow', justify="center")
orLabel.config(justify="center")
orLabel.place(x=340, y=20)

def home_page():
    window.destroy()
    import HomePage

def Crassula_page():
    window.destroy()
    import cra

def Ech_page():
    window.destroy()
    import ech

def Nep_page():
    window.destroy()
    import nehro

def Mon_page():
    window.destroy()
    import mon

def Chr_page():
        window.destroy()
        import chr

def Dl_page():
            window.destroy()
            import dl

def open():
    top = Toplevel()
    lbl = Label(top)


hibi_btn = PhotoImage(file='1c.png')
img_label = Label(image=hibi_btn)
btn = Button(window, image=hibi_btn, bd=0, command=Crassula_page).place(x=50, y=100, height=270, width=270)

orLabel: Label = Label(text="Crassula ", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=100, y=380)




def open():
    top = Toplevel()
    lbl = Label(top)


money_btn = PhotoImage(file='1e.png')
img_label = Label(image=money_btn)
btn = Button(window, image=money_btn, bd=0, command=Ech_page)
btn.place(x=375, y=100, height=270, width=270)

orLabel: Label = Label(text="Echeveria", font=('Nova Oval Bold', 15), bg='light blue', justify="left")
orLabel.place(x=435, y=380)



def open():
    top = Toplevel()
    lbl = Label(top)


pink_btn = PhotoImage(file='1n.png')
img_label = Label(image=pink_btn)
btn = Button(window, image=pink_btn, bd=0, command=Nep_page).place(x=700, y=100, height=270, width=270)

orLabel: Label = Label(text="Nephrolepi", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=750, y=380)

def open():
    top = Toplevel()
    lbl = Label(top)


Red_btn = PhotoImage(file='1m.png')
img_label = Label(image=Red_btn)
btn = Button(window, image=Red_btn, bd=0, command=Mon_page)
btn.place(x=700, y=435, height=270, width=270)

orLabel: Label = Label(text="Monstera", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=750, y=720)

def open():
    top = Toplevel()
    lbl = Label(top)


Blue_btn = PhotoImage(file='1ch.png')
img_label = Label(image=Blue_btn)
btn = Button(window, image=Blue_btn, bd=0, command=Chr_page)
btn.place(x=375, y=435, height=270, width=270)

orLabel: Label = Label(text="Chrysanthemum", font=('Nova Oval Bold', 15), bg='light blue', justify="left")
orLabel.place(x=435, y=720)

def open():
    top = Toplevel()
    lbl = Label(top)


Grey_btn = PhotoImage(file='dl.png')
img_label = Label(image=Grey_btn)
btn = Button(window, image=Grey_btn, bd=0, command=Dl_page)
btn.place(x=50, y=435, height=270, width=270)

orLabel: Label = Label(text="Dypsis lutescens ", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=80, y=720)

myButton = Button(window, text="X", font=('Times Roman', 14, 'bold'), bg='Orange Red4', fg='beige', bd=0,
                  activeforeground='beige', activebackground='brown', command=home_page)
myButton.place(x=1050, y=0, height=30, width=30)

window.mainloop()
