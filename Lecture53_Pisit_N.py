print("Welcome to SmartVAT")
totalPrice = float(input("? = "))

def vatCal(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

print("Result =", vatCal(totalPrice))