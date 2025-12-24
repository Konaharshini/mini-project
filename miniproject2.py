correct_pin = "1234"
attempts = 3
count = 0

while count < attempts:
    pin = input("Enter your ATM PIN: ")
    
    if pin == correct_pin:
        print("PIN verified successfully. Access granted.")
        break
    else:
        count += 1
        remaining = attempts - count
        print("Incorrect PIN.")
        
        if remaining > 0:
            print(f"Attempts left: {remaining}")
        else:
            print("Card blocked. Too many incorrect attempts.")
