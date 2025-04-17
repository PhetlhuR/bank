#checking if pushed into github
## Bank account program

balance = float(input("Enter your initial balance: "))

while True:
    print("\n\nWelcome to your bank ®!")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Send Money")
    print("5. Exit")

    try:
        option = int(input("Select an option (1-5): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match option:
        case 1:
            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw > balance:
                print("Insufficient funds!")
            else:
                balance -= withdraw
                print(f"Withdrawal successful! New balance: {balance}")

        case 2:
            deposit = float(input("Enter amount to deposit: "))
            balance += deposit
            print(f"Deposit successful! New balance: {balance}")

        case 3:
            print(f"Your current balance is: {balance}")

        case 4:
            import sendScreen 
            break
        case 5:
            print("Thank you for using the bank account program!")
            import landingpage
            break

        case _:
            print("Invalid option. Please select from 1 to 5.")