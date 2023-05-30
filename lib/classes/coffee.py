class Coffee:

    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception 
    
    def orders(self, new_order=None):
        from classes.order import Order 
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
        pass

    def customers(self, new_customer=None):
        from classes.customer import Customer
        # write unique list , meanisn not repeatin and all elements ORIGINAL
        if new_customer not in self._customers and isinstance(new_customer, Customer):
            self._customers.append(new_customer)
        return self._customers
        pass

    def num_orders(self):
        return len(self._orders)
        pass

    def average_price(self):
        return sum([order.price for order in self._orders]) / len(self._orders)
        pass
