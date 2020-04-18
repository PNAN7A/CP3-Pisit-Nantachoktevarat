def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "777":
        return showMenu()
    else:
        print("Try Again!")
        return login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelect = int(input("Choose : "))
    if userSelect == 1:
        return vatCal()
    elif userSelect == 2:
        return priceCal()
def vatCal():
    price = int(input("Price (THB) : "))
    vat = 7
    result = price + (price * vat / 100)
    return result
def priceCal():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return price1 + price2
print(login())