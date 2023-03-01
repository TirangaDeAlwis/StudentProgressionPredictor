# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20210411 
# Date: 6/12/2021

progressCount = 0
retrieverCount = 0
trailerCount = 0
excludeCount = 0
totalCount = 0
ValumeOfCredits = [0, 20, 40, 60, 80, 100, 120]

resultList = []


def startStudent():
    isQuit = False;
    hasValidPassCr = False;
    hasValidDeferCr = False;
    hasValidFailCr = False;

    while not isQuit:
        try:
            if not hasValidPassCr:
                passCr = int(input("Enter your total PASS credits: "))
                if passCr in ValumeOfCredits:
                    hasValidPassCr = True
                else:
                    hasValidPassCr = False
                    print("Out of range\n")
                    continue
            if not hasValidDeferCr:
                deferCr = int(input("Enter your total DEFER credits: "))
                if deferCr in ValumeOfCredits:
                    hasValidDeferCr = True
                else:
                    hasValidDeferCr = False
                    print("Out of range\n")
                    continue
            if not hasValidFailCr:
                failCr = int(input("Enter your total FAIL credits: "))
                if failCr in ValumeOfCredits:
                    hasValidFailCr = True
                else:
                    hasValidFailCr = False
                    print("Out of range\n")
                    continue

            if (passCr + deferCr + failCr) == 120:
                progressionOutcome(passCr, deferCr, failCr)
                isQuit = True
            else:
                print("Total incorrect\n")
                exit()

        except ValueError:
            print("Integer required\n")
            continue

def progressionOutcome(passCr, deferCr, failCr):
    global progressCount, retrieverCount, trailerCount, excludeCount, totalCount

    if passCr == 120:
        progressCount += 1
        print("Progress")
    elif passCr == 100:
        trailerCount += 1
        print("Progress (module trailer)")
    elif failCr > (passCr + deferCr):
        excludeCount += 1
        print("Exclude")
    else:
        retrieverCount += 1
        print("Module retriever")
    totalCount += 1

startStudent()

