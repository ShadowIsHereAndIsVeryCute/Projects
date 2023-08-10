class Item:
    pay_rate = 0.8 # discount rate
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the recived arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} Is not greater than zero!"


        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)



    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def instanciate_from_csv(self):


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

#Changing the indivudal discount of a instance
itema = Item("Laptop", 1000, 3)
itema.pay_rate = 0.7
itema.apply_discount()
print(itema.price)


print(Item.all)


#print(Item.__dict__) #Class level atributes
#print(item1.__dict__) # Instance level atributes

