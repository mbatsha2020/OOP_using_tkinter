# Import libraries
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('500x700')


# Creating a variables for prices
sctk = 40
mvtk = 75
thtk = 100

# Creating Tkinter widgets
tkvar = StringVar()
cellno = Entry(root, width=10)
tkcat = ttk.Combobox(root, textvariable=tkvar, width=10, value=["Soccer", "Movie", "Theater"])
nrtk = ttk.Spinbox(root, from_=0, to=20, state="readonly")
celllb = Label(root, text="Cellphone number:")
catlb = Label(root, text="Ticket Category:")
nrlb = Label(root, text="Number of tickets:")
anslb = Label(root)


#Creating class
class clsTiketSales:
 def __init__(self, celno, nrtkts, price):
   self.celno = celno
   self.nrtkts = nrtkts
   self.price = price

   return

       # Creates function for button
def calc():

    tksale = clsTiketSales(cellno.get(), float(nrtk.get()), tkcat.get())

# Desicion tree
if tkcat.get() == "Soccer":
 scprice = sctk * int(nrtk.get()) + (14/100)
anslb.config(text="Price:"+ str(scprice) + "\n" + "tickets:"+str(nrtk.get()) + "\n" +"Number:"+ str(cellno.get()))
if tkcat.get() == "Movie":
 mvprice = mvtk * int(nrtk.get()) + (14/100)
anslb.config(text="Price:"+ str(mvprice) + "\n" + "tickets:"+str(nrtk.get()) + "\n" +"Number:"+ str(cellno.get()))
if tkcat.get() == "Theater":
 thprice = thtk * int(nrtk.get()) + (14/100)
anslb.config(text="Price:"+ str(scprice) + "\n" + "tickets:"+str(nrtk.get()) + "\n" +"Number:"+ str(cellno.get()))



# function

#Creating button
tkbtn = Button(root, text="calculate", command=calc, width=20, height=1)

# Adds widgets
celllb.grid(row=0, column=0, sticky=W)
catlb.grid(row=4, column=0, sticky=W)
nrlb.grid(row=4, column=0, sticky=W)
cellno.grid(row=0, column=1)
tkcat.grid(row=3, column=1)
nrtk.grid(row=2, column=1)
anslb.grid(row=8, column=0)
tkbtn.grid(row=8, column=0)


root.mainloop()
