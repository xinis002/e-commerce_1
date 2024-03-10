from abc import ABC, abstractmethod

class AbstractProduct(ABC):

    def __init__(self):
        pass


    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    @abstractmethod
    def __str__(self):
        pass


    


class InfoMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
        return f"{class_name}({attributes})"





class Category:
    name: str
    discription: str
    products: list

    total_categories = 0
    total_uniq_products = set()


    def __init__(self, name, discription, products):
        self.name = name
        self.discription = discription
        self.__products = products
        Category.total_categories += 1
        for product in products:
            Category.total_uniq_products.add(product.name)

    def __len__(self):
        return sum(product.quantity for product in self.products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."





    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только продукты или их наследников")
        self.products.append(product)

    def __add__(self, other):
        if isinstance(other, Product):
            self.add_product(other)
        else:
            raise ValueError("Можно добавлять только продукты или их наследников")
        return self

    def average_price(self):
        try:
            total_price = sum(product.price for product in self.products)
            average = total_price / len(self.products)
            return average
        except ZeroDivisionError:
            return 0


    @property
    def products(self):
        return '\n'.join([f"{product.name}, {product.price} руб. Остаток: {product.amount_in_stock} шт." for product in self.__products])














class Product(InfoMixin, AbstractProduct):
    name: str
    discription: str
    price: float
    amount_in_stock = int
    colour = str

    def __init__(self, name, discription, price, amount_in_stock, colour):
        try:
            if amount_in_stock <= 0:
                raise ValueError("Количество товара не может быть нулевым или отрицательным.")
            self.name = name
            self.discription = discription
            self._price = price
            self.amount_in_stock = amount_in_stock
            self.colour = colour
            print(repr(self))
        except ValueError as e:
            print(f"Ошибка при создании продукта: {e}")
            raise





    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.amount_in_stock} шт."




    @classmethod
    def create_product(cls, name, description, price, amount_in_stock, products):
        for existing_product in products:
            if existing_product.name == name:
                existing_product.amount_in_stock += amount_in_stock
                existing_product.price = max(existing_product.price, price)
                return existing_product
        return cls(name, description, price, amount_in_stock)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print('Price is incorrect')
        else:
            self._price = value

    def __add__(self, other):
        if type(self) == type(other):
            total_price = self.price * self.amount_in_stock + other.price * other.amount_in_stock
            return total_price
        else:
            raise TypeError("Можно складывать только товары одного класса")







class Smartphone(InfoMixin, Product):
    def __init__(self,  name, discription, price, amount_in_stock, colour, performance, model, memory):
        super().__init__(name, discription, price, amount_in_stock, colour)
        self.performance = performance
        self.model = model
        self.memory = memory
        print(repr(self))





class Grass(InfoMixin, Product):

    def __init__(self, name, discription, price, amount_in_stock, colour, country, term):
        super().__init__(name, discription, price, amount_in_stock, colour)
        self.country = country
        self.term = term
        print(repr(self))



    



