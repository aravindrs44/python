from products import Product

class Store:
    def __init__(self, name, product_list = []):
        self.name = name
        self.product_list = product_list
        self.product = product

    def add_product(self, new_product):
        self.product_list.append(new_product)

    def sell_product(self, id):
        self.product_list.pop(id)
        self.product.print_info()

    def inflation(self, percent_increase):
        if percent_increase < 0:
            for prod_counter in product_list:
                self.product.update_price(percent_increase, False)
        elif: percent_increase > 0:
            for prod_counter in product_list:
                self.product.update_price(percent_increase, True)
        else:
            print("No change")


    def set_clearance(self, category, percent_discount):
        
