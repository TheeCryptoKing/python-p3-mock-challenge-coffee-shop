class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

        coffee.orders(self)
        coffee.customers(customer)

        customer.orders(self)
        customer.coffees(coffee)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        from classes.customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception
        
    @property
    def order(self):
        return self._order
    
    @order.setter
    def order(self, order):
        from classes.order import Order
        if isinstance(order, Order):
            self._order = order
        else:
            raise Exception
        

    # Micheals solution 
    # @property
    # def price(self):
    #     return self._price

    # @price.setter
    # def price(self, price):
    #     if not (isinstance(price, float) or (1 <= price <= 10)):
    #         raise Exception("Price must be a number between 1 and 10.")
    #     self._price = price

    # @property
    # def customer(self):
    #     return self._customer

    # @customer.setter
    # def customer(self, customer):
    #     from classes.customer import Customer

    #     if not (isinstance(customer, Customer)):
    #         raise Exception("Customer must be an instance of Customer class.")
    #     self._customer = customer

    # @property
    # def coffee(self):
    #     return self._coffee

    # @coffee.setter
    # def coffee(self, coffee):
    #     from classes.coffee import Coffee

    #     if not (isinstance(coffee, Coffee)):
    #         raise Exception("Coffee must be an instance of Coffee class.")
    #     self._coffee = coffee