from common.domain.response_llistener import ResponseListener
from config.config_singleton import ConfigSingleton
from features.facturacion.domain.search_type import SearchType
from features.facturacion.entities.facturacion_state import FacturacionState
from features.inventory.data.models.product_model import ProductModel


class FacturacionController:
    def __init__(self) -> None:
        self.facturacion_state= FacturacionState()
        pass
    
    def sendSuccess(self, responseListener: ResponseListener | None):
        if responseListener is not None:
            responseListener.onSuccess()
        pass

    def sendError(self, responseListener: ResponseListener | None, error):
        if responseListener is not None and responseListener.onError is not None:
            responseListener.onError(error)
        pass

    def search_products(
        self, 
        key_search,
        responseListener: ResponseListener | None,
        search_type: SearchType = SearchType.NOMBRE,
    ):
        try:
            query = ""
            if(search_type ==SearchType.CODIGO):
                query = "SELECT * FROM producto WHERE id_producto LIKE %s"
            else:
                query = "SELECT * FROM producto WHERE nombre_producto LIKE %s"
            parameters = ("%" + key_search + "%",)
            db_response = ConfigSingleton().dbUtils.ejecutar_consulta(query,parameters=parameters)
            list = []
            for response in db_response:
                list.append(ProductModel.map_to_producto(response))
            
            self.facturacion_state.set_product_list(list)
            self.sendSuccess(responseListener)
        except IndexError:
            self.sendError(responseListener, "")
            pass
        
        pass
    
    def add_product_info(self, product_info, precio, cantidad):
        self.facturacion_state.add_product_info(product_info)
        self.facturacion_state.modify_values(precio, cantidad)
        pass
    
    def clear_info(self):
        self.facturacion_state.clear_info()
        pass
