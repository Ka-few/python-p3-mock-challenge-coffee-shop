class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        if hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed once set")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        if hasattr(self, "_name"):
            raise AttributeError("Coffee name cannot be changed after instantiation")
        self._name = value

    @property
    def name(self):
        return self._name
        
    def orders(self):
        # from order import Order
        return [order for order in Order.all if order.coffee is self]

    
    def customers(self):
        # from customer import  Customer
        return list({order.customer for order in self.orders() if isinstance(order.customer, Customer)})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total = sum(order.price for order in orders)
        return total / len(orders)

class Customer:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            if not isinstance(name, str):
                raise ValueError("Name must be a string")
            if not (1 <= len(name) <= 15):
                raise  ValueError("Name must be between 1 and 15 characters")
        self._name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
        
    def orders(self):
        # from order import Order
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        # from coffee import Coffee
        return list({order.coffee for order in self.orders() if isinstance(order.coffee, Coffee)})
    
    def create_order(self, coffee, price):
        # from  order import Order
        return Order(self,coffee,price)

    @classmethod
    def most_aficionado(cls, coffee):
        # from order import Order
        spending = {}
        for order in Order.all:
            if order.coffee is coffee:
                spending[order.customer] = spending.get(order.customer, 0) + order.price
            if not spending:
                return None
            return max(spending, key=spending.get)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price: float):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        # from customer import Customer
        if not isinstance(value, Customer):
            raise  ValueError("customer must be a Customer instance")
        self._customer = value
    
    @property
    def coffee(self):
        return self._coffee


    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("coffee must be a Coffee instance")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Price must be a float")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0 inclusive")
        if hasattr(self, "_price"):
            raise AttributeError("Price cannot be changed after the order is created")
        self._price = value

c1 = Customer("Kevin")
c2 = Customer("Mercy")
coffee1 = Coffee("Latte")



c1.create_order(coffee1, 4.0)
c1.create_order(coffee1, 5.0)

c2.create_order(coffee1, 6.0)


print(Customer.most_aficionado(coffee1))