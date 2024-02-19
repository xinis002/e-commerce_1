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


    def add_product_to_category(self, product):
        self.__products.append(product)

    @property
    def products(self):
        return '\n'.join([f"{product.name}, {product.price} руб. Остаток: {product.amount_in_stock} шт." for product in self.__products])












class Product:
    name: str
    discription: str
    price: float
    amount_in_stock = int

    def __init__(self, name, discription, price, amount_in_stock):
        self.name = name
        self.discription = discription
        self.price = price
        self.amount_in_stock = amount_in_stock


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
        return self.price

    @price.setter
    def price(self,value):
        if value <= 0:
            print('Price is incorrect')
        else:
            self.price = value




