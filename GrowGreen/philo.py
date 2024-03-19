from tkinter import *
window = Tk()
window.title("Grow Green")
window.config(background= 'light yellow')
window.geometry("1200x700")

def open():

 top = Toplevel()
 lbl = Label(top, text="Philodendron xanadu").place()

pink_btn = PhotoImage(file='1p.png')
img_label= Label(image=pink_btn)
btn = Button(window, image=pink_btn,bd=0, command=open).place(x=200,y=100)

orLabel=Label(text="Botanical Name=Thaumatophyllum xanadu \nFamily=Araceae \nSun Exposure=Partial \nSoil Type=Moist but well-draining \nSoil pH=Acidic, neutral \nBloom Time=Spring, summer \nFlower Color=Green ",font=('Nova Oval',18),bg='light yellow')
orLabel.place(x=605,y=150)

myButton = Button(window, text="Buy now" , font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown')
myButton.place(x=750,y=400)
myButton = Button(window, text="Add to cart " , font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown')
myButton.place(x=810,y=450)
myButton = Button(window, text="Back" , font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown',command=quit)
myButton.place(x=900,y=400)

window.mainloop()