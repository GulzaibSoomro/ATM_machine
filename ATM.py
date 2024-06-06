import time

def atm_system():
    print("Please enter your card")
    time.sleep(5)

    password = 1234
    balance = 50000

    try:
        pin = int(input("Enter your ATM pin: "))
    except ValueError:
        print("Invalid input. Please enter a numeric pin.")
        return

    if pin == password:
        while True:
            print("""
            1 == Balance
            2 == Withdraw amount
            3 == Deposit amount
            4 == Exit
            """)
            
            try:
                option = int(input("Please enter your choice: "))
            except ValueError:
                print("Invalid option. Please enter a number between 1 and 4.")
                continue

            if option == 1:
                print(f"Your balance is: ${balance}")
            elif option == 2:
                try:
                    withdraw = int(input("Enter the amount you want to withdraw: "))
                    if withdraw > balance:
                        print("Insufficient funds.")
                    else:
                        balance -= withdraw
                        print(f"You withdrew ${withdraw}. Your new balance is: ${balance}")
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
            elif option == 3:
                try:
                    deposit = int(input("Enter the amount you want to deposit: "))
                    balance += deposit
                    print(f"You deposited ${deposit}. Your new balance is: ${balance}")
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
            elif option == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please enter a number between 1 and 4.")
    else:
        print("Wrong pin. Exiting.")

if __name__ == "__main__":
    atm_system()
