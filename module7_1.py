class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products = []
            for i in file:
                name, weight, category = i.strip().split(',')
                product = Product(name, weight, category)
                products.append(product)
        return products

    def add(self, *product):
        with open(self.__file_name, 'a') as file:
            for i in product:
                if i.name in self.get_products():
                    file.write(f'{i.name},{i.weight},{i.category}\n')
                else:
                    print(f'Продукт {i.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
