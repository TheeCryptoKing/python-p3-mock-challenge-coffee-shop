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
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception 
    
    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order, Order):
            self._order.append(new_order)
        return self._order
        pass

    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee not in self._coffee and isinstance(new_coffee, Coffee):
            self._coffee.append(new_coffee)
        return self._coffee
        pass

    def create_order(self, coffee, price):
        from classes.coffee import Coffee
        pass

