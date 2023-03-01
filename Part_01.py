# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20210411 
# Date: 6/12/2021

#Declare Variables
progressCount = 0
retrieverCount = 0
trailerCount = 0
excludeCount = 0
totalCount = 0
ValumeOfCredits = [0, 20, 40, 60, 80, 100, 120]     #for to check the user input range

def startQ1():
    
    isQuit = False;
    hasValidPassCr = False;
    hasValidDeferCr = False;
    hasValidFailCr = False;
    
    while not isQuit:
        isRestart = ""
        invalidQuit = False
    
        try:
            if not hasValidPassCr:
                passCr = int(input("Enter your total PASS credits: "))      # take user input and assign it to a variable
                if passCr in ValumeOfCredits:
                    hasValidPassCr = True
                else:
                    hasValidPassCr = False
                    print("Out of range\n")
                    continue
            if not hasValidDeferCr:
                deferCr = int(input("Enter your total DEFER credits: "))    # take user input and assign it to a variable
                if deferCr in ValumeOfCredits:
                    hasValidDeferCr = True
                else:
                    hasValidDeferCr = False
                    print("Out of range\n")
                    continue
            if not hasValidFailCr:
                failCr = int(input("Enter your total FAIL credits: "))      # take user input and assign it to a variable
                if failCr in ValumeOfCredits:
                    hasValidFailCr = True
                else:
                    hasValidFailCr = False
                    print("Out of range\n")
                    continue
                    
            if (passCr + deferCr + failCr) == 120:
                progressionOutcome(passCr, deferCr, failCr)
            else:
                print("Total incorrect\n")

            #Ask user to Rerun      
            while not invalidQuit:
                isRestart = input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ").lower()

                if isRestart != "y" and isRestart != "q":                    
                    print("Invalid input. Please try again!")
                else:
                    invalidQuit = True
                    if isRestart == "y":
                        hasValidPassCr = False;
                        hasValidDeferCr = False;
                        hasValidFailCr = False;
                        isQuit = False
                    elif isRestart == "q":
                        isQuit = True
                
        except ValueError:
            print("Integer required\n")
            continue

    histogramGenerator()    #To call the Histogram function
    exit()

def progressionOutcome(passCr, deferCr, failCr):
    global progressCount, retrieverCount, trailerCount, excludeCount, totalCount
    
    if passCr == 120:
        progressCount += 1  # increment variable value by 1
        print("Progress") 
    elif passCr == 100:
        trailerCount += 1   # increment variable value by 1
        print("Progress (module trailer)") 
    elif failCr > (passCr + deferCr):
        excludeCount += 1   # increment variable value by 1
        print("Exclude") 
    else:
        retrieverCount += 1  # increment variable value by 1
        print("Module retriever") 
    totalCount += 1

def histogramGenerator():   # Histogram Generator Function
    print('-' * 70) 
    print('Horizontal Histogram')
    print(f"progress {progressCount}\t: {'*' * progressCount}")
    print(f"Trailer {trailerCount}\t: {'*' * trailerCount}")
    print(f"Retriever {retrieverCount}\t: {'*' * retrieverCount}")
    print(f"Excluded {excludeCount}\t: {'*' * excludeCount}\n")
    print(f'{totalCount} outcomes in total.')
    print('-' * 70)


