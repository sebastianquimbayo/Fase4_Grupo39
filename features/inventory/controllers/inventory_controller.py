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

    def eliminarProductoById(
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
