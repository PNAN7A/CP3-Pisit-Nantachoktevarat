menuList = []
priceList = []

print("Welcome to iShop".center(24))
print(" Add Order ".center(24, "-"))
print('Enter "Exit" When Finish')

while True:
    menuName = input("Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)

def showBill():
    print(" Bill ".center(24, "-"))
    for number in range(len(menuList)):
        print(menuList[number], ":", priceList[number], "THB")
        result = 0
        for price in priceList:
            result += price
    print("-".center(24, "-"))
    print("Total =", result, "THB")

showBill()