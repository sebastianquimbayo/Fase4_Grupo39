from tkinter import ttk, Toplevel, Button, Entry, Label, StringVar, messagebox

from features.inventory.controllers.inventory_controller import InventoryController
from features.inventory.data.models.product_model import ProductModel
from config.theme import fonts
from common.domain.response_llistener import ResponseListener


def edit_product(
    id_product,
    product: ProductModel,
    inventory_controller: InventoryController,
    on_success,
):
    inventory_controller.edit_product(
        id_product,
        product=product,
        responseListener=ResponseListener(
            onSuccess=on_success,
            onError=lambda: messagebox.showerror(
                "ERROR", f"Error al editar el producto: {product.nombre_producto}"
            ),
            onLoading=None,
        ),
    )
    pass


class ProductEditWindow(Toplevel):
    def __init__(
        self,
        parent,
        inventory_controller: InventoryController,
        product: ProductModel,
        on_success,
    ):
        self.inventory_controller = inventory_controller
        Toplevel.__init__(self, parent)
        self.build(product=product, on_success=on_success)
        pass

    def build(self, product: ProductModel, on_success):
        self.title = "EDITAR PRODUCTO"
        Label(
            self,
            text="Codigo del producto: ",
            font=fonts.LABEL_SMALL,
        ).grid(row=0, column=0, sticky="s", padx=5, pady=8)
        self.resizable(0, 0)

        # Valores ventana editar
        Label(
            self,
            text="Codigo del producto: ",
            font=fonts.LABEL_SMALL,
        ).grid(row=0, column=0, sticky="s", padx=5, pady=8)
        nuevo_id_producto = Entry(
            self,
            textvariable=StringVar(self, value=product.id_producto),
            width=25,
        )
        nuevo_id_producto.grid(row=0, column=1, padx=5, pady=8)

        Label(
            self,
            text="Nombre del producto: ",
            font=fonts.LABEL_SMALL,
        ).grid(row=1, column=0, sticky="s", padx=5, pady=8)
        nuevo_nombre_producto = Entry(
            self,
            textvariable=StringVar(self, value=product.nombre_producto),
            width=25,
        )
        nuevo_nombre_producto.grid(row=1, column=1, padx=5, pady=8)

        Label(self, text="Categoria: ", font=fonts.LABEL_SMALL).grid(
            row=2, column=0, sticky="s", padx=5, pady=9
        )
        nuevo_categoria_producto = ttk.Combobox(
            self,
            values=["Fruta Deshidratada", "Frutos Secos"],
            width=22,
            state="readonly",
        )
        nuevo_categoria_producto.set(product.categoria_producto)
        nuevo_categoria_producto.grid(row=2, column=1, padx=5, pady=0)

        Label(self, text="Precio (S/.): ", font=fonts.LABEL_SMALL).grid(
            row=0, column=2, sticky="s", padx=5, pady=8
        )
        nueva_valor_producto = Entry(
            self,
            textvariable=StringVar(self, value=product.valor_producto),
            width=25,
        )
        nueva_valor_producto.grid(row=0, column=3, padx=5, pady=8)

        Label(self, text="Cantidad: ", font=fonts.LABEL_SMALL).grid(
            row=1, column=2, sticky="s", padx=5, pady=8
        )
        nuevo_cantidad_producto = Entry(
            self,
            textvariable=StringVar(self, value=product.cantidad_producto),
            width=25,
        )
        nuevo_cantidad_producto.grid(row=1, column=3, padx=5, pady=8)

        Label(self, text="ID Recurso: ", font=fonts.LABEL_SMALL).grid(
            row=2, column=2, sticky="s", padx=10, pady=8
        )
        nueva_id_recurso = Entry(
            self,
            textvariable=StringVar(self, value=product.id_recurso),
            width=25,
        )
        nueva_id_recurso.grid(row=2, column=3, padx=10, pady=8)

        boton_actualizar = Button(
            self,
            text="ACTUALIZAR",
            command=lambda: edit_product(
                id_product=product.id_producto,
                product=ProductModel(
                    nuevo_id_producto.get(),
                    nuevo_nombre_producto.get(),
                    nuevo_categoria_producto.get(),
                    nueva_valor_producto.get(),
                    nuevo_cantidad_producto.get(),
                    nueva_id_recurso.get(),
                ),
                inventory_controller=self.inventory_controller,
                on_success=lambda: self.on_success_intern(on_success),
            ),
            height=2,
            width=20,
            bg="black",
            fg="white",
            font=fonts.LABEL_SMALL,
        )
        boton_actualizar.grid(row=3, column=1, columnspan=2, padx=10, pady=15)

        pass
    
    def on_success_intern(self, on_success):
        on_success()
        self.destroy()
        pass
