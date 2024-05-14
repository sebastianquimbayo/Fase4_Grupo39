from config.config_singleton import ConfigSingleton
from features.inventory.entities.inventory_state import InventoryState
from common.domain.response_llistener import ResponseListener
from features.inventory.data.models.product_model import ProductModel


class InventoryController:
    def __init__(self) -> None:
        self.inventory_state = InventoryState()
        pass

    def sendSuccess(self, responseListener: ResponseListener | None):
        if responseListener is not None:
            responseListener.onSuccess()
        pass

    def sendError(self, responseListener: ResponseListener | None, error):
        if responseListener is not None and responseListener.onError is not None:
            responseListener.onError(error)
        pass

    def obtener_all_productos(self, responseListener: ResponseListener | None = None):
        query = "SELECT * FROM producto ORDER BY nombre_producto DESC"
        try:
            list = []
            db_response = ConfigSingleton().dbUtils.ejecutar_consulta(query)
            for response in db_response:
                list.append(ProductModel.map_to_producto(response))
            self.inventory_state.set_product_list(list)
            self.sendSuccess(responseListener)

        except IndexError:
            self.sendError(responseListener, "")
            pass
        pass

    def eliminar_producto_by_id(
        self, idProducto, responseListener: ResponseListener | None = None
    ):
        query = "DELETE FROM producto WHERE id_producto = %s"
        try:
            ConfigSingleton().dbUtils.ejecutar_consulta(query, (idProducto,))
            self.obtener_all_productos(responseListener)
        except IndexError:
            if responseListener is not None and responseListener.onError is not None:
                responseListener.onError("")
            pass

        pass

    def agregar_producto(
        self, product: ProductModel, responseListener: ResponseListener | None = None
    ):
        try:
            query = (
                "INSERT INTO producto (id_producto, nombre_producto, categoria_producto, valor_producto, "
                "cantidad_producto, id_recurso) VALUES(%s, %s, %s, %s, %s, %s)"
            )
            parameters = (
                product.id_producto,
                product.nombre_producto,
                product.categoria_producto,
                product.valor_producto,
                product.cantidad_producto,
                product.id_recurso,
            )
            ConfigSingleton().dbUtils.ejecutar_consulta(query, parameters)
            self.obtener_all_productos(responseListener)

        except:  # noqa: E722
            self.sendError(responseListener, "")
        pass

    def edit_product(
        self,
        id_product,
        product: ProductModel,
        responseListener: ResponseListener | None = None,
    ):
        try:
            query = (
                "UPDATE producto SET id_producto = %s, nombre_producto = %s, categoria_producto = %s, "
                "valor_producto = %s, cantidad_producto = %s, id_recurso = %s WHERE id_producto = %s"
            )
            parameters = (
                product.id_producto,
                product.nombre_producto,
                product.categoria_producto,
                product.valor_producto,
                product.cantidad_producto,
                product.id_recurso,
                id_product,
            )
            ConfigSingleton().dbUtils.ejecutar_consulta(query, parameters)
            self.obtener_all_productos(responseListener)
        except:  # noqa: E722
            self.sendError(responseListener, "")

        pass
