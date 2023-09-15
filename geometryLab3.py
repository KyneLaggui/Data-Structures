import math
"""(Geometry: n-sided regular polygon) An n-sided regular polygon’s sides all have the same
length and all of its angles have the same degree (i.e., the polygon is both equilateral and
equiangular). Design a class named RegularPolygon that contains"""
class RegularPolygon:
    """A constructor that creates a regular polygon with the specified n (default 3), side (default 1), x (default 0), and y (default 0)."""
    def __init__(self, n = 3, sides= 1, x= 0, y= 0):
        #If else statement because the number of sides of a polygon must have atleast 3
        if n < 3:
            self.__numberofsides = 3
        else:
            self.__numberofsides= int(n)#The number of sides in the polygon

        #If else statement because the length of sides must have atleast 1 side
        if sides < 1:
            self.__lengthofsides = 1
        else:
            self.__lengthofsides = float(sides)#the length of the sides

        self.__xCoordinate = float(x)#X coordinate of the center of the polygon
        self.__yCoordinate = float(y)#Y coordinate of the center of the polygon

    #The accessor of the number of sides
    def getNumberSides(self):
        return self.__numberofsides
    #The mutator of the number of sides
    def setNumberSides(self, newNumSides):
        if newNumSides < 3:
            self.__numberofsides = 3
        else:
            self.__numberofsides = newNumSides
    #The accessor of the length of sides
    def getLengthSides(self):
        return self.__lengthofsides
    #The mutator of the length of sides
    def setLengthSides(self, newLengthSides):
        if newLengthSides < 1:
            self.__lengthofsides = 1
        else:
            self.__lengthofsides = newLengthSides
    #The accessor of the xCoordinate
    def getX_Coordinate(self):
        return self.__xCoordinate
    #The mutator of the xCoordinate
    def setX_Coordinate(self, newX_Coordinate):
        self.__xCoordinate = newX_Coordinate
    #The accessor of the yCoordinate
    def getY_Coordinate(self):
        return self.__yCoordinate
    #The mutator of the yCoordinate
    def setX_Coordinate(self, newY_Coordinate):
        self.__yCoordinate = newY_Coordinate
    
    #This method returns the perimeter of the Polygon
    def getPerimeter(self):
        return self.__numberofsides * self.__lengthofsides
    #This method returns the perimeter of the Area
    def getArea(self):
        return round((self.__numberofsides * self.__lengthofsides**2)/(4 * math.tan(math.pi/self.__numberofsides)),2)
        #Round is used to round off the answers to 2 decimals places to make it cleaner

#Test Programs
regularPolygon1= RegularPolygon()#First Polygon using default values
regularPolygon2= RegularPolygon(6,4)#Second Polygon using (6,4) values
regularPolygon3= RegularPolygon(10,4,5.6,7.8)#Third polygon using (3,4) values

#To display the perimeter and area of the polygon
print(f"The Polygon 1 \nPerimeter values: {regularPolygon1.getPerimeter()} \nArea values: {regularPolygon1.getArea()}\n")
print(f"The Polygon 2 \nPerimeter values: {regularPolygon2.getPerimeter()} \nArea values: {regularPolygon2.getArea()}\n")
print(f"The Polygon 3 \nPerimeter values: {regularPolygon3.getPerimeter()} \nArea values: {regularPolygon3.getArea()}\n")


        
