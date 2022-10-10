class Product:
    def __init__(self):
        self.Dict_product = {}

    def get(self, name_product):
        if name_product in self.Dict_product:
            return f"{name_product} - {self.Dict_product[name_product]}"
        else:
            return self.eror_index(name_product)

    def update(self, name_product, prize_product):
        if name_product in self.Dict_product:
            self.Dict_product[name_product] = prize_product
        else:
            return self.eror_index(name_product)

    def product_is_exist(self, product):
        return product in self.Dict_product

    def create(self, name_product, prize_product):
        if name_product not in self.Dict_product:
            self.Dict_product[name_product] = prize_product
        else:
            self.update(name_product, prize_product)

    def delete(self, name_product):
        if name_product in self.Dict_product:
            del self.Dict_product[name_product]
        else:
            return self.eror_index(name_product)

    def get_sum_product(self):
        if len(self.Dict_product):
            all_sum_product = sum(self.Dict_product.values())
            return f"your all budget equal to: {all_sum_product}"
        else:
            return "you don`t have any product"

    def eror_index(self, index):
        return f"Don`t exist a {index} in list product"

    def helper_text(self):
        return '''
         1)For creating new list product type "create" after type name product and prize
         2) for updating type 'update' after type name product and prize
         3) for deleting product type 'delete' and after type name product
         4) for getting prize product type 'get'
         4) for getting budget all product type 'budget'
         5) for exit type 'exit'
        '''


if __name__ == '__main__':
    sub = 'None'
    product = Product()
    print(product.helper_text())
    while sub != 'exit':
        sub = input('Enter a massage: ')
        if sub == 'exit':
            break
        elif sub == 'create':
            name = input('name product: ')
            prize = input('prize product: ')
            product.create(name, prize)
        elif sub == 'updating':
            name = input('name product: ')
            prize = input('prize product: ')
            product.update(name, prize)
        elif sub == 'delete':
            name = input('name product: ')
            product.delete(name)
        elif sub == 'get':
            name = input('name product: ')
            print(product.get(name))
        elif sub == 'budget':
            print(product.get_sum_product())
        else:
            print('you type wrong command type again')
