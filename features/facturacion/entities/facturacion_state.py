from features.inventory.data.models.product_model import ProductModel


class FacturacionState:
    def __init__(self) -> None:
        self.productList = []
        
        self.selected_products_info= []
        self.impuestos= 0
        self.subtotal = 0
        self.total = 0
        pass

    def set_product_list(self, list: list[ProductModel]):
        self.productList = list
        pass
    
    def add_product_info(self, item_product):
        self.selected_products_info.append(item_product)
        pass
    
    def modify_values(self, precio_producto, cantidad, IVA = 0.16):
        producto_sub_total=0
        producto_sub_total += precio_producto * cantidad
        self.subtotal += producto_sub_total
        producto_impuestos = producto_sub_total * 0.16
        self.impuestos += producto_impuestos
        self.total = self.subtotal + self.impuestos
        pass
    
    def clear_info(self):
        self.selected_products_info = []
        self.impuestos = 0
        self.subtotal = 0
        self.total = 0
        pass