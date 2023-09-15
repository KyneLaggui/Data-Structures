"""(The Stock class) Design a class named Stock to represent a company’s stock
that contains"""

"""A constructor that creates a stock with the specified symbol, name, previous price, and current
price."""
class Stock:
    def __init__(self, symbol, name, previousClosingPrice,currentPrice):
        self.__symbol= str(symbol)#Private string named symbol for stock's symbol
        self.__name = str(name)#Private string named name for the stocks's name
        #Private float named previousClosing price to store the stock price for the previous day
        self.__previous_closing_price = float(previousClosingPrice)
        #Private float named current Price to store price for the current time
        self.__current_price = float(currentPrice)

    #Get method for returning the stock name
    def getStockName(self):
        return self.__name
    #Get method for returning the stock symbol
    def getStockSymbol(self):
        return self.__symbol
    #Get method for getting the stocks's previous price
    def getPreviousPrice(self):
        return self.__previous_closing_price
    #Set method for setting the stocks's previous price
    def setPreviousPrice(self, newPrevPrice):
        self.__previous_closing_price = float(newPrevPrice)
    #Get method for getting the stocks's current price
    def getStockCurrentPrice(self):
        return self.__current_price
    #Set method for setting the stocks's current price
    def setStockCurrentPrice(self, newCurrentPrice):
        self.__current_price = float(newCurrentPrice)
    #A method to return the percentage change from previousClosingprice and currentPrice
    def getChangePercent(self):
        percentChange = round(((self.__current_price - self.__previous_closing_price)/self.__previous_closing_price *100),2)
        return percentChange

"""Write a test program that creates a Stock object with the stock symbol INTC, the name Intel
Corporation, the previous closing price of 20.5, and the new current price of
20.35, and display the price-change percentage."""

percentProgram= Stock("INTC", "Intel Corporation", 20.5, 20.35)
print(f"The price-change Percent is: \n{percentProgram.getChangePercent()}%")

    


        