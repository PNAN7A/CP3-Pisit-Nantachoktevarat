print("Welcome to Hello Shop")
print("------- Login -------")
usr = input("Username : ")
pwd = input("Password : ")
print("---------------------")
if usr == "Admin" and pwd == "777":
    print("Choose Your Product?")
    print("(1) MacBook 11 Inch : Price 50,000 Baht")
    print("(2) iPad Pro 9.7 Inch : Price 30,000 Baht")
    print("(3) iPhone 6s : Price 20,000 Baht")
    print("---------------------")
    num = int(input("Number : "))
    amt = int(input("Amount : "))
    mbk = 50000
    ipd = 30000
    iph = 20000
    if num == 1:
        tot = mbk * amt
        print("---------------------")
        print("MacBook 11 Inch : Amount", amt)
        print("Total Price =", tot, "Baht")
        print("---------------------")
        print("***** Thank You *****")
    elif num == 2:
        tot = ipd * amt
        print("---------------------")
        print("iPad Pro 9.7 Inch : Amount", amt)
        print("Total Price =", tot, "Baht")
        print("---------------------")
        print("***** Thank You *****")
    elif num == 3:
        tot = iph * amt
        print("---------------------")
        print("iPhone 6s : Amount", amt)
        print("Total Price =", tot, "Baht")
        print("---------------------")
        print("***** Thank You *****")
else:
    print("Wrong!")