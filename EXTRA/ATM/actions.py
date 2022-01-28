CPY_NAME = "=== Welcome to Ramosa Group Bank - ATM ==="


class Actions:

    def __init__(self, balance):
        self.balance = balance

    def check_balance(self, balance):
        print(f"You're outstanding balance is: {balance}")

    def deposit(self):
        print(CPY_NAME)
        print("How much do you want to deposit?")
        deposited = int(input("Enter Amount: "))
        new_balance = self.balance + deposited
        print(f"You're outstanding balance is: {new_balance}")
        return new_balance

    def withdraw(self, balance):
        print(CPY_NAME)
        print("How much do you want to withdraw?")
        withdrawn = int(input("Enter Amount: "))
        if withdrawn > balance:
            print("The amount entered is greater than outstanding balance")
            return balance
        elif withdrawn < 0:
            print("Invalid withdrawal amount!")
            return balance
        else:
            new_balance = balance - withdrawn
            print(f"You're outstanding balance is: {new_balance}")
            return new_balance


