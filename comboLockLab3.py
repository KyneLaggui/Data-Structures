"""Implement a class ComboLock that works like the combination lock in a gym locker. The lock is
constructed with a combination—three numbers between 0 and 39. The reset method resets the
dial so that it points to 0. The turnLeft and turnRight methods turn the dial by a given number of
ticks to the left or right. The open method attempts to open the lock. The lock opens if the user
first turned it right to the first number in the combination, then left to the second, and then right
to the third"""

class ComboLock:
	def __init__(self, secret1, secret2, secret3):
		self.secret_1= secret1
		self.secret_2 = secret2
		self.secret_3 = secret3
		self.current = 0
		self.status = 0

	#This method is to reset the the dial to 0
	def reset(self):
		self.current= 0
		self.status =0
		print("________________")
		print("Lock is Reset")

	#This method subtracts the current dial to the ticks
	def turnLeft(self,ticks):
		self.current = self.current - ticks
		#If the current dial is less than zero, it will add it to 39
		if self.current <0:
			self.current= 39 + self.current
		#To display the values of the ticks and the current status
		print(f"Left Ticks= {ticks}\nCurrent= {self.current}")

	#This method adds the current dial to the ticks
	def turnRight(self, ticks):
		#If the current dial is more than 40, it will get its remainder
		self.current = (self.current + ticks)%40
		#To display the values of the ticks and the current status
		print(f"Right Ticks= {ticks}\nCurrent= {self.current}")
	
	def open(self):
		while True:
			try:#Try and catch mechanism
				#To ask the first tick of the user
				rotateTick = int(input("Enter the First number of ticks [Turn Right]: "))
				self.turnRight(rotateTick)
				#If the input is correct it will continue
				if self.current == self.secret_1:
					self.status= 1#It will add a status because if it reaches 3 the Combolock will open
					print("First pattern Unlock")
				#If the input is incorrect it will ask if the user wants to reset or exit
				else:
					print("Incorrect Pattern")
					print("The Lock is NOT Open")
					userReset = int(input("\n[0]Reset \n[1]Exit \nDo you wish to reset? "))
					#If the user chooses to 
					if userReset ==0:
						self.reset()
						continue
					elif userReset ==1:
						break
				#To ask the second tick of the user
				rotateTick = int(input("Enter the Second number of ticks [Turn Left]: "))
				self.turnLeft(rotateTick)
				if self.current == self.secret_2:
					self.status =2 
					print("Second pattern Unlock")
				else:
					print("Incorrect Pattern")
					print("The Lock is NOT Open")
					userReset = int(input("\n[0]Reset \n[1]Exit \nDo you wish to reset? "))
					if userReset ==0:
						self.reset()
						continue
					elif userReset ==1:
						break
				#To ask the third tick of the user
				rotateTick = int(input("Enter the Third number of ticks [Turn Right]: "))
				self.turnRight(rotateTick)
				if self.current == self.secret_3:
					self.status=3 
					break
				else:
					print("Incorrect Pattern")
					print("The Lock is NOT Open")
					userReset = int(input("\n[0]Reset \n[1]Exit \nDo you wish to reset? "))
					if userReset ==0:
						self.reset()
						continue
					elif userReset ==1:
						break

			except ValueError:#If the user inputs a non integer it will reset to its first question
				print("Invalid Value, Input a number/Integer")
				continue
		
		if self.status ==3:#If the user correctly tick it 3 times, the combolock will open
			print("Lock is Open")
			print("________________")
		
#To run the program		
currentlock1= ComboLock(10,20,30)#The values for the Combolock
open= currentlock1.open()

"""
Programmed by Kyne Domerei N. Laggui from BSCOE 2-1
Alternative approach for the Program 
class ComboLock:
    def __init__(self, secret1, secret2, secret3):
        self.secret_1= secret1
        self.secret_2 = secret2
        self.secret_3 = secret3
        self.current = 0
        self.status = 0

    def reset(self):
        self.current= 0
        self.status =0
        print("Lock is reset")

    def turnLeft(self,ticks):
        
        self.current = self.current - ticks
        if self.current <0:
            self.current= 39 + self.current
        print(f"Left ticks = {ticks} and current {self.current}")
        if self.current == self.secret_2:
            self.status =2 
        else:
            self.status =0

    def turnRight(self, ticks):
        self.current = self.current + ticks
        if self.current > 39:
            self.current = self.current - 39
        print(f"Right ticks = {ticks} and current {self.current}")
        if self.current == self.secret_1:
            self.status= 1
        elif self.current == self.secret_3:
            self.status=3 
        else:
            self.status =0

    def open(self):
        if self.status ==3:
            print("Lock is Open")
        if self.status != 3:
            print("The lock is not open")

currentlock1= ComboLock(10,20,30)
currentlock1.reset()
currentlock1.turnRight(10)
currentlock1.turnLeft(29)
currentlock1.turnRight(10)
currentlock1.open()
            
"""

			
