from tkinter import Tk, Label

# langas = Tk()
# langas.geometry("250x200")
# uzrasas = Label(langas, text="Tiesiog tekstas")
# uzrasas.pack() #atvaizduoja
# langas.mainloop() # reikalingas, kad neuzsidarytu,pygame naudoti galima


from tkinter import Tk, Frame, Button, BOTTOM, LEFT, Y
#galima from tkinter import *  (all)
langas = Tk()
langas.geometry("250x200")
virsutinis = Frame(langas)
apatinis = Frame(langas)

mygtukas1 = Button(virsutinis, text="1 mygtukas")
mygtukas2 = Button(virsutinis, text="2 mygtukas")
mygtukas3 = Button(virsutinis, text="3 mygtukas")
mygtukas4 = Button(apatinis, text="4 mygtukas")

virsutinis.pack()
apatinis.pack(side=BOTTOM)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=LEFT)
mygtukas3.pack(side=LEFT)
mygtukas4.pack(side=BOTTOM, fill=Y)

langas.mainloop()




# from tkinter import *
#
# langas = Tk()
#
# uzrasas1 = Label(langas, text="Vardas")
# laukas1 = Entry(langas)
# uzrasas2 = Label(langas, text="Pavardė")
# laukas2 = Entry(langas)
# varnele = Checkbutton(langas, text="Pažymėk varnelę")
#
# uzrasas1.grid(row=0, column=0, sticky=E) # sticky -lygiavimas
# laukas1.grid(row=0, column=1)
# uzrasas2.grid(row=1, column=0, sticky=E)
# laukas2.grid(row=1, column=1)
# varnele.grid(row=2, columnspan=2)
#
# langas.mainloop()



#
# from tkinter import *
# langas = Tk()
#
# def spausdinti():
#     print("Spausdina!")
#
# mygtukas = Button(langas, text="Spausdinti", command=spausdinti)
# mygtukas.pack()
# langas.mainloop()




from tkinter import *
langas = Tk()

def spausdinti(event):
    print("Paspaustas kairys pelės mygtukas!")

def spausdinti2(event):
    print("Paspaustas dešinys pelės mygtukas!")

def spausdinti3(event):
    print("Paspaustas ENTER!")

mygtukas = Button(langas, text="Spausdinti")
mygtukas.bind("<Button-1>", spausdinti)
mygtukas.bind("<Button-3>", spausdinti2)
langas.bind("<Return>", spausdinti3)
mygtukas.pack()

langas.mainloop()




