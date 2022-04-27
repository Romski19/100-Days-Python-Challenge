balance = 0


def company_name():
    print("=== Welcome to Ramosa Group Bank - ATM ===")


def deposit():
    company_name()
    print("How much do you want to deposit?")
    deposited = int(input("Enter Amount: "))
    new_balance = balance + deposited
    print(f"You're outstanding balance is: {new_balance}")
    return new_balance


def withdraw():
    company_name()
    print("How much do you want to withdraw?")
    withdrawed = int(input("Enter Amount: "))
    if withdrawed > balance:
        print("The amount entered is greater than outstanding balance")
        return balance
    elif withdrawed < 0:
        print("Invalid withdrawal amount!")
        return balance
    else:
        new_balance = balance - withdrawed
        print(f"You're outstanding balance is: {new_balance}")
        return new_balance


def check_balance():
    print(f"You're outstanding balance is: {balance}")


should_continue = True

while should_continue:
    company_name()
    print("=== Please select an option ===")
    print("=== 1. Inquire Balance ===")
    print("=== 2. Deposit         ===")
    print("=== 3. Withdraw        ===")
    chosen = int(input("Selection:"))
    if chosen == 1:
        check_balance()
    elif chosen == 2:
        balance = deposit()
    elif chosen == 3:
        balance = withdraw()
    else:
        print("You have chosen a wrong option")

    result = input("Do you still wanna continue? Y/N: ").lower()
    if result == "n":
        should_continue = False
        print("Goodbye")
