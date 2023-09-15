class Animal:#The class named animal
    def __init__(self,name) :
        self.name = name
        #To display if an animal has been born
        print("__________________________ \nAn animal has been born")

    def eat(self):#The eat method to display and indicate the animal is eating
        print("Munch munch")
    
    def make_noise(self):#The make noise method to display and indicate that the animal is making noise
        print(f"Grrr says {self.name}")#Also calling the name of the animal
        
class Cat(Animal):#A subclass to make the animal as the parent
    def __init__(self, name):
        super().__init__(name)
        #To display if a cat has been born
        print("A cat has been born")

    def make_noise(self):#The make noise method, to display and indicate that the cat is making noise
        print(f"Meow says {self.name}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A dog has been born")

    def make_noise(self,):#The make noise method to display and indicate that the dog is making noise
        print(f"Bark says {self.name}")

"""Create a test program that will:
 * Code that creates a cat, two dogs, and an animal.
 * Sets the name for each animal.
 * Code that calls eat() and make_noise() for each animal. (Don't forget this!)"""
#Cat
cat_1= Cat("Candido")
cat_1.eat()
cat_1.make_noise()
#First Dog
dog_1= Dog("Cheetos")
dog_1.eat()
dog_1.make_noise()
#Second dog
dog_2= Dog("Jake")
dog_2.eat()
dog_2.make_noise()
#Default Animal
Anims= Animal("Snow")
Anims.eat()
Anims.make_noise()