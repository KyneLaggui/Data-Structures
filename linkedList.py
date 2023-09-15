class NODES:
    def __init__(self, value = None, next= None):
        self.value = value #The entire data
        self.next = next #Next Element

class LINKEDLIST:
    def __init__(self):
        self.head = None #Head or the entry point of the linked list
    
    def createList(self,value):
        #If the value is null, we just return the value
        if self.head is None:
            self.head = NODES(value)
            return
        iterateAppend = self.head
        #Iterate through the list
        while iterateAppend.next:
            iterateAppend = iterateAppend.next#Iterate through the next element
        iterateAppend.next = NODES(value)#If we iterate to the last element we display the value
        
    #Taking the value and inserting at the beginning of the linked list
    def addBeginning(self, newBeginning):
        #Inserting the data into front and it will be the current head
        new_head = NODES(newBeginning,self.head)
        self.head = new_head

    def display(self):
        #If the linked list is blank
        iterate_to_display = self.head
        display_list = ""
        #Iterating through the linked list
        while iterate_to_display:
            #Then looping it one by one to display it
            display_list += str(iterate_to_display.value) + " ==> "
            iterate_to_display = iterate_to_display.next
        print(display_list)

    #Adding the values in a certain index that the user wants
    def addAfter(self,elemIndex,newIndex):
        #If the index is less than the head and also greater than the length of the count
        if elemIndex <0 or elemIndex >= self.count():
            print("[INDEX IS INVALID]")#It will raise an exception
            self.main()
        #If the element is at zero index, add it at the beginning   
        if elemIndex==0:
            self.addBeginning(newIndex)
            return
        iterate_to_add_index = self.head
        count_linked_list = 0
        #Count until it gets the specific index the user want to put it
        while iterate_to_add_index:
            #Get the index and then add it to the certain index  
            if count_linked_list == elemIndex -1:
                #And then the element on that index will be push to next index
                 new_index = NODES(newIndex,iterate_to_add_index.next)
                 iterate_to_add_index.next = new_index
                 break
            count_linked_list +=1  
            iterate_to_add_index = iterate_to_add_index.next
            
    def count(self):
        count_linked_list = 0
        iterate_to_count = self.head
        #Iterating through the linked list and counting the elements inside it
        while iterate_to_count:
            count_linked_list +=1#Add counts everytime you iterate
            iterate_to_count = iterate_to_count.next 
        return count_linked_list #Returns the length

    def delete(self, value):#Remove the given element 
        #If the element the user want to delete is the head     
        if self.head.value == value:
            self.head= self.head.next
            print(f"ELEMENT [{value}] DELETED")
            return
        iterate_to_delete = self.head
        #Iterate until it reaches the certain element that the user wants to delete
        while iterate_to_delete.next:
            if iterate_to_delete.next.value ==  value:
                iterate_to_delete.next = iterate_to_delete.next.next
                print(f"ELEMENT [{value}] DELETED")
                return
            iterate_to_delete = iterate_to_delete.next
        print("THE ELEMENT IS NOT FOUND")
        
    def reverse(self):
        current_element = self.head #Set the current element as the head
        previous_element = None
        while current_element:
            #Set the current element to the next element
            next_element = current_element.next
            #Reversing the list
            current_element.next = previous_element
            previous_element = current_element
            current_element = next_element
        self.head = previous_element #Set the reverse element as the head

    def search(self,userSearch):
        iterate_to_search = self.head
        position_search = 0 #To get the position of what the user wants
        while iterate_to_search:
            #if the element that the user is finding is found
            if iterate_to_search.value == userSearch:  
                print(f"The Element is at the Linked List and position is [{position_search + 1}]")
                return position_search
            #continue to iterate until the element isnt found
            iterate_to_search = iterate_to_search.next
            position_search +=1#Add position everytime
        print("[THE ELEMENT CANNOT BE FOUND]")#Else display this

    def emptyElem(self):#If the user chooses the other option without creating a list
        if not self.head:
            #This will display and bring it back to the main question
            print("[YOU HAVE NO ELEMENT/S]")
            self.main()

    def main(self):
        while True:
            try:#Try and catch mechanism
                linked_list_choice= int(input(""" 
************* L  I  N  K  E  D L  I  S  T ************
*      Programmed by: Kyne Domerei N. Laggui         *
*                    BSCOE 2-1                       *
*                                                    *
*              (1) CREATE A LIST                     *
*              (2) ADD AT BEGINNING                  *
*              (3) ADD AFTER                         *                               
*              (4) DELETE                            *                
*              (5) DISPLAY                           *
*              (6) COUNT                             *
*              (7) REVERSE                           *
*              (8) SEARCH                            *
*              (9) QUIT                              * 
*                                                    *                                          
******************************************************
Select an Option: """))
                if linked_list_choice ==1:
                    print("[CREATE A LIST]")
                    #Ask the user for their input
                    elem_count= int(input("How many nodes you want? "))
                    print(f"Input your {elem_count} digit/s numbers: ")
                    #Create a list by looping depending on the number of nodes that the user wants
                    for elements in range(elem_count):
                        self.createList(int(input("")))
                    self.display()
                elif linked_list_choice ==2:
                    self.emptyElem()
                    print("[ADD AT BEGINNING]")
                    new_head= int(input("Insert the New First Element: "))
                    self.addBeginning(new_head)
                    self.display()
                elif linked_list_choice ==3:
                    self.emptyElem()
                    print("[ADD AFTER]")
                    new_elem = int(input("Insert the Element you wish to add: "))
                    new_index= int(input("Insert the index of the Element: "))
                    self.addAfter(new_index, new_elem)
                    self.display()        
                elif linked_list_choice ==4:
                    self.emptyElem()
                    print("[DELETE]")
                    delete_elem= int(input("Enter the element you wish to delete: "))
                    self.delete(delete_elem)
                    self.display()  
                elif linked_list_choice ==5:
                    self.emptyElem()
                    print("[DISPLAY]")
                    self.display() 
                elif linked_list_choice ==6:
                    self.emptyElem()
                    print("[COUNT]")
                    print(f"Number of Elements: {self.count()}")
                    self.display()
                elif linked_list_choice ==7:
                    self.emptyElem()
                    print("[REVERSE]")
                    self.reverse()
                    self.display()
                elif linked_list_choice ==8:
                    self.emptyElem()
                    print("[SEARCH]")
                    user_search = int(input("Enter the element you wish to find: "))
                    self.search(user_search)
                elif linked_list_choice ==9:
                    print("[QUIT]")
                    quit("Thank you for using my program\nProgrammed by: Kyne Domerei N. Laggui")
                else:
                    print("Choose an option from the category")
            except ValueError:#Display if the value is not a integer 
                print("[ERROR] PLEASE INPUT A VALID INTEGER")
#Driver for the linked list
linkedListDriver = LINKEDLIST()
linkedListDriver.main()
