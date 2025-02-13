accounts = {
    1001: [1000, 2345, "tharunika@gmail.com", "user1"],
    1002: [2000, 7416, "tharunika1234@gmail.com", "user2"],
    1003: [10000, None, "tharunika1@gmail.com", "user3"]
}
print("Welcome to the ATM System")

while True:
    print("\n*******************************")
    print("Choose your Option: ")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. PIN Generation")
    print("4. Mini Statement")
    print("5. Balance Inquiry")  
    print("6. Change PIN")
    print("7. Exit")
    x = int(input("Enter Your Option: "))
    print("********************************")

    if x == 1:  # Withdraw
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            if accounts[acc][1] is None:
                print(f"Dear {accounts[acc][3]}, PIN Not Generated!")
            else:
                while True:
                    pin = input("Enter Your 4-Digit PIN: ")
                    if pin.isdigit() and len(pin) == 4:
                        pin = int(pin)
                        break
                    else:
                        print("Invalid PIN! Enter exactly 4 digits.")

                if accounts[acc][1] == pin:
                    amt = int(input("Enter Amount: "))
                    if accounts[acc][0] >= amt:
                        accounts[acc][0] -= amt
                        print("Amount Withdrawn Successfully!")
                    else:
                        print("Insufficient Balance")
                else:
                    print("Invalid PIN!")
        print("********************************")

    elif x == 2:  # Deposit
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            amt = int(input("Enter Amount to Deposit: "))
            accounts[acc][0] += amt
            print("Deposit Successful!")
        print("********************************")

    elif x == 3:  # PIN Generation
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            if accounts[acc][1] is not None:
                print("PIN Already Generated!")
            else:
                while True:
                    pin = input("Enter a 4-Digit PIN: ")
                    if pin.isdigit() and len(pin) == 4:
                        accounts[acc][1] = int(pin)
                        print("PIN Generated Successfully!")
                        break
                    else:
                        print("Invalid PIN! Enter exactly 4 digits.")
        print("********************************")

    elif x == 4:  # Mini Statement
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            while True:
                pin = input("Enter Your 4-Digit PIN: ")
                if pin.isdigit() and len(pin) == 4:
                    pin = int(pin)
                    break
                else:
                    print("Invalid PIN! Enter exactly 4 digits.")

            if accounts[acc][1] == pin:
                print(f"\nMini Statement for {accounts[acc][3]}")
                print(f"Email: {accounts[acc][2]}")
                print(f"Balance: ₹{accounts[acc][0]}")
            else:
                print("Invalid PIN!")
        print("********************************")

    elif x == 5:  # Balance Inquiry
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            while True:
                pin = input("Enter Your 4-Digit PIN: ")
                if pin.isdigit() and len(pin) == 4:
                    pin = int(pin)
                    break
                else:
                    print("Invalid PIN! Enter exactly 4 digits.")

            if accounts[acc][1] == pin:
                print(f"Your Current Balance: ₹{accounts[acc][0]}")
            else:
                print("Invalid PIN!")
        print("********************************")

    elif x == 6:  # Change PIN
        acc = int(input("Enter Your Account Number: "))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            if accounts[acc][1] is None:
                print(f"Dear {accounts[acc][3]}, PIN Not Generated!")
            else:
                while True:
                    old_pin = input("Enter Your Current 4-Digit PIN: ")
                    if old_pin.isdigit() and len(old_pin) == 4:
                        old_pin = int(old_pin)
                        break
                    else:
                        print("Invalid PIN! Enter exactly 4 digits.")

                if accounts[acc][1] == old_pin:
                    while True:
                        new_pin = input("Enter Your New 4-Digit PIN: ")
                        if new_pin.isdigit() and len(new_pin) == 4:
                            new_pin = int(new_pin)
                            if new_pin == old_pin:
                                print("New PIN cannot be the same as the old PIN!")
                            else:
                                accounts[acc][1] = new_pin
                                print("PIN Updated Successfully!")
                                break
                        else:
                            print("Invalid PIN! Enter exactly 4 digits.")
                else:
                    print("Incorrect Old PIN!")
        print("********************************")

    elif x == 7:  # Exit
        print("*****************************")
        print("Thank You for Using Our ATM!")
        print("Visit Again!")
        print("*****************************")
        break

    else:
        print("Invalid Option! Please Choose Again.")
