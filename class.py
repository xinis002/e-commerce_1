class Category:
    name: str
    discription: str
    products: list

    total_categories = 0
    total_uniq_products = set()


    def __init__(self, name, discription, products):
        self.name = name
        self.discription = discription
        self.product = products
        Category.total_categories += 1
        for product in products:
            Category.total_uniq_products.add(product.name)





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
