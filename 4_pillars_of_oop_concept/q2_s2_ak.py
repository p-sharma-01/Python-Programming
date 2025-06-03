d={}
class Item:
    def __init__(self, name, price):
        self.name=name
        self.price=price

class ShoppingCart():
    def add_item(self,name,price):
        w={}
        w[name]=price
        d.update(w)
        print("Item added succesfully")
    def remove_item(self, name):
        d.pop(name)
        print("Item deleted successfully")

    def total_price(self):
        e=sum([value for key,value in d.items()])
        print("Total price: ",e)

# Example usage:
cart = ShoppingCart()
cart.add_item('meow',47389)
cart.add_item('billi',56473)

cart.total_price()
cart.remove_item('meow')
cart.total_price()
# Read input and perform operations