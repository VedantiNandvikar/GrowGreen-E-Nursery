import tkinter
from tkinter import *
from tkinter import Label

window = Tk()
window.title("Grow Green")
window.config(background='light yellow')
window.geometry("1078x768")



orLabel: Label = Label(text="Air Purifying Plants", font=('Nova Oval Bold', 35), bg='light yellow', justify="center")
orLabel.config(justify="center")
orLabel.place(x=340, y=20)

def home_page():
    window.destroy()
    import HomePage

def Aspa_page():
    window.destroy()
    import Aspa

def Snake_page():
    window.destroy()
    import Snake

def Sch_page():
        window.destroy()
        import Sch

def Sens_page():
            window.destroy()
            import Sens

def Zamia_page():
                window.destroy()
                import Zamia

def Fox_page():
        window.destroy()
        import Foxtail

def open():
    top = Toplevel()
    lbl = Label(top)


hibi_btn = PhotoImage(file='Aspa.png')
img_label = Label(image=hibi_btn)
btn = Button(window, image=hibi_btn, bd=0, command=Aspa_page).place(x=50, y=100, height=270, width=270)

orLabel: Label = Label(text="Valentine Asparagus Plant", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=100, y=380)




def open():
    top = Toplevel()
    lbl = Label(top)


money_btn = PhotoImage(file='Snake .png')
img_label = Label(image=money_btn)
btn = Button(window, image=money_btn, bd=0, command=Snake_page)
btn.place(x=375, y=100, height=270, width=270)

orLabel: Label = Label(text="Snake Plant", font=('Nova Oval Bold', 15), bg='light blue', justify="left")
orLabel.place(x=435, y=380)



def open():
    top = Toplevel()
    lbl = Label(top)


pink_btn = PhotoImage(file='Schefflera.png')
img_label = Label(image=pink_btn)
btn = Button(window, image=pink_btn, bd=0, command=Sch_page).place(x=700, y=100, height=270, width=270)

orLabel: Label = Label(text="Schefflera Plant", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=750, y=380)

def open():
    top = Toplevel()
    lbl = Label(top)


Red_btn = PhotoImage(file='Sensveria.png')
img_label = Label(image=Red_btn)
btn = Button(window, image=Red_btn, bd=0, command=Sens_page)
btn.place(x=700, y=435, height=270, width=270)

orLabel: Label = Label(text="Sensveria Birthday Plant", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=750, y=720)

def open():
    top = Toplevel()
    lbl = Label(top)


Blue_btn = PhotoImage(file='Zamia.png')
img_label = Label(image=Blue_btn)
btn = Button(window, image=Blue_btn, bd=0, command=Zamia_page)
btn.place(x=375, y=435, height=270, width=270)

orLabel: Label = Label(text="Zamia Zamioculous", font=('Nova Oval Bold', 15), bg='light blue', justify="left")
orLabel.place(x=435, y=720)

def open():
    top = Toplevel()
    lbl = Label(top)


Grey_btn = PhotoImage(file='Foxtail.png')
img_label = Label(image=Grey_btn)
btn = Button(window, image=Grey_btn, bd=0, command=Fox_page)
btn.place(x=50, y=435, height=270, width=270)

orLabel: Label = Label(text="Foxtail Fern", font=('Nova Oval Bold', 15), bg='light pink', justify="left")
orLabel.place(x=80, y=720)

myButton = Button(window, text="X", font=('Times Roman', 14, 'bold'), bg='Orange Red4', fg='beige', bd=0,
                  activeforeground='beige', activebackground='brown', command=home_page)
myButton.place(x=1050, y=0, height=30, width=30)

window.mainloop()
