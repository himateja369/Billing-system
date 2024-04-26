from tkinter import *
import random
import time
import datetime

root = Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")
#root.option_add("*Font", "helvetica 20")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=GROOVE)
f1.pack(side=LEFT)

# =================================================================================
#                  TIME MODULE
# ================================================================================
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('perpetua', 50, 'bold'), text="Telugu Bro's Restaurant", fg="aquamarine4", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('castellar', 20, 'bold'), text=localtime, fg="aquamarine4", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)


def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    if (Idly.get() == ""):
        CoIdly = 0
    else:
        CoIdly = float(Idly.get())

    if (Dosa.get() == ""):
        CoDosa = 0
    else:
        CoDosa = float(Dosa.get())

    if (Poori.get() == ""):
        CoPoori = 0
    else:
        CoPoori = float(Poori.get())

    if (Pulav.get() == ""):
        CoPulav = 0
    else:
        CoPulav = float(Pulav.get())

    if (Pongal.get() == ""):
        CoPongal = 0
    else:
        CoPongal = float(Pongal.get())

    if (Drinks.get() == ""):
        CoD = 0
    else:
        CoD = float(Drinks.get())

    CostofIdly = CoIdly * 25
    CostofDrinks = CoD * 20
    CostofDosa = CoDosa * 35
    CostofPoori = CoPoori * 25
    CostPulav = CoPulav * 35
    CostPongal = CoPongal * 20

    CostofMeal = "Rs", str('%.2f' % (CostofIdly + CostofDrinks + CostofDosa + CostofPoori + CostPulav + CostPongal))

    PayTax = ((CostofIdly + CostofDrinks + CostofDosa + CostofPoori + CostPulav + CostPongal) * 0.2)

    TotalCost = (CostofIdly + CostofDrinks + CostofDosa + CostofPoori + CostPulav + CostPongal)

    Ser_Charge = ((CostofIdly + CostofDrinks + CostofDosa + CostofPoori + CostPulav + CostPongal) / 99)

    Service = "Rs", str('%.2f' % Ser_Charge)

    OverAllCost = "Rs", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = "Rs", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    root.destroy()


def Reset():
    rand.set("")
    Idly.set("")
    Dosa.set("")
    Poori.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Pulav.set("")
    Pongal.set("")


# ====================================RESTAURANT MENU INFO 1===========================================================
rand = StringVar()
Idly = StringVar()
Dosa = StringVar()
Poori = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Pulav = StringVar()
Pongal = StringVar()

lblReference = Label(f1, font=('corbel', 16, 'bold'), text="Reference", bd=16, anchor="w",fg="aquamarine4")
lblReference.grid(row=0, column=1)
txtReference = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="grey80",
                     justify='right')
txtReference.grid(row=0, column=2)

lblIdly = Label(f1, font=('candara', 16, 'bold'), text="Idly", bd=16, anchor="w")
lblIdly.grid(row=1, column=1)
txtIdly = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=Idly, bd=10, insertwidth=4, bg="grey80",
                justify='right')
txtIdly.grid(row=1, column=2)

lblDosa = Label(f1, font=('candara', 16, 'bold'), text="Dosa", bd=16, anchor="w")
lblDosa.grid(row=2, column=1)
txtDosa = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=Dosa, bd=10, insertwidth=4, bg="grey80",
                justify='right')
txtDosa.grid(row=2, column=2)

lblPoori = Label(f1, font=('candara', 16, 'bold'), text="Poori", bd=16, anchor="w")
lblPoori.grid(row=3, column=1)
txtPoori = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=Poori, bd=10, insertwidth=4, bg="grey80",
                  justify='right')
txtPoori.grid(row=3, column=2)

lblPulav = Label(f1, font=('candara', 16, 'bold'), text="Pulav", bd=16, anchor="w")
lblPulav.grid(row=4, column=1)
txtPulav = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=Pulav, bd=10, insertwidth=4, bg="grey80",
                 justify='right')
txtPulav.grid(row=4, column=2)

lblPongal = Label(f1, font=('candara', 16, 'bold'), text="Pongal", bd=16, anchor="w")
lblPongal.grid(row=5, column=1)
txtPongal = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=Pongal, bd=10, insertwidth=4, bg="grey80",
                  justify='right')
txtPongal.grid(row=5, column=2)

# ============================================================================================================
#                           RESTAURANT MENU INFO 2
# ========================================================================================

lblDrinks = Label(f1, font=('candara', 16, 'bold'), text="Drinks", bd=16, anchor="w")
lblDrinks.grid(row=0, column=3)
txtDrinks = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="grey80",
                  justify='right')
txtDrinks.grid(row=0, column=4)

lblCost = Label(f1, font=('candara', 16, 'bold'), text="Cost of Meal", bd=16, anchor="w")
lblCost.grid(row=1, column=3)
txtCost = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="grey80",
                justify='right')
txtCost.grid(row=1, column=4)

lblService = Label(f1, font=('candara', 16, 'bold'), text="Service Charge", bd=16, anchor="w")
lblService.grid(row=2, column=3)
txtService = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4, bg="grey80",
                   justify='right')
txtService.grid(row=2, column=4)

lblStateTax = Label(f1, font=('candara', 16, 'bold'), text="State Tax", bd=16, anchor="w")
lblStateTax.grid(row=3, column=3)
txtStateTax = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="grey80",
                    justify='right')
txtStateTax.grid(row=3, column=4)

lblSubTotal = Label(f1, font=('corbel', 16, 'bold'), text="Sub Total", bd=16, anchor="w",fg="aquamarine4")
lblSubTotal.grid(row=4, column=3)
txtSubTotal = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="grey80",
                    justify='right')
txtSubTotal.grid(row=4, column=4)

lblTotalCost = Label(f1, font=('corbel', 16, 'bold'), text="Total Cost", bd=16, anchor="w",fg="aquamarine4")
lblTotalCost.grid(row=5, column=3)
txtTotalCost = Entry(f1, font=('Times New Roman', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="grey80",
                     justify='right')
txtTotalCost.grid(row=5, column=4)

# ==========================================Buttons==========================================================================================
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="white", font=('castellar', 16, 'bold'), width=10, text="Total",
                  bg="DarkSeaGreen4", command=Ref).grid(row=7, column=2)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="white", font=('castellar', 16, 'bold'), width=10, text="Reset",
                  bg="DarkSeaGreen4", command=Reset).grid(row=7, column=3)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="white", font=('castellar', 16, 'bold'), width=10, text="Exit",
                 bg="AntiqueWhite4", command=qExit).grid(row=7, column=4)

fakelab1=Label(f1,text="                                                                                    ",anchor="w")
fakelab2=Label(f1,text="    ",anchor="w")
fakelab3=Label(f1,text="    ",anchor="w")
fakelab4=Label(f1,text="    ",anchor="w")
fakelab5=Label(f1,text="    ",anchor="w")
fakelab6=Label(f1,text="    ",anchor="w")
fakelab7=Label(f1,text="    ",anchor="w")
fakelab1.grid(row=0, column=0)
fakelab2.grid(row=1, column=0)
fakelab3.grid(row=2, column=0)
fakelab4.grid(row=3, column=0)
fakelab5.grid(row=4, column=0)
fakelab6.grid(row=5, column=0)
fakelab7.grid(row=6, column=0)



root.mainloop()