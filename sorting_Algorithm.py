class SORTINGALGORITHM:
    """Selection Sort- It finds the lowest element in each index and swaps its position."""
    def SELECTIONSORT(self):
        #To find the first index of the List
        for selection_sort in range(len(mainList) - 1):
            minimum_index = selection_sort
            if sortElements ==1 or sortElements ==3:#If the user selects Ascending or Alphabetical
                #To check the right element of the index 
                for check_selection_sort in range(selection_sort + 1, len(mainList)):
                    if mainList[check_selection_sort] < mainList[minimum_index]:
                        minimum_index = check_selection_sort
            elif sortElements ==2:#If the user selects Descending 
                for check_selection_sort in range(selection_sort + 1, len(mainList)):
                    if mainList[check_selection_sort] > mainList[minimum_index]:
                        minimum_index = check_selection_sort
            # Replace the first element of the unsorted list with the minimum element
            mainList[selection_sort], mainList[minimum_index] = mainList[minimum_index],mainList[selection_sort]
            # To display the steps or passess
            print(f'Pass {selection_sort+1}: {mainList}')

    """Bubble Sort- If the element from the left index is greater than the element from the right index, swap it."""
    def BUBBLESORT(self):
        # Iterate through the List
        for bubble_sort in range(len(mainList)):
            if sortElements ==1 or sortElements ==3:
                for checkBS in range(len(mainList)-1):#If the user selects Ascending or Alphabetical
                    #If the left element is greather than the right element it swaps its position
                    if mainList[checkBS] > mainList[checkBS+1]:
                        mainList[checkBS], mainList[checkBS+1] = mainList[checkBS+1], mainList[checkBS]
            elif sortElements ==2:#If the user selects Descending 
                for checkBS in range(len(mainList)-1):
                    #If the left element is less than the right element it swaps its position
                    if mainList[checkBS] < mainList[checkBS+1]:
                        mainList[checkBS], mainList[checkBS+1] = mainList[checkBS+1], mainList[checkBS]
            # To display the steps or passess
            print(f'Pass {bubble_sort+1}: {mainList}')

    """Similar to playing cards, insertion sort works by replacing the index instead of the position. 
    Unlike selection sort, this automatically places the appropriate element in its proper location."""
    def INSERTIONSORT(self):
        #Iterate through the list, starting from the second element
        for insertion_sort in range(1, len(mainList)):
            #Set a variable to contain the current element.
            current_insertion_sort = mainList[insertion_sort]
            # Set the preceding element's index to the present element's index.
            new_insertion_sort = insertion_sort 
            if sortElements ==1 or sortElements ==3:#If the user selects Ascending or Alphabetical
                while new_insertion_sort > 0 and mainList[new_insertion_sort-1] > current_insertion_sort:
                    # Move the previous element to the current index
                    mainList[new_insertion_sort] = mainList[new_insertion_sort-1]
                    new_insertion_sort -= 1#Reduce the Index
                    mainList[new_insertion_sort] = current_insertion_sort#Set the current index to the stored value
            elif sortElements ==2:#If the user selects Descending 
                while new_insertion_sort > 0 and mainList[new_insertion_sort-1] < current_insertion_sort:
                    mainList[new_insertion_sort] = mainList[new_insertion_sort-1]
                    new_insertion_sort -= 1
                    mainList[new_insertion_sort] = current_insertion_sort
            # To display the steps or passess
            print(f'Pass {insertion_sort +1}: {mainList}')

    """Merge Sort- the idea  of divide and conquer. Divides the element into half until 
    it cannot be further divided"""
    def MERGESORT(self, mainList):
        #If the number of element stored in the list is less than or equal to one, display the list
        if len(mainList) <= 1:
            return mainList
        #Find the middle index of the mainList
        middleMergeSort = len(mainList) // 2
        #Set the elements from the beginning to the center of the list in the left half
        leftMergeSort = mainList[:middleMergeSort]
        #Set the elements from the beginning to the center of the list in the right half
        rightMergeSort = mainList[middleMergeSort:]
        #Sort the left half of the list repeatedly until it cannot be divided
        self.MERGESORT(leftMergeSort)
        #Sort the right half of the list repeatedly until it cannot be divided
        self.MERGESORT(rightMergeSort)
        #Set the indices to zero
        msLeft = msRight = msList = 0
        
        #This while loop is to find the largest/lowest element depending in the sorting method to their respective positions
        while msLeft < len( leftMergeSort ) and msRight < len(rightMergeSort):
            if sortElements ==1 or sortElements ==3:#If the user selects Ascending or Alphabetical
                #If the current left element is less than the current right element
                if leftMergeSort[msLeft] < rightMergeSort[msRight]:
                    #Increase the left index and set the current main list index to the left element.
                    mainList[msList] = leftMergeSort[msLeft]
                    msLeft += 1
                    
                else:
                    """if the left element is greater than or equal to the right element. 
                    It will be set as the current main list element, and the right index increases."""
                    mainList[msList] = rightMergeSort[msRight]
                    msRight += 1
            elif sortElements ==2:#If the user selects Descending
                #Vice versa of the first if statement
                if leftMergeSort[msLeft] > rightMergeSort[msRight]:
                    mainList[msList] = leftMergeSort[msLeft]
                    msLeft += 1
                else:
                    mainList[msList] = rightMergeSort[msRight]
                    msRight += 1
            msList += 1

        #To add the remaining elements of the left side to their respective indices
        while msLeft < len(leftMergeSort):
            mainList[msList] = leftMergeSort[msLeft]
            msLeft += 1
            msList += 1
        #To add the remaining elements of the right side to their respective indices
        while msRight < len(rightMergeSort):
            mainList[msList] = rightMergeSort[msRight]
            msRight += 1
            msList += 1
        # To display the steps or passess
        print(f"Pass {msLeft}: {mainList}")
    
    #This function is for the main function of the program.
    def USERMENU(self):
        global mainList, sortElements
        try:#Try and catch mechanism
            while True:
                UserAlgoChoice = int(input
            (""" 
*************SORTING ALGORITHM APPLICATION************
*      Programmed by: Kyne Domerei N. Laggui         *
*                    BSCOE 2-1                       *
*                                                    *
*     <<< M   A   I   N    M   E   N   U   >>>       *
*                                                    *
*              (1) SELECTION SORTING                 *                               
*              (2) BUBBLE SORTING                    *                
*              (3) INSERTION SORTING                 *
*              (4) MERGE SORTING                     *
*                                                    *
*                                                    *                                         
******************************************************
Select an Option: """))
                mainList = []#Main list to store the elements
                #A list of options that the user can utilize to appropriately find the desired outcome
                numElements = int(input("How many elements are there on your list: "))
                typeElements =int(input("[1] INTEGERS \n[2] LETTERS(UPPER-CASE ONLY) \nWhat type of elements: "))
                sortElements= int(input("[1] ASCENDING \n[2] DESCENDING \n[3] ALPHABETICALLY \nWhat sorting mode: "))
                print(f"Input your {numElements} digit/s number/letters:")
                #This if and else if statement is to differentiate Integers and Letters
                if typeElements ==1:#For the Integers 
                    for k in range (numElements):
                        mainList.append(int(input("")))
                elif typeElements ==2:#For the Letters
                    #As given in the instruction the Letters must be uppercase
                    for k in range (numElements):
                        LetterInput = input("")
                        #If the letters are uppercase it will append it to the list
                        if LetterInput.isupper() == True:
                            mainList.append(LetterInput)
                        else:
                            print("THE LETTER MUST BE CAPITALIZED")#Else this will display
                            #Then it will ask the user if they want tor restart or terminate the program
                            runAgain1 = input("Do you want to try again [y/n]? ").lower()
                            if runAgain1 == "y":
                                self.USERMENU()
                                break
                            elif runAgain1 == "n":
                                quit("Thank you for using my program\n-Kyne Domerei N. Laggui")
                            
                print(f"List: {mainList}")
                if UserAlgoChoice == 1:#If the user selects Selection Sort
                    self.SELECTIONSORT()
                elif UserAlgoChoice == 2:#If the user selects Bubble Sort
                    self.BUBBLESORT()
                elif UserAlgoChoice == 3:#If the user selects Insertion Sort
                    self.INSERTIONSORT()
                elif UserAlgoChoice == 4:#If the user selects Merge Sort
                    self.MERGESORT(mainList)
                
                print("Final Sorted Elements:", mainList)#To display the final sorter element
                #It will ask the user if they want to use to program again
                runAgain = input("Do you want to try again [y/n]? ").lower()
                if runAgain == "n":#The software will end if the user decides not to execute it 
                    quit("Thank you for using my program \n-Kyne Domerei N. Laggui")
        except ValueError:
            print("Please input a valid number")#If the user inputs a non-integer it will display this message

#Driver of the Sorting Algorithm Program
SR_AlgoDriver = SORTINGALGORITHM()
SR_AlgoDriver.USERMENU()




