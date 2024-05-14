class ProductModel:
    def __init__(
        self,
        id_producto,
        nombre_producto,
        categoria_producto,
        valor_producto,
        cantidad_producto,
        id_recurso,
    ):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.categoria_producto = categoria_producto
        self.valor_producto = valor_producto
        self.cantidad_producto = cantidad_producto
        self.id_recurso = id_recurso

    @staticmethod
    def map_to_producto(row):
        return ProductModel(*row)
