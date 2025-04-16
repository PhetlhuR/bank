#from send screen importing send amount, account number, and balance

from sendScreen import sendamount, accnum, balance

print("Confirm Send Money \n\n")
would_you_like_to_send = input(f"Would you like to send {sendamount} to account number {accnum}? (yes/no): ").strip().lowe
if True:
    print(f"Sending {sendamount} to account number {accnum}...\n")
    print(f"Withdrawal successful! New balance: {balance}")
print(f"Account number: {accnum}")  