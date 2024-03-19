import tkinter
from tkinter import *
from tkinter import Label

window = Tk()
window.title("Grow Green")
window.config(background='light yellow')
window.geometry("1078x768")

orLabel: Label = Label(text="Outdoor Plants  ", font=('Nova Oval Bold', 35), bg='light yellow', justify="center")
orLabel.config(justify="center")
orLabel.place(x=340, y=20)

def home_page():
    window.destroy()
    import HomePage

def Bonsai_page():
    window.destroy()
    import Bonsai

def Mur_page():
    window.destroy()
    import Murraya

def Rub_page():
    window.destroy()
    import Rubber

def Fic_page():
        window.destroy()
        import Ficus

def Pomo_page():
            window.destroy()
            import pomog

def Ulmus_page():
                window.destroy()
                import Ulmus

def open():
    top = Toplevel()
    lbl = Label(top)


hibi_btn = PhotoImage(file='Bonsai.png')
img_label = Label(image=hibi_btn)
btn = Button(window, image=hibi_btn, bd=0, command=Bonsai_page).place(x=50, y=100, height=270, width=270)

orLabel: Label = Label(text="Ficus I Shape Bonsai", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=100, y=380)




def open():
    top = Toplevel()
    lbl = Label(top)


money_btn = PhotoImage(file='Murraya.png')
img_label = Label(image=money_btn)
btn = Button(window, image=money_btn, bd=0, command=Mur_page)
btn.place(x=375, y=100, height=270, width=270)

orLabel: Label = Label(text="Murraya Exotica Plant", font=('Nova Oval Bold', 15), bg='light blue', justify="left")
orLabel.place(x=435, y=380)



def open():
    top = Toplevel()
    lbl = Label(top)


pink_btn = PhotoImage(file='Rubber.png')
img_label = Label(image=pink_btn)
btn = Button(window, image=pink_btn, bd=0, command= Rub_page).place(x=700, y=100, height=270, width=270)

orLabel: Label = Label(text="Rubber Plant", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=750, y=380)

def open():
    top = Toplevel()
    lbl = Label(top)


Red_btn = PhotoImage(file='Ficus1.png')
img_label = Label(image=Red_btn)
btn = Button(window, image=Red_btn, bd=0, command=Fic_page)
btn.place(x=700, y=435, height=270, width=270)

orLabel: Label = Label(text="Ficus Compacta", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=750, y=720)

def open():
    top = Toplevel()
    lbl = Label(top)


Blue_btn = PhotoImage(file='Pomo.png')
img_label = Label(image=Blue_btn)
btn = Button(window, image=Blue_btn, bd=0, command=Pomo_page)
btn.place(x=375, y=435, height=270, width=270)

orLabel: Label = Label(text="Divine Pomegranate", font=('Nova Oval Bold', 15), bg='light blue', justify="left")
orLabel.place(x=435, y=720)

def open():
    top = Toplevel()
    lbl = Label(top)


Grey_btn = PhotoImage(file='Ulmus.png')
img_label = Label(image=Grey_btn)
btn = Button(window, image=Grey_btn, bd=0, command=Ulmus_page)
btn.place(x=50, y=435, height=270, width=270)

orLabel: Label = Label(text="Ulmus S Shaped Bonsai", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=80, y=720)

myButton = Button(window, text="X", font=('Times Roman', 14, 'bold'), bg='Orange Red4', fg='beige', bd=0,
                  activeforeground='beige', activebackground='brown', command=home_page)
myButton.place(x=1050, y=0, height=30, width=30)

window.mainloop()
