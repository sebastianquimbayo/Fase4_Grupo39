
from features.inventory.data.models.product_model import ProductModel


class InventoryState:
    def __init__(self) -> None:
        self.productList  = []
        pass

    def set_product_list(self,list:list[ProductModel]):
        self.productList=list