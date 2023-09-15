#The modules that are needed to import
from tkinter import *
from tkinter import messagebox

#The format of the window
def mainWindow():
    global CandyMachineWindow
    CandyMachineWindow = Tk() #The Package for the window
    CandyMachineWindow.geometry("300x400") 
    CandyMachineWindow.resizable(0,0) 
    CandyMachineWindow.title("Kaydee's Candies") 
    CandyMachineWindow.config(bg="PaleVioletRed1")
    Label(CandyMachineWindow, text="   Kaydee's Candies   ", font=("Helvetica", 18, "bold"), fg="white", bg="PaleVioletRed1").place(x= 30, y=45)
    Label(CandyMachineWindow, text="Home of Sweet Delicacies", font=("Helvetica",9, "italic"), fg="white", bg="PaleVioletRed1").place(x= 75, y=75)
mainWindow()

#The classes that are needed:
#This class accepts the amount and shows the current balance of the Register
class Cash_Register:
    def __init__(self, cashonHand = 500):
        if cashonHand < 0:
            self.__cashonHand = 500
        else:
            self.__cashonHand = cashonHand
    #This method displays the current balance of the Cash Register
    def currentBalance(self):
        return self.__cashonHand
    #This method accepts what the user pays and add it to the Cash Register
    def acceptAmount(self, userMoney):
        self.__cashonHand += userMoney

#The class stores the number of product and how much an item cost 
class Dispenser:
    def __init__(self, numberofItems= 50, costofItems= 50):
        if numberofItems <0:
            self.__numberItems = 50
        else:
            self.__numberItems = numberofItems
        if costofItems <0:
            self.__costItems = 50
        else:
            self.__costItems = costofItems
    #This returns the number of items of a particular product
    def getCount(self):
        return self.__numberItems
    #This method returns the price of an item 
    def getProductCost(self):
        return self.__costItems
    #This method reduces the number of item if a user make a purchase
    def makeSale(self):
        self.__numberItems -= 1

#To call and assign the class
Cashier = Cash_Register()
Candy = Dispenser()
Chips = Dispenser()
Gum = Dispenser()
Cookies = Dispenser()

#This method is to store the stocks and the cashier balance on the main window
def mainValue():
    global cashierBalance, msgBuy, userPayment, stockCandy, stockChip, stockGum, stockCookies
    cashierBalance= StringVar()
    msgBuy = StringVar()
    userPayment = StringVar()
    stockCandy = StringVar()
    stockChip = StringVar()
    stockGum = StringVar()
    stockCookies = StringVar()
    cashierBalance.set(f"Balance of the Cash Register: {Cashier.currentBalance()}")
    stockCandy.set(f"Candy: {Candy.getCount()}")
    stockChip.set(f"Chips: {Chips.getCount()}")
    stockGum.set(f"Gum: {Gum.getCount()}")
    stockCookies.set(f"Cookies: {Cookies.getCount()}")
mainValue()

#This method is to sell the product selected by the User
def sellProduct(machineItem, cashAccept):
    try: #Try and catch mechanism
        product_cost = machineItem.getProductCost()
        if machineItem.getCount():
            userPay= int(userPayment.get())
            userChange = userPay - product_cost
            userPayment.set('')
            if userChange < 0:
                messagebox.showerror("Error", f"Insufficient Payment {product_cost - userPay} cents more")
                return
            else: 
                msgBuy.set(f"Your change is {userChange}, Come Again")
                cashAccept.acceptAmount(product_cost)
                machineItem.makeSale()
                cashierBalance.set(f"Balance of the Cash Register: {Cashier.currentBalance()}")
                stockCandy.set(f"Candy: {Candy.getCount()}")
                stockChip.set(f"Chips: {Chips.getCount()}")
                stockGum.set(f"Gum: {Gum.getCount()}")
                stockCookies.set(f"Cookies: {Cookies.getCount()}")
                return
        else: 
            messagebox.showerror("Sorry", "The product is no longer available")
            return
    except ValueError:
        messagebox.showerror("Value cannot be accepted", "Please Input an Integer/Number")

#This method is for the window of the Candy
def sellCandy():
    candyWindow = Toplevel(CandyMachineWindow)
    #The format for the Candy Window
    candyWindow.config(bg = "LightPink1")
    candyWindow.title("Candy")
    candyWindow.geometry("250x250")
    candyWindow.resizable(0,0)
    msgBuy.set("")
    Label(candyWindow, text="Insert Money:", font='helvetica 12 bold' ,fg= "white", bg="LightPink1").place(x = 10, y = 15)
    #Where the user can type in the amount of their money
    userEntry_Payment = Entry(candyWindow, textvariable = userPayment, width = 25)
    userEntry_Payment.place(x= 50, y=45)
    #To show the price of a product
    Label(candyWindow, text=f"The price of a Candy is: {Candy.getProductCost()} ", font='helvetica 10 bold',fg= "white", bg="LightPink1").place(x= 40, y=75)
    #This will store the change of the User
    Label(candyWindow, textvariable= msgBuy, font='helvetica 10 bold',fg= "white", bg="LightPink1").place(x= 25, y=95)
    #After the Pay button is pressed, it will process the product to sell it
    Button(candyWindow,text="Pay", fg = "LightPink1", font='arial 12 bold',bg='white',
    command = lambda: sellProduct(Candy, Cashier)).place(x = 150, y=205)
    candyWindow.mainloop()

