print("WELCOME TO YOUR BANK ®")

# Get and validate account number
while True:
    accnum = input("Enter your 10-digit account number: ")
    if accnum.isdigit() and len(accnum) == 10:
        break
    else:
        print("Invalid account number. It must be exactly 10 digits.")

# Get and validate PIN
while True:
    pin = input("Enter your 4-digit PIN: ")
    if pin.isdigit() and len(pin) == 4:
        import bankAccount
        break
    else:
        print("Invalid PIN. It must be exactly 4 digits.")

# Optionally convert to int if needed
accnum = int(accnum)
pin = int(pin)