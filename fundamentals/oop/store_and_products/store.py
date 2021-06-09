class Store:
    def __init__(self, name, product_list = []):
        self.name = name
        self.product_list = product_list
        self.product = product

    def add_product(self, new_product):
        self.product_list.append(new_product)

    def sell_product(self, id):
        self.product_list.pop(id)

    def inflation(self, percent_increase):
        if percent_increase < 0:
            self


    def set_clearance(self, category, percent_discount):
        pass
