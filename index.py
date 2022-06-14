class MyCheck:
    def __init__(self, title):
        if len(title) == 0:
            raise ValueError('Значение атрибута title должно быть заполнено')
        else:
            self.__title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) == 0:
            raise ValueError('Значение атрибута title должно быть заполнено')
        else:
            self.__title = value


class Product(MyCheck):
    def __init__(self, title, calorific, cost):
        super().__init__(title)
        
        if calorific <= 0 or cost <= 0:
            raise ValueError('Значение атрибутов calorific и cost может быть только положительным')
        else:
            self.__calorific = calorific
            self.__cost = cost

    @property
    def calorific(self):
        return self.__calorific

    @calorific.setter
    def calorific(self, value):
        if value <= 0:
            raise ValueError('Значение атрибута calorific может быть только положительным')
        else:
            self.__calorific = value
    
    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        if value <= 0:
            raise ValueError('Значение атрибута cost может быть только положительным')
        else:
            self.__cost = value

class Ingredient:
    def __init__(self, product, weight):
        self.product = product
        
        if weight <= 0:
            raise ValueError('Значение атрибута weight может быть только положительным')
        else:
            self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError('Значение атрибута weight может быть только положительным')
        else:
            self.__weight = value

    
    def get_calorific(self):
        return self.weight / 100 * Product.calorific

    
    def get_cost(self):
        return self.weight / 100 * Product.cost


class Pizza(MyCheck):
    def __init__(self, title, ingredients):
        super().__init__(title)
        self.ingredients = ingredients
    
    def __str__(self):
        return f'{self.title} ({self.get_calorific()} kkal) - {self.get_cost()} руб'


    def get_calorific(self):
        get_calorific = 0
        for i in self.ingredients:
            get_calorific += i.product.calorific * i.weight / 100
        return get_calorific


    def get_cost(self):
        get_cost = 0
        for i in self.ingredients:
            get_cost += i.product.cost * i.weight / 100
        return get_cost
    
