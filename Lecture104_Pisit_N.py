class Customer:
    name = ""
    lastName = ""
    age= 0

    def addCart(self):
        print("Added to", self.name, self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Pisit"
customer1.lastName = "Nantachoktevarat"
customer1.addCart()

customer2 = Customer()
customer2.name = "Patchanya"
customer2.lastName = "Nantachoktevarat"
customer2.addCart()

customer3 = Customer()
customer3.name = "Anupap"
customer3.lastName = "Ploydee"
customer3.addCart()

customer4 = Customer()
customer4.name = "Thamonpat"
customer4.lastName = "Nantachokrapeekarn"
customer4.addCart()