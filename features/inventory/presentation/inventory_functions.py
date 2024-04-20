from tkinter import messagebox, ttk

from common.domain.response_llistener import ResponseListener
from features.inventory.data.models.product_model import ProductModel
from features.inventory.controllers.inventory_controller import InventoryController
from features.inventory.presentation.product_edit_window import ProductEditWindow


def eliminar_producto(
    inventory_controller: InventoryController,
    on_success,
    inventory_table: ttk.Treeview,
):
    try:
        info = inventory_table.item(inventory_table.selection())
        nombre_producto = info["values"][0]
        idProducto = info["text"]
    except IndexError:
        messagebox.showerror("ERROR", "Por favor selecciona un elemento")
        return

    respuesta = messagebox.askquestion(
        "ADVERTENCIA", f"¿Seguro que desea eliminar el producto: {nombre_producto}?"
    )
    if respuesta == "yes":
        inventory_controller.eliminar_producto_by_id(
            idProducto,
            responseListener=ResponseListener(
                onSuccess=on_success,
                onError=lambda: messagebox.showerror(
                    "ERROR", f"Error al eliminar el producto: {nombre_producto}"
                ),
                onLoading=None,
            ),
        )
        messagebox.showinfo("EXITO", f"Producto eliminado: {nombre_producto}")
    else:
        messagebox.showerror(
            "ERROR", f"Error al eliminar el producto: {nombre_producto}"
        )
    pass


def agregar_producto(
    product: ProductModel, inventory_controller: InventoryController, on_success
):
    try:
        inventory_controller.agregar_producto(
            product,
            responseListener=ResponseListener(
                onSuccess=on_success,
                onError=lambda: messagebox.showerror(
                    "ERROR", f"Error al agregar el producto: {product.nombre_producto}"
                ),
                onLoading=None,
            ),
        )

    except:  # noqa: E722
        (
            messagebox.showerror(
                "ERROR", f"Error al agregar el producto: {product.nombre_producto}"
            ),
        )
        print("Ha ocurrido un error")

    pass


def on_add_success(product: ProductModel, on_success):
    messagebox.showinfo(
        "REGISTRO EXITOSO",
        f"Producto registrado: {product.nombre_producto}",
    )
    on_success()
    print("REGISTRADO")
    pass


def send_edit_window(
    parent,
    on_success,
    inventory_table: ttk.Treeview,
    inventory_controller: InventoryController,
):
    try:
        info = inventory_table.item(inventory_table.selection())
        values= info['values']
        product = ProductModel(
            info["text"],
            values[0],
            values[1],
            values[2],
            values[3],
            values[4],
        )
    except IndexError:
        messagebox.showerror("ERROR", "Por favor selecciona un elemento")
        return
    ProductEditWindow(
        parent, 
        product=product,
        inventory_controller=inventory_controller,
        on_success=on_success,
    ).mainloop()
    pass


