def adding_report (report_type):
    total = 0
    items = ""
    
    string = input ('Input an integer to add to the total or "Q" to quit: ')
    while True:
        if string.isdigit ():
            total += int (string)
            if report_type == "A":
                items = items + string + "\n"
        elif string.startswith ("Q"):
            if report_type == "A":
                print ("\nItems\n" + items + "\n" + "\nTotal\n" + str(total))
            elif report_type == "T":
                print ("\nTotal\n" + str(total))
            break
        else:
            print ("Invalid input")
        
        string = input ('Enter an integer or "Q" to quit: ')

print ("This program adds a sequence of integers and produces two types of reports.")
print ("Report A: Prompts for a sequence of integers and outputs the concatenated sequence and total.")
print ("Report B: Prompts for a sequence of integers and output only the total.\n")

report_type = input ("Which report type do you prefer [A, T, or Q to quit]? ")
while report_type != "Q":
    if report_type in "A T":
        adding_report (report_type)
    else:
        print ("ERROR: Try again!\n")
    report_type = input ("\nWhich report type do you prefer [A, T, or Q to quit]? ")
    
print ("Bye!")