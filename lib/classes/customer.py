class Customer:
    def __init__(self, name):
        self.name = name
        self._order = []
        self._coffee = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <=15:
            self._name = name
        else:
            raise Exception

    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._order.append(new_order)
        else:
            raise Exception
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee not in self._coffee and isinstance(new_coffee, Coffee):
            self._coffee.append(new_coffee)
        return self._coffee
    
    
    
    # def create_order(self):
    #     return len(self._order)
    
     
    # def average_price(self):
    #     return sum([order.coffee for order in self._coffee]) / len(self._coffee)