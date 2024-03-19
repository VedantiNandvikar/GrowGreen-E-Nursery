import tkinter
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox


def clear_item():
    qty_spinbox.delete(0, tkinter.END)
    qty_spinbox.insert(0, "1")
    desc_entry.delete(0, tkinter.END)
    price_entry.delete(0, tkinter.END)



invoice_list = []


def add_item():
    name = first_name_entry.get()
    address= last_name_entry.get()
    qty = int(qty_spinbox.get())
    desc = desc_entry.get()
    price =int(price_entry.get())
    line_total = qty * price
    invoice_item = [name,address,qty, desc, price, line_total]
    tree.insert('', 0, values=invoice_item)
    clear_item()

    invoice_list.append(invoice_item)


def new_invoice():
    first_name_entry.delete(0, tkinter.END)
    last_name_entry.delete(0, tkinter.END)
    phone_entry.delete(0, tkinter.END)
    clear_item()
    tree.delete(*tree.get_children())

    invoice_list.clear()


def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = first_name_entry.get() + last_name_entry.get()
    phone = phone_entry.get()
    subtotal = sum(item[4] for item in invoice_list)
    salestax = 0.1
    total = subtotal * (1 - salestax)

    doc.render({"name": name,
                "phone": phone,
                "invoice_list": invoice_list,
                "subtotal": subtotal,
                "salestax": str(salestax * 100) + "%",
                "total": total})

    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)

    messagebox.showinfo("Invoice Complete", "Invoice Complete")

    new_invoice()


window = tkinter.Tk()
window.title("Invoice Generator Form")
window.config(background='light yellow')

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)
frame.config(background='light yellow')

first_name_label = tkinter.Label(frame, text="Name")
first_name_label.grid(row=0, column=0)
first_name_label.config(background='light yellow')
last_name_label = tkinter.Label(frame, text="Address")
last_name_label.grid(row=0, column=1)
last_name_label.config(background='light yellow')

first_name_entry = tkinter.Entry(frame)
last_name_entry = tkinter.Entry(frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

phone_label = tkinter.Label(frame, text="Phone")
phone_label.grid(row=0, column=2)
phone_label.config(background='light yellow')
phone_entry = tkinter.Entry(frame)
phone_entry.grid(row=1, column=2)

qty_label = tkinter.Label(frame, text="Qty")
qty_label.grid(row=2, column=0)
qty_label.config(background='light yellow')
qty_spinbox = tkinter.Spinbox(frame, from_=1, to=100)
qty_spinbox.grid(row=3, column=0)
qty_spinbox.config(background='light yellow')

desc_label = tkinter.Label(frame, text="Plant Name")
desc_label.grid(row=2, column=1)
desc_label.config(background='light yellow')
desc_entry = tkinter.Entry(frame)
desc_entry.grid(row=3, column=1)

price_label = tkinter.Label(frame, text="Price")
price_label.grid(row=2, column=2)
price_label.config(background='light yellow')
price_entry = tkinter.Entry(frame)
price_entry.grid(row=3, column=2)


add_item_button = tkinter.Button(frame, text="Add item", command=add_item)
add_item_button.grid(row=4, column=2, pady=5)
add_item_button.config(background='light yellow')

columns = ('name','address','qty', 'desc', 'price', 'total')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('name', text='Name')
tree.heading('address', text='Address')
tree.heading('qty', text='Qty')
tree.heading('desc', text='PlantName')
tree.heading('price', text='Price')
tree.heading('total', text="Total")

tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

save_invoice_button = tkinter.Button(frame, text="Generate Invoice", command=generate_invoice)
save_invoice_button.grid(row=6, column=0, columnspan=3, sticky="news", padx=20, pady=5)
save_invoice_button.config(background='brown')
new_invoice_button = tkinter.Button(frame, text="New Invoice", command=new_invoice)
new_invoice_button.grid(row=7, column=0, columnspan=3, sticky="news", padx=20, pady=5)
new_invoice_button.config(background='brown')

window.mainloop()