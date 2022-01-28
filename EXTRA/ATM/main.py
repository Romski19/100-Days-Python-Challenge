from actions import Actions
balance = 0
to_act = Actions(balance)

should_continue = True

while should_continue:
    print("=== Welcome to Ramosa Group Bank - ATM ===")
    print("=== Please select an option ===")
    print("=== 1. Inquire Balance ===")
    print("=== 2. Deposit         ===")
    print("=== 3. Withdraw        ===")
    chosen = int(input("Selection:"))
    if chosen == 1:
        to_act.check_balance(balance)
    elif chosen == 2:
        balance = to_act.deposit()
    elif chosen == 3:
        balance = to_act.withdraw(balance)
    else:
        print("You have chosen a wrong option")

    result = input("Do you still wanna continue? Y/N: ").lower()
    if result == "n":
        should_continue = False
        print("Goodbye")