#This method is for the window of the Chips
def sellChip():
    ChipWindow = Toplevel(CandyMachineWindow)
    ChipWindow.config(bg = "LightPink1")
    ChipWindow.title("Chip")
    ChipWindow.geometry("250x250")
    ChipWindow.resizable(0,0)
    msgBuy.set("")
    Label(ChipWindow, text="Insert Money:", font='helvetica 12 bold',fg= "white", bg="LightPink1").place(x = 10, y = 15)
    userEntry_Payment = Entry(ChipWindow, textvariable = userPayment, width = 25)
    userEntry_Payment.place(x= 50, y=45)
    Label(ChipWindow, text=f"The price of a Chip is: {Chips.getProductCost()} ", font='helvetica 10 bold',fg= "white", bg="LightPink1").place(x= 40, y=75)
    Label(ChipWindow, textvariable= msgBuy, font='helvetica 10 bold',fg= "white", bg="LightPink1").place(x= 25, y=95)
    Button(ChipWindow,text="Pay", fg = "LightPink1", font='arial 12 bold',bg='white',
    command = lambda: sellProduct(Chips, Cashier)).place(x = 150, y=205)
    ChipWindow.mainloop()

#This method is for the window of the Gum
def sellGum():
    GumWindow = Toplevel(CandyMachineWindow)
    GumWindow.config(bg = "LightPink1")
    GumWindow.title("Gum")
    GumWindow.geometry("250x250")
    GumWindow.resizable(0,0)
    msgBuy.set("")
    Label(GumWindow, text="Insert Money:", font='helvetica 12 bold', fg= "white", bg="LightPink1").place(x = 10, y = 15)
    userEntry_Payment = Entry(GumWindow, textvariable = userPayment, width = 25)
    userEntry_Payment.place(x= 50, y=45)
    Label(GumWindow, text=f"The price of a Gum is: {Gum.getProductCost()} ", font='helvetica 10 bold', fg= "white", bg="LightPink1").place(x= 40, y=75)
    Label(GumWindow, textvariable= msgBuy, font='helvetica 10 bold', fg= "white", bg="LightPink1").place(x= 25, y=95)
    Button(GumWindow,text="Pay", fg = "LightPink1", font='arial 12 bold',bg='white',
    command = lambda: sellProduct(Gum, Cashier)).place(x = 150, y=205)
    GumWindow.mainloop()

#This method is for the window of the Cookies
def sellCookies():
    CookiesWindow = Toplevel(CandyMachineWindow)
    CookiesWindow.config(bg = "LightPink1")
    CookiesWindow.title("Candy")
    CookiesWindow.geometry("250x250")
    CookiesWindow.resizable(0,0)
    msgBuy.set("")
    Label(CookiesWindow, text="Insert Money:", font='helvetica 12 bold',fg= "white", bg="LightPink1").place(x = 10, y = 15)
    userEntry_Payment = Entry(CookiesWindow, textvariable = userPayment, width = 25)
    userEntry_Payment.place(x= 50, y=45)
    Label(CookiesWindow, text=f"The price of a Candy is: {Cookies.getProductCost()} ", font='helvetica 10 bold',fg= "white", bg="LightPink1").place(x= 40, y=75)
    Label(CookiesWindow, textvariable= msgBuy, font='helvetica 10 bold',fg= "white", bg="LightPink1").place(x= 25, y=95)
    Button(CookiesWindow,text="Pay", fg = "LightPink1", font='arial 12 bold',bg='white',
    command = lambda: sellProduct(Cookies, Cashier)).place(x = 150, y=205)
    CookiesWindow.mainloop()

#This method is to Exit the window
def Exit():
    CandyMachineWindow.destroy()

#The buttons for the main window
def MainButtons():
    candyButton= Button(CandyMachineWindow, text= "   Candy   ", fg= "white", font= "Helvetica 15 bold", bg= "VioletRed1", command= sellCandy)
    candyButton.place(x=35, y=110)
    chipButton= Button(CandyMachineWindow, text= "   Chips   ", fg= "white", font= "Helvetica 15 bold", bg= "VioletRed1", command= sellChip)
    chipButton.place(x=155, y=110)
    gumButton= Button(CandyMachineWindow, text= "    Gum    ", fg= "white", font= "Helvetica 15 bold", bg= "VioletRed1", command= sellGum)
    gumButton.place(x=35, y=160)
    cookieButton= Button(CandyMachineWindow, text= "  Cookie  ", fg= "white", font= "Helvetica 15 bold", bg= "VioletRed1", command= sellCookies)
    cookieButton.place(x=155, y=160)
    exitButton= Button(CandyMachineWindow, text= "   Exit   ", fg= "white", font= "Helvetica 15 bold", bg= "VioletRed1", command= Exit)
    exitButton.place(x=100, y=210)
MainButtons()

#This method is store the text and values in the main window
def mainText():
    Label(CandyMachineWindow, textvariable = cashierBalance, font='Helvetica 13 bold', bg="PaleVioletRed1", fg="White").place(x=15, y=265)
    Label(CandyMachineWindow, text= "STOCKS", font='Helvetica 13 bold', bg="PaleVioletRed1", fg="White").place(x=110, y=290)
    Label(CandyMachineWindow, textvariable= stockCandy, font='Helvetica 13 bold', bg="VioletRed1", fg="White").place(x=35, y=320)
    Label(CandyMachineWindow, textvariable= stockChip, font='Helvetica 13 bold', bg="VioletRed1", fg="White").place(x=35, y=350)
    Label(CandyMachineWindow, textvariable= stockGum, font='Helvetica 13 bold', bg="VioletRed1", fg="White").place(x=200, y=320)
    Label(CandyMachineWindow, textvariable= stockCookies, font='Helvetica 13 bold', bg="VioletRed1", fg="White").place(x=175, y=350)
mainText()
CandyMachineWindow.mainloop()#Continous display of the output window and run the Tkinter