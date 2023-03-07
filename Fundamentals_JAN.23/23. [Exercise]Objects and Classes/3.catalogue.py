class Catalogue:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []
    
    def add_product(self, product_name):
        self.products.append(product_name)
    
    def get_by_letter(self, first_letter):
        filtered_products = [prod for prod in self.products if prod.startswith(first_letter)]
        return filtered_products

    def __repr__(self) -> str:
        products = sorted(self.products)
        return f"Items in the {self.name} catalogue:\n"+'\n'.join(products)
    

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)