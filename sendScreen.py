#send screen when user chooses to send money to another person
#with account number, amount to send, return and confirm

#importinng the balance from bankAccount.py
from bankAccount import balance

print ("Send Money \n")
while True:
    accnum = input("Enter reciepient account number: ")
    if accnum.isdigit() and len(accnum) == 10:
        break
    else:
        print("Invalid account number. It must be EXACTLY 10 digits.")
    print ("Account number must be EXACTLY 10 digits")  
sendamount = float(input("Enter the amount to send: "))
if sendamount < balance:
    print("Insufficient funds!")
else:
    balance -= sendamount
    print(f"Sending {sendamount} to account number {accnum}...\n")
    print(f"Withdrawal successful! New balance: {balance}")