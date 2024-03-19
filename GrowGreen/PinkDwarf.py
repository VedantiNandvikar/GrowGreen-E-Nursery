import tkinter
from tkinter import *
from tkinter import Label

window = Tk()
window.title("Grow Green")
window.config(background='light yellow')
window.geometry("1078x768")

def cart_page():
    window.destroy()
    import Cart

def back_page():
    window.destroy()
    import FloweringPlants

def open():
    top = Toplevel()
    lbl = Label(top)


pink_btn = PhotoImage(file='Pink Dwarf.png')
img_label = Label(image=pink_btn)

btn = Button(window, image=pink_btn, bd=0, command=open).place(x=200, y=100, height=300, width=300)

orLabel: Label = Label(text="Ixora Pink Dwarf"
                            "\nPrice : Rs.545 ", font=('Nova Oval Bold', 25), bg='light yellow', justify="left")
orLabel.place(x=200, y=450)
orLabel: Label = Label(text="● PRODUCT DETAILS: "
                     "\nPlant Name- Ixora Pink Dwarf"
                     "\nPlant Type: Flowering Plant "
                     "\nPlant Height: 6 Inches Approx "
                     "\nPlant Location: Outdoors"
                            "\nVase Height: 4 Inches"
                            "\nVase Metarial: Ceramic"
                     "\n  "
                     "\n● CARING TIPS"
                     "\nBright, indirect light is crucial."
                     "\nWater the plant once a week."
                     "\nEnsure proper drainage from soil.."
                    "\nFertilise the plant from spring to summer during its growth season."
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
