import datetime
import random
from tkinter import END, Text, messagebox, simpledialog, ttk
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


def facturar(
    texto_recibo: Text,
    facturacion_controller: FacturacionController,
):
    # Actualiza la factura en el área de recibo
    texto_recibo.delete(1.0, END)
    num_recibo = f"N° - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = (
        f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    )
    texto_recibo.insert(END, f"Datos: \t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, "*" * 90 + "\n")
    texto_recibo.insert(END, "Items\t\tCant.\tCosto Items\n")
    texto_recibo.insert(END, "-" * 108)
    info = facturacion_controller.facturacion_state
    for producto in info.selected_products_info:
        # Mostrar detalles del producto en la factura
        nombre_producto, cantidad, precio = producto
        costo_producto = cantidad * precio
        texto_recibo.insert(
            END, f"{nombre_producto}\t\t{cantidad}\t${costo_producto}\n"
        )

    subtotal = info.subtotal
    impuestos = info.impuestos
    total = info.total

    texto_recibo.insert(END, "-" * 108)
    texto_recibo.insert(END, f" Sub-total: \t\t\t{subtotal}\n")
    texto_recibo.insert(END, f" Impuestos: \t\t\t{impuestos}\n")
    texto_recibo.insert(END, f" Total: \t\t\t{total}\n")
    texto_recibo.insert(END, "*" * 90 + "\n")
    texto_recibo.insert(END, "Vuelva pronto")
    pass
