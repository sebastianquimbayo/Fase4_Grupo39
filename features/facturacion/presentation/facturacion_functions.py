from tkinter import messagebox, simpledialog, ttk
from common.domain.response_llistener import ResponseListener
from features.facturacion.controllers.facturacion_controller import (
    FacturacionController,
)
from features.facturacion.domain.search_type import SearchType


def buscar_producto(
    facturacion_controller: FacturacionController,
    on_success,
    search_text,
    search_type: SearchType,
):
    try:
        facturacion_controller.search_products(
            search_text,
            search_type=search_type,
            responseListener=ResponseListener(
                onSuccess=on_success,
                onError=lambda: messagebox.showerror(
                    "ERROR", f"Error al buscar el producto: {search_text}"
                ),
                onLoading=None,
            ),
        )
    except IndexError:
        messagebox.showerror("ERROR", "No se pudo buscar por el item seleccionado")
        return
    pass


def agregar_producto(
    facturacion_controller: FacturacionController,
    on_success,
    facturacion_table: ttk.Treeview,
):
    try:
        info = facturacion_table.item(facturacion_table.selection())["values"]

        nombre_producto = info[0]
        precio_producto = float(info[2])

        # Solicitar la cantidad de productos
        cantidad = simpledialog.askinteger(
            "Cantidad", f"¿Cuántos {nombre_producto} deseas llevar?"
        )

        if cantidad is None or cantidad <= 0:
            messagebox.showerror("ERROR", "Cantidad inválida")
            return
        facturacion_controller.add_product_info(
            (nombre_producto, cantidad, precio_producto),
            precio_producto,
            cantidad,
        )
        on_success()
    except IndexError:
        messagebox.showerror("ERROR", "Por favor selecciona un elemento")
        return
    pass


def clear_info(
    facturacion_controller: FacturacionController,
    on_success,
):
    respuesta = messagebox.askquestion(
        "ADVERTENCIA", "¿Seguro que desea limpiar la factura?"
    )
    if respuesta == "yes":
        facturacion_controller.clear_info()
        on_success()
        pass
    
    pass
