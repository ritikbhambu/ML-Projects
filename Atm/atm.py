balance = 1000.0
pin = "1234"

user_pin = input("Enter your 4-digit PIN: ")

if user_pin == pin:
    print("Login successful!\n")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"Your balance is: ${balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposited ${amount}. New balance: ${balance}")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrew ${amount}. New balance: ${balance}")
            else:
                print("Not enough balance!")

        elif choice == "4":
            print("Thank you...")
            break

        else:
            print("Invalid option.")

else:
    print("Wrong PIN. Access denied.")
