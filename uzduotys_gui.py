# 1 uzduotis: Sukurti programą su grafine sąsaja, kuri:
# *Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti
# vardą
# *Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku
# atspausdintų "Labas, {vardas}!"+++

# from tkinter import *
#
# langas = Tk()
#
# def spausdinti():
#     vardas = laukas1.get()
#     print(f"Labas, {vardas}!")
#
# def spausdinti3(event):
#     print("Paspaustas ENTER!")
#
# uzrasas1 = Label(langas, text="Įveskite vardą")
# uzrasas1.grid(row=0, column=0, sticky=E)
#
# laukas1 = Entry(langas)
# laukas1.grid(row=0, column=1)
#
# mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
# mygtukas.grid(row=1, column=0, columnspan=2)
#
# langas.bind("<Return>", spausdinti3)
# langas.mainloop()


# 2 uzduotis:Patobulinti 1 užduoties programą, kad ji:
# Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką, bet ir paspaudus
# mygtuką "Enter"+++++
#
# from tkinter import *
#
# langas = Tk()
#
# def spausdinti():
#     vardas = laukas1.get()
#     print(f"Labas, {vardas}!")
#
# def spausdinti3(event):
#     print("Paspaustas ENTER!")
#
# uzrasas1 = Label(langas, text="Įveskite vardą")
# uzrasas1.grid(row=0, column=0, sticky=E)
#
# laukas1 = Entry(langas)
# laukas1.grid(row=0, column=1)
#
# mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
# mygtukas.grid(row=2, column=0, columnspan=2)
# mygtukas2 = Button(langas, text="enter", command=spausdinti)
# mygtukas2.grid(row=0, column=2, columnspan=2)
#
# langas.bind("<Return>", spausdinti3)
# langas.mainloop()



# 3 uzduotis: Patobulinti 2 užduoties programą, kad ji turėtų meniu
# pavadinimu "Meniu", kuriame:
# *Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje,
# kurioje spausdinamas pasisveikinimo tekstas+++
# *Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto eilutėje
# butų atspausdintas paskutinis atspausdintas tekstas+++
# *Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas++++
# *Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys+++++

# from tkinter import *
#
# langas = Tk()
#
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff=0)
#
#
# def spausdinti():
#     vardas = laukas1.get()
#     print(f"Labas, {vardas}!")
#     rezultatas["text"] = f"Labas {vardas}!"
#
# def spausdinti3(event):
#     print("Paspaustas ENTER!")
#
# def istrinti():
#     print("Tekstas istrintas")
#     rezultatas["text"] = f""
#
# def atkurti():
#     vardas = laukas1.get()
#     print("Tekstas atkurtas")
#     rezultatas["text"] = f"Labas {vardas}!"
#
# def iseiti():
#     print("Programa isjungta")
#     quit(langas)
#
# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Isvalyti", command=istrinti)
# submeniu.add_command(label="Atkurti", command=atkurti)
# submeniu.add_separator()
# submeniu.add_command(label="Iseiti", command=iseiti)
#
#
# uzrasas1 = Label(langas, text="Įveskite vardą")
# uzrasas1.grid(row=0, column=0, sticky=E)
#
# laukas1 = Entry(langas)
# laukas1.grid(row=0, column=1)
#
# mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
# mygtukas.grid(row=2, column=0, columnspan=2)
#
# mygtukas2 = Button(langas, text="Enter", command=spausdinti)
# mygtukas2.grid(row=0, column=2, columnspan=2)
#
# rezultatas = Label(langas, text="")  #grazina teksta labas + vardas
# rezultatas.grid(row=3, columnspan=3)
#
# langas.bind("<Return>", spausdinti3)
# langas.mainloop()


# 4 uzduotis: Patobulinti 3 užduoties programą, kad ji turėtų statuso juostą apačioje,
# kurioje:
# *Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# *Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# *Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo
# tekstas Nuspaudus klaviatūros mygtuką "Escape", uždarytų programos langą

from tkinter import *

langas = Tk()

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

status = Label(langas, text="Nieko nedaro...", bd=1, relief=SUNKEN, anchor=W)

def update_status_bar(text):
    status["text"] = text

def spausdinti():
    vardas = laukas1.get()
    print(f"Labas, {vardas}!")
    rezultatas["text"] = f"Labas {vardas}!"

def spausdinti3(event):
    print("Paspaustas ENTER!")

def istrinti():
    print("Tekstas istrintas")
    rezultatas["text"] = f""

def atkurti():
    vardas = laukas1.get()
    print("Tekstas atkurtas")
    rezultatas["text"] = f"Labas {vardas}!"

def iseiti():
    print("Programa isjungta") #ARBA langas.destroy()
    quit(langas)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Isvalyti", command=istrinti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Iseiti", command=iseiti)


uzrasas1 = Label(langas, text="Įveskite vardą")
uzrasas1.grid(row=0, column=0, sticky=E)

laukas1 = Entry(langas)
laukas1.grid(row=0, column=1)

mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
mygtukas.grid(row=2, column=0, columnspan=2)

mygtukas2 = Button(langas, text="Enter", command=spausdinti)
mygtukas2.grid(row=0, column=2, columnspan=2)

rezultatas = Label(langas, text="")  #grazina teksta labas + vardas
rezultatas.grid(row=3, columnspan=3)

#STATUSO JUOSTA
status.grid(row=6, columnspan=3, sticky=W+E)

langas.bind("<Return>", spausdinti3)
langas.mainloop()



# 5 uzduotis: Perdaryti bet kurią ankstesnėse pamokose sukurtą arba savo programą,
# kurioje vartotojas turėjo įvesti duomenis, į programą su grafine sąsaja.
# Pvz., tą, kuri atrenka keliamuosius metus, skaičiuoja laiką nuo praeitos datos,
# pateikia informaciją apie įvestą eilutę ar pan.


# 6 uzduotis: Perdaryti biudžeto programą (pvz. su pickle), pridedant tkinter grafinę sąsają.

