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
    def acceptAmount(self, cashIn): 
        self.__cashonHand += cashIn

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
        
#This class shows the selection for the user, to sell a product and for the user to choose their desired product
class mainProgram:
    #This method is to print the selections of the user
    def showSelection(self):
        global userInputChoice
        print("_________________________________")
        print("Welcome to Kaydee's Candies Shop")
        print("To select an item enter")
        print("""
[1] Candy 
[2] Chips
[3] Gum
[4] Cookies
[0] View Balance
[9] Exit
        """)
        #To enter the choice of the user
        userInputChoice= int(input("Enter your choice: "))

    #This method is to sell the product selected by the User
    def sellProduct(self, machineItem, cashAccept):
        try:#The try and catch mechanism
            product_cost = machineItem.getProductCost()
            if machineItem.getCount():
                print(f"The product cost {product_cost} cents")
                userPay = int(input("How much money are you going to input? "))
                print(f"I receive {userPay}, Thank you")
                userChange = userPay - product_cost
                if userChange < 0:
                    print(f"You need {product_cost - userPay} cents more")
                    print("You dont have enough money")
                    return
                else: 
                    print(f"Your change is {userChange}, Come Again")
                    cashAccept.acceptAmount(product_cost)
                    machineItem.makeSale()
                    return
            else: 
                print("Product is Sold Out")
                return
        #The value error is needed if the user input a wrong data value
        except ValueError: 
            print("Value cannot be accepted: Please Input an Integer/Number")
  
    #This method is for the user to pick their desired choice or product
    def userChoice(self):
        #This line of codes are to call the class
        Cashier = Cash_Register()
        Candy = Dispenser()
        Chips = Dispenser()
        Gum = Dispenser()
        Cookies = Dispenser()
        while True:
            self.showSelection()
            if userInputChoice == 1: 
                self.sellProduct(Candy, Cashier)
            elif userInputChoice ==2:
                self.sellProduct(Chips, Cashier)
            elif userInputChoice ==3: 
                self.sellProduct(Gum, Cashier)
            elif userInputChoice ==4:
                self.sellProduct(Cookies, Cashier)
            elif userInputChoice ==0:
                print(f"Balance of the Cashier is {Cashier.currentBalance()}")
            elif userInputChoice ==9:
                break

#To run the output
Candy_machine_Program = mainProgram()
Candy_machine_Program.userChoice()


    


   





        
