class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Th Payment of Amount{amount} is done through Credit Card.")

class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"Th Payment of Amount{amount} is done through Debit Card.")

class Cash(PaymentMethod):
    def pay(self, amount):
        print(f"Th Payment of Amount{amount} is done through Cash.")

# Example usage:
amount = int(input())
p=[CreditCard(),DebitCard(),Cash()]
for i in p:
    i.pay(amount)

# Call the pay method for each payment type




#2
class Item:
    def __init__(self, name, price):
        pass

class ShoppingCart:
    def __init__(self):
        pass

    def add_item(self, name, price):
        pass

    def remove_item(self, name):
        pass

    def total_price(self):
        pass

# Example usage:
cart = ShoppingCart()
# Read input and perform operations