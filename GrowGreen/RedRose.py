import tkinter
from tkinter import *
from tkinter import Label

window = Tk()
window.title("Grow Green")
window.config(background='light yellow')
window.geometry("1078x768")

def back_page():
    window.destroy()
    import FloweringPlants

def cart_page():
    window.destroy()
    import Cart


def open():
    top = Toplevel()
    lbl = Label(top)


pink_btn = PhotoImage(file='Red Rose.png')
img_label = Label(image=pink_btn)

btn = Button(window, image=pink_btn, bd=0, command=open).place(x=200, y=100, height=300, width=300)

orLabel: Label = Label(text="Red Rose Plant"
                            "\nPrice : Rs.600 ", font=('Nova Oval Bold', 25), bg='light yellow', justify="left")
orLabel.place(x=200, y=450)
orLabel: Label = Label(text="● Product Details: "
                     "\nPlant Name- Red Rose Plant"
                     "\nPlant Type: Flowering Plant "
                     "\nPlant Height: 10Inches Approx "
                     "\nPlant Location: Outdoors"
                     "\n  "
                     "\n● Caring Tips"
                     "\nWater regularly. Do not let soil get dry.."
                     "\nProvide six hours of sunlight on a daily basis."
                     "\nAdd the fertiliser monthly to the soil."
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
                  activeforeground='beige', activebackground='brown',command=cart_page)
myButton.place(x=680, y=600, height=60, width=130)
myButton = Button(window, text="Back", font=('Times Roman', 14, 'bold'), bg='Orange Red4', fg='beige', bd=0,
                  activeforeground='beige', activebackground='brown', command=back_page)
myButton.place(x=790, y=500, height=60, width=130)

window.mainloop()
