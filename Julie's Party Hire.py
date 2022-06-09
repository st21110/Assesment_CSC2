#Date: 3/6/22
#Author: Prisha

"""
Julie's Party Hire. 

This code will use functions along side methods to...

"""

#imports for the project
from tkinter import *
from tkinter import ttk
from tkinter import font

#Naming the roots
root = Tk()
root.title("Julie's Party Hires")


#Quit Function
def quit():
    exit()


#Labels for entries
Label(root, text="Customer Name:").grid(row=4,column=2)
Label(root, text="Item Hired:").grid(row=5,column=2)
Label(root, text="Quantity Hired:").grid(row=6,column=2)
Label(root, text="Receipt Number:").grid(row=7,column=2)
Label(root, text="Row Number:").grid(row=11,column=2)

#Heading
Label(root,text="Julie's Party Hire", font='bold', bg='orange').grid(row=1,column=4)

#Values for item hire
item_names = ["Chairs","Tables","Speakers","Coloured Lights",
"Helium Tanks", "Gas Barbeque","Marquees","Inflatable Pool",
"Bubble Machine","Glassware","Microphone","Karaoke Machine",
"Bouncy Castle","Cake Stand" ,"Fog Machine"]



#Entries
def temp_text(e):
   (customer_name).delete(0,"end")
customer_name = Entry(root,bg="white", width=17, borderwidth=2)
customer_name.insert(0, "Full Name")
customer_name.bind("<FocusIn>", temp_text)
customer_name.grid(row=4,column=3)

items=StringVar()
item_hired = ttk.Combobox(root, textvariable = items, values =(item_names),
state = "readonly",width=17)
item_hired.grid(row=5, column=3)

quantity_hired = Entry(root)
quantity_hired.grid(row=6,column=3)
receipt_number = Entry(root)
receipt_number.grid(row=7,column=3)

delete_item = Entry(root)
delete_item .grid(row=11,column=3)

#customer_details = ([customer_name.get(),item_hired.get(),quantity_hired.get(),receipt_number.get()])
#Print details function 
def print_details():
    global total_entries
    name_count = 0
    
    while name_count < total_entries :
        Label(root, text=name_count).grid(column=0,row=name_count+13) 
        Label(root, text=(customer_details[name_count][0])).grid(column=1,row=name_count+13)
        Label(root, text=(customer_details[name_count][1])).grid(column=2,row=name_count+13)
        Label(root, text=(customer_details[name_count][2])).grid(column=3,row=name_count+13)
        Label(root, text=(customer_details[name_count][3])).grid(column=4,row=name_count+13)
        name_count +=  1


def append_details():
    global customer_details,customer_name,item_hired,quantity_hired,receipt_number,total_entries
    if len(customer_name.get()) != 0:
        customer_details.append([customer_name.get(),item_hired.get(),quantity_hired.get(),receipt_number.get()])
        customer_name.delete(0,'end')
        item_hired.set("")
        quantity_hired.delete(0,'end')
        receipt_number.delete(0,'end')
        total_entries += 1
        print_details()
        

def delete_row ():
    global customer_details, delete_item, total_entries, name_count
    del customer_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0,'end')
    Label(root, text="       ").grid(column=0,row=name_count+12) 
    Label(root, text="       ").grid(column=1,row=name_count+12)
    Label(root, text="       ").grid(column=2,row=name_count+12)
    Label(root, text="       ").grid(column=3,row=name_count+12)
    Label(root, text="       ").grid(column=4,row=name_count+12)

#Buttons
Button(root, text="Append",command=append_details,width=17).grid(row=8,column=3)
Button(root, text="Print Details",command=print_details,width=17).grid(row=8,column=4)
Button(root,text="Delete",command=delete_row).grid(row=11,column=4)
Button(root,text="Quit",command=quit).grid(row=13,column=5)

def main():
    global root
    global customer_details,total_entries
    customer_details = []
    total_entries = 0
    root.mainloop()
    root.geometry("400x400")


main()
