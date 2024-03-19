import tkinter
from tkinter import *
from tkinter import Label

window = Tk()
window.title("Grow Green")
window.config(background='light yellow')
window.geometry("1078x768")


def open():
    top = Toplevel()
    lbl = Label(top)


pink_btn = PhotoImage(file='dl.png')
img_label = Label(image=pink_btn)

btn = Button(window, image=pink_btn, bd=0, command=open).place(x=200, y=100, height=300, width=300)

orLabel: Label = Label(text="Dypsis lutescens "
                            "\nPrice : Rs.600 ", font=('Nova Oval Bold', 25), bg='light yellow', justify="left")
orLabel.place(x=200, y=450)
orLabel: Label = Label(text="● Product Details: "
                     "\nPlant Name-Dypsis lutescens "
                     "\nPlant Type: Indoor Plant "
                     "\nPlant Height: 3.5 Inches Approx "
                     "\nPlant Location: Indoors"
                             "\nVase Height: 4 Inches"
                            "\nVase Metarial: Ceramic"
                     "\n  "
                     "\n● Caring Tips"
                            "\nSome outdoor time during the spring, summer, "
                            "\nWater once a week to every ten days."
                            "\nFertilizing is necessary to keep it lush and green.."
                            "\nThe image is indicative in nature."
                            "\nAs plants are natural products, shape and size may be of varying scale."
                            "\nFor flowering plants, the flower can be fully bloomed,"
                            "\nsemi bloomed or in bud stage."
                            "\nIt will be delivered on the same day of placing the order.", font=('Nova Oval', 13),bg='light yellow',justify="left")

orLabel.place(x=550, y=100)

myButton = Button(window, text="Buy now", font=('Times Roman', 14, 'bold'), bg='Orange Red4', fg='beige', bd=0,
                  activeforeground='beige', activebackground='brown')
myButton.place(x=550, y=500, height=60, width=130)
myButton = Button(window, text="Add to cart ", font=('Times Roman', 14, 'bold'), bg='Orange Red4', fg='beige', bd=0,
                  activeforeground='beige', activebackground='brown')
myButton.place(x=680, y=600, height=60, width=130)
myButton = Button(window, text="Back", font=('Times Roman', 14, 'bold'), bg='Orange Red4', fg='beige', bd=0,
                  activeforeground='beige', activebackground='brown', command=quit)
myButton.place(x=790, y=500, height=60, width=130)

window.mainloop()

