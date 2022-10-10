class Product:
    def __init__(self):
        self.Dict_product = {}

    def get(self, name_product):
        if name_product in self.Dict_product:
            return f"{name_product} - {self.Dict_product[name_product]}"
        else:
            self.eror_index(name_product)

    def update(self, name_product, prize_product):
        if name_product in self.Dict_product:
            self.Dict_product[name_product] = prize_product
        else:
            self.eror_index(name_product)

    def create(self, name_product, prize_product):
        if name_product not in self.Dict_product:
            self.Dict_product[name_product] = prize_product
        else:
            self.update(name_product, prize_product)

    def delete(self, name_product):
        if name_product in self.Dict_product:
            del self.Dict_product[name_product]
        else:
            self.eror_index(name_product)

    def get_sum_product(self):
        if len(self.Dict_product):
            all_sum_product = self.Dict_product.values()
            return f"your all budget equal to: {all_sum_product}"
        else:
            return "you don`t have any product"

    def eror_index(self, index):
        return f"Don`t exist a {index} in list product"


if __name__ == '__main__':

