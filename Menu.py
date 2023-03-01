# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20210411 
# Date: 6/12/2021

from Part_01 import *
from Part_02 import *
from Part_03 import *
from Part_04 import *



def main():
    while True:    
        
        print("-------------------------------------")
        print("|                                   |")
        print("|   ~~  progression predictor  ~~   |")
        print("|                                   |")
        print("|     Press [1] to access PART 01   |")
        print("|                                   |")
        print("|     Press [2] to access PART 02   |")
        print("|                                   |")
        print("|     Press [3] to access PART 03   |")
        print("|                                   |")
        print("|     Press [4] to access PART 04   |")
        print("|                                   |")
        print("-------------------------------------")


        user_input = int(input("Enter the PART number: " ))
        
        if user_input == 1:        
            startQ1() #Starting Horizontal Histogram
            
        elif user_input == 2:
            startQ2() #Starting Vertical Histogram
            
        elif user_input == 3:
            startQ3() #Starting List Extension Module
           
        elif user_input == 4:
            startQ4() #Starting Text File Extension Module
              
        else:
            print("Given PART is not available")
           
            
    
main()
    
