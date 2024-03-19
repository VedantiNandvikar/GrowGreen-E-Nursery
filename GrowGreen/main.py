from tkinter import *
import sqlite3

window = Tk()
window.title("Grow Green")
window.config(background= 'light yellow')
window.geometry("1200x700")







def open():

 top = Toplevel()
 lbl = Label(top, text=" Dypsis lutescens ").place()

pink_btn = PhotoImage(file='dl.png')
img_label= Label(image=pink_btn)
btn = Button(window, image=pink_btn,bd=0, command=open).place(x=200,y=100)

orLabel=Label(text="Botanical Name=Dypsis lutescens \n Family=Arecaceae\n Sun Exposure=Full to partial sun\nSoil Type=Moist, well-drained\nSoil pH=Acidic, neutral\nBloom Time=Summer\nFlower Color=Pale yellow ",font=('Nova Oval',18),bg='light yellow')
orLabel.place(x=705,y=200)

myButton = Button(window, text="Buy now" , font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown')
myButton.place(x=750,y=450)
myButton = Button(window, text="Back" , font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown',command=quit)
myButton.place(x=900,y=450)
myButton = Button(window, text="Add to cart" , font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown')
myButton.place(x=800,y=525)



window.mainloop()
