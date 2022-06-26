# Sprint Week 1 Python Program
# Authors: Tyler Power & Colby Ash
# Due: 06-26-22


# Functions for menu
def CalcEmployTc():
    while True:
        import math
        from datetime import datetime

        # Constant Values
        Tax = 0.15
        DayRate = 85.00
        Mileamountperkilo = 0.17
        Mileamountperrent = 65.00
        holidaybonus = 50.00
        # Input Values
        EmployeeNum = input("Enter Employee number: ")
        Employeefirstname = input("Enter Employee First name: ")
        str.capitalize(Employeefirstname)
        Employeelastname = input("Enter Employee Last name: ")
        str.capitalize(Employeelastname)
        locationtrip = input("Enter location of the trip: ")
        startdate = input("Enter start date of the trip: ")
        datetime_start = startdate
        datetime.strptime(datetime_start, '%d-%m')
        enddate = input("Enter end date of the trip: ")
        datetime_end = enddate
        datetime.strptime(datetime_end, '%d-%m')
        Numofdays = int(input("Enter the number of days the trip lasted: "))
        cartype = input("Enter if the car was owned (O) or rented (R): ")
        if cartype == "O":
            totalkilo = int(input("Enter total number of kilometers traveled: "))
        elif cartype == "R":
            totalkilo = 0
            Kilobonus = 0
        claimtype = input("Enter the claim type, standard (S) and executive (E): ")

        # If statements
        if len(EmployeeNum) >= 6:
            print("Error Employee Number is greater than 5 characters")

        if Numofdays >= 7:
            print("Number of days can not be greater than 7")

        if Numofdays >= 3:
            Bonus = 100

        if cartype == "O":
            Mileageamount = totalkilo * Mileamountperkilo
        else:
            Mileageamount = Mileamountperrent * Numofdays

        if totalkilo >= 1000:
            Kilobonus = totalkilo * 0.04

        if totalkilo >= 2000:
            print("Total kilometers cannot be greater than 2000.")

        if claimtype == "E":
            claimtypebonus = Bonus + 45 + Kilobonus
        else:
            claimtypebonus = Bonus + Kilobonus

        if datetime_start <= "12-15":
            HolidayBonus = holidaybonus * 0

        if datetime_start >= "12-15":
            HolidayBonus = holidaybonus * Numofdays

        if datetime_start >= "12-22":
            HolidayBonus = holidaybonus * 0

            # Calculations
        ClaimBonus = Bonus + Kilobonus + claimtypebonus
        Perdiemamount = Numofdays * DayRate
        Totalbonus = Bonus + HolidayBonus + ClaimBonus
        Claimamount = Perdiemamount + Mileageamount + Totalbonus
        HST = Perdiemamount * Tax
        Totalclaim = Claimamount + HST

        # Print all necessary values

        print()
        print(f"Employee Number:{EmployeeNum}, Name: {Employeefirstname},{Employeelastname}")
        print(f"Trip location: {locationtrip}")
        print(f"Start date of  trip: {startdate}", f"End date of trip: {enddate}")
        print(f"Num of days spent on trip: {Numofdays}")
        print(f"If car was owned or rented: {cartype}", f"Claim  type: {claimtype}")
        print(f"Bonus: {f'${claimtypebonus:,.2f}':>}")
        print(f"Total bonus: {f'${Totalbonus:,.2f}':>}")
        print(f"Total mileage: {f'{Mileageamount:.2f}'}")
        print(f"Per diem amount: {f'${Perdiemamount:,.2f}':>}")
        print(f"Claim amount: {f'${Claimamount:,.2f}':>}")
        print(f"HST: {f'${HST:,.2f}':>}")
        print(f"Total claim amount: {f'${Totalclaim:,.2f}':>}")

        check = input("Press Y to submit another claim: ")

        if check.upper() == "Y":
            continue
        else:
            break


def CalcFunIntQ():
    # Function for FizzBuzz Problem
    def fizz_buzz():
        for Number in range(1, 101):
            if (Number % 5 == 0) and (Number % 8 == 0):
                print("FizzBuzz")
            elif Number % 5 == 0:
                print("Fizz")
            elif Number % 8 == 0:
                print("Buzz")
            else:
                print(Number)

    print(fizz_buzz())

# End program validation
    Continue = input("Press Enter to continue.")


def StringsDates():
    import string

    while True:
        from datetime import datetime

        # Constants

        Currentdate = datetime.today()

        # Input variables

        Firstname = input("Enter first name: ")
        Lastname = input("Enter last name: ")
        Phonenumber = int(input("Enter phone number: "))
        datetime_start = input("Enter start date (DD-MM-YYYY): ")
        datetime_birth = input("Enter Birthday (DD-MM-YYYY): ")

        # Calculations

        DtS = datetime.strptime(datetime_start, '%d-%m-%Y')
        DtB = datetime.strptime(datetime_birth, '%d-%m-%Y')
        Workamount = Currentdate - DtS
        Tillbirth = Currentdate - DtB

        # Print all necessary values

        print()
        print(f"The current date and time is: {Currentdate}")
        print(f"Your phone number is: {Phonenumber}")
        print(f"Your name is {Firstname} {Lastname}.")
        print(f"You have worked here for: {Workamount}")
        print(f"You are {Tillbirth} old.")

        check = input("Press any letter to continue: ")
        if check == string.ascii_letters:
            continue
        else:
            break


def GraphMonClaimTot():
    import datetime
    import math
    import matplotlib.pyplot as plt

    # Graph a line based on user input for x and y
    x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    y = []

    # for loop for input sales per Month
    for Months in range(1, 13):
        MonthSales = input("Enter the Month sales for " + x[Months - 1] + ": ")
        y.append(MonthSales)

    plt.title("Monthly Claim Totals")
    plt.plot(x, y, color='darkred')

    plt.xlabel("Months of the Year")
    plt.ylabel("Monthly Sales($)")

    plt.grid(True)

    plt.show()

# End program validation
    Continue = input("Press Enter to continue: ")

while True:

    # Main program starts here
    print(" NL Chocolate Company")
    print(" Travel Claims Processing System")
    print()
    print(" 1. Enter an Employee Travel Claim.")
    print(" 2. Fun Interview Question.")
    print(" 3. Cool Stuff with Strings and Dates.")
    print(" 4. Graph Monthly Claim Totals.")
    print(" 5. Quit Program.")
    print()

    while True:     # Loop for choice input (1-5) validation
        try:
            Choice = int(input("Enter choice (1-5): "))
        except:
            print("Error - Choice Must be between (1-5) - Please re-enter.")
        else:
            if Choice < 1 or Choice > 5:
                print("Error - Choice Must be between (1-5) - Please re-enter.")
            else:
                break

    if Choice == 1:
        CalcEmployTc()
    elif Choice == 2:
        CalcFunIntQ()
    elif Choice == 3:
        StringsDates()
    elif Choice == 4:
        GraphMonClaimTot()
    else:
        break


