from tkinter import *
import tkinter as tk
from tkinter import ttk
window = Tk()
window.title("Grow Green")
window.config(background= 'light yellow')
window.geometry("1000x600")

frame = Frame(window)
frame.config(background= 'light yellow')
frame.pack(padx=20, pady=20)

heading=Label(window,text='Add to cart',font=('Times Roman',24,'bold'),fg='brown',bg='light yellow')
heading.place(x=410,y=20)
columns = ('qty', 'plant name', 'price')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('qty', text='Qty')
tree.heading('plant name', text='Plant Name')
tree.heading('price', text='Unit Price')

tree.grid(row=10, column=0, columnspan=3, padx=100, pady=50)


def back_page():
    window.destroy()
    import HomePage



class Add_to_Cart:
    def __init__ (window):
        import RedHibi

        # Create listbox to display items
         window.items_listbox = tk.Listbox(window)
         window.items_listbox.pack(side=tk.LEFT, padx=5, pady=10)

        # Create scrollbar for listbox
         window.items_scrollbar = tk.Scrollbar(window)
         window.items_scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Set scrollbar to listbox
         window.items_listbox.config(yscrollcommand=window.items_scrollbar.set)
         window.items_scrollbar.config(command=window.items_listbox.yview)

        # Create button to add items
         window.add_button = tk.Button(window, text="Add Item", command=window.add_item)
         window.add_button.pack(side=tk.TOP, padx=10, pady=10)

        # Create button to remove items
         window.remove_button = tk.Button(window, text="Remove Item", command=window.remove_item)
         window.remove_button.pack(side=tk.TOP, padx=10, pady=10)


    def add_item(window):
        # Create a new window to input item details
        window.add_window = tk.Toplevel(window)
        window.add_window.title("Add Item")

        # Create labels and entry boxes for item details
        tk.Label(window.add_window, text="Item Name").grid(row=0, column=0)
        window.name_entry = tk.Entry(window.add_window)
        window.name_entry.grid(row=0, column=1)

        tk.Label(window.add_window, text="Item Price").grid(row=1, column=0)
        window.price_entry = tk.Entry(window.add_window)
        window.price_entry.grid(row=1, column=1)

        # Create button to add item to listbox
        window.add_item_button = tk.Button(window.add_window, text="Add Item", command=window.add_item_to_listbox)
        window.add_item_button.grid(row=2, column=1, pady=10)


    def add_item_to_listbox(window):
        # Get item details from entry boxes
        name = window.name_entry.get()
        price = window.price_entry.get()

        # Add item to listbox
        window.items_listbox.insert(tk.END, f"{name}: ${price}")

        # Close add window
        window.add_window.destroy()


    def remove_item(window):
        # Get selected item from listbox
        selected_item = window.items_listbox.curselection()

        # Remove selected item from listbox
        if selected_item:
            window.items_listbox.delete(selected_item)







myButton = Button(window, text=" Back " , font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown',command=back_page)
myButton.place(x=670,y=350)

myButton = Button(window, text=" Proceed to pay " , font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown')
myButton.place(x=250,y=350)

myButton = Button(window, text=" remove from cart " , font=('Times Roman',14,'bold'),bg='Orange Red4',fg='beige',bd=0,activeforeground='beige',activebackground='brown')
myButton.place(x=450,y=350)



window.mainloop()
