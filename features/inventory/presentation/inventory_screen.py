from tkinter import (
    ttk,
    Frame,
    CENTER,
    NO,
    E,
    Misc,
    Button,
    Entry,
    Label,
    LabelFrame,
)

from features.inventory.data.models.product_model import ProductModel

from config.theme import colors, fonts
from features.inventory.controllers.inventory_controller import InventoryController
from features.inventory.presentation.inventory_functions import (
    eliminar_producto,
    agregar_producto,
    send_edit_window,
)
from common.domain.response_llistener import ResponseListener
from common.presentation.frame_logo import frame_logo


class InventoryScreen(Frame):
    def __init__(self, parent) -> None:
        self.parent =parent
        self.inventory_controller = InventoryController()
        Frame.__init__(self, parent)
        self.inventory_controller.obtener_all_productos(
            responseListener=ResponseListener(
                onSuccess=lambda: self.update(),
                onError=None,
                onLoading=None,
            )
        )
        self.build()
        pass

    # listener de selección de la tabla
    def table_item_selected(self, event=None):
        selection = self.inventory_table.selection()
        if selection:
            self.edit_button.grid()
            self.delete_button.grid()

        else:
            self.edit_button.grid_remove()
            self.delete_button.grid_remove()
        pass

    def cleanTableAndUpdate(self):
        children = self.inventory_table.get_children()
        for item in children:
            self.inventory_table.delete(item)
        list = self.inventory_controller.inventory_state.productList
        for product in list:
            self.inventory_table.insert(
                "",
                0,
                text=product.id_producto,
                values=(
                    product.nombre_producto,
                    product.categoria_producto,
                    product.valor_producto,
                    product.cantidad_producto,
                    product.id_recurso,
                ),
            )
        self.update()
        pass

    def build(self):
        self.label_titulo = LabelFrame(self)
        
        self.frame_registro = LabelFrame(
            self,
            text="Informacion del producto",
            font=fonts.LABEL_SMALL,
            background=colors.BACKGROUND_COLOR,
            pady=5,
        )
        self.frame_botones_registro = LabelFrame(
            self,
            background=colors.BACKGROUND_COLOR,
        )
        self.frame_tabla_crud = LabelFrame(self)

        #
        self.label_titulo.config(bd=0)
        self.label_titulo.grid(row=0, column=0, padx=5, pady=5)
        # ************************ Titulo *********************************
        self.titulo = Label(
            self.label_titulo,
            text="Inventarios Sweet Fruits",
            fg=colors.BLACK,
            font=fonts.LABEL_LARGE,
            bg=colors.BACKGROUND_COLOR,
        )
        self.titulo.grid(row=0, column=2)

        # # ****************************** Logo empresa ***************************************
        frame_logo(self)
        
        # ************************** Frame marco ********************************
        self.frame_registro.config(bd=2, bg=colors.FORM_BAKGROUND)
        self.frame_registro.grid(row=2, column=0, padx=5, pady=5)

        # ************************** Formulario Stock Productos ***********************************
        self.label_create(
            text="Codigo del producto: ",
        ).grid(row=0, column=0, sticky="s", padx=5, pady=8)
        self.id_producto = Entry(self.frame_registro, width=25)
        self.id_producto.focus()
        self.id_producto.grid(row=0, column=1, padx=5, pady=8)

        self.label_create(
            text="Nombre del producto: ",
        ).grid(row=1, column=0, sticky="s", padx=5, pady=8)

        self.nombre_producto = Entry(self.frame_registro, width=25)
        self.nombre_producto.grid(row=1, column=1, padx=5, pady=8)

        self.label_create(
            text="Categoria: ",
        ).grid(row=2, column=0, sticky="s", padx=5, pady=9)

        self.categoria_producto = ttk.Combobox(
            self.frame_registro,
            values=["Fruta Deshidratada", "Frutos Secos"],
            width=22,
            state="readonly",
        )
        self.categoria_producto.current(0)
        self.categoria_producto.grid(row=2, column=1, padx=5, pady=0)

        self.label_create(
            text="Precio (S/.): ",
        ).grid(row=0, column=2, sticky="s", padx=5, pady=8)
        self.valor_producto = Entry(self.frame_registro, width=25)
        self.valor_producto.grid(row=0, column=3, padx=5, pady=8)

        self.label_create(
            text="Cantidad: ",
        ).grid(row=1, column=2, sticky="s", padx=5, pady=8)
        self.cantidad_producto = Entry(self.frame_registro, width=25)
        self.cantidad_producto.grid(row=1, column=3, padx=5, pady=8)

        self.label_create(
            text="Código de recurso necesario: ",
        ).grid(row=2, column=2, sticky="s", padx=10, pady=8)
        self.id_recurso = Entry(self.frame_registro, width=25)
        self.id_recurso.grid(row=2, column=3, padx=10, pady=8)

        # ************************* Frame botones ****************************
        self.frame_botones_registro.config(bd=0, bg=colors.BACKGROUND_COLOR)
        self.frame_botones_registro.grid(row=3, column=0, padx=5, pady=5)

        # ****************************** Botones Base de Datos **************************
        Button(
            self.frame_botones_registro,
            text="REGISTRAR",
            command=lambda:agregar_producto(
                ProductModel(
                    self.id_producto.get(),
                    self.nombre_producto.get(),
                    self.categoria_producto.get(),
                    self.valor_producto.get(),
                    self.cantidad_producto.get(),
                    self.id_recurso.get(),
                ),
                inventory_controller= self.inventory_controller,
                on_success=lambda: self.cleanTableAndUpdate(),
            ),
            height=2,
            width=12,
            bg=colors.SUCCESS,
            fg="white",
            font=fonts.LABEL_SMALL,
        ).grid(row=0, column=1, padx=10, pady=15)
        self.edit_button = Button(
            self.frame_botones_registro,
            text="EDITAR",
            command=lambda: send_edit_window(
                parent=self.parent,
                inventory_table=self.inventory_table,
                inventory_controller=self.inventory_controller,
                on_success=lambda: self.cleanTableAndUpdate(),
            ),
            height=2,
            width=12,
            fg="white",
            bg="#FF9200",
            font=fonts.LABEL_SMALL,
        )
        self.edit_button.grid(row=0, column=2, padx=10, pady=15)
        self.edit_button.grid_remove()
        self.delete_button = Button(
            self.frame_botones_registro,
            text="ELIMINAR",
            command=lambda: eliminar_producto(
                self.inventory_controller,
                lambda: self.cleanTableAndUpdate(),
                self.inventory_table,
            ),
            height=2,
            width=12,
            bg=colors.PRIMARY,
            # fg="red",
            font=fonts.LABEL_SMALL,
        )
        self.delete_button.grid(row=0, column=3, padx=10, pady=15)
        self.delete_button.grid_remove()

        # *********************************** Tabla ***********************************
        self.frame_tabla_crud.config(bd=2)
        self.frame_tabla_crud.grid(row=4, column=0, padx=5, pady=5)

        self.inventory_table_create()
        pass

    def label_create(
        self,
        text: str,
        master: Misc | None = None,
    ) -> Label:
        masster = master if master is not None else self.frame_registro
        return Label(
            masster,
            text=text,
            bg=colors.FORM_BAKGROUND,
            font=fonts.LABEL_SMALL,
        )

    def inventory_table_create(self):
        self.inventory_table = ttk.Treeview(
            self.frame_tabla_crud,
            height=11,
            columns=("columna1", "columna2", "columna3", "columna4", "columna5"),
        )
        self.inventory_table.bind("<<TreeviewSelect>>", self.table_item_selected)
        self.inventory_table.heading("#0", text="ID Producto", anchor=CENTER)
        self.inventory_table.column("#0", width=90, minwidth=75, stretch=NO)

        self.inventory_table.heading("columna1", text="Nombre Producto", anchor=CENTER)
        self.inventory_table.column("columna1", width=150, minwidth=75, stretch=NO)

        self.inventory_table.heading("columna2", text="Categoria", anchor=CENTER)
        self.inventory_table.column("columna2", width=150, minwidth=75, stretch=NO)

        self.inventory_table.heading("columna3", text="Precio", anchor=CENTER)
        self.inventory_table.column("columna3", width=70, minwidth=60, stretch=NO)

        self.inventory_table.heading("columna4", text="Cantidad", anchor=CENTER)
        self.inventory_table.column("columna4", width=70, minwidth=60, stretch=NO)

        self.inventory_table.heading("columna5", text="ID Recurso", anchor=CENTER)

        self.inventory_table.grid(row=0, column=0, sticky=E)

        list = self.inventory_controller.inventory_state.productList

        for product in list:
            self.inventory_table.insert(
                "",
                0,
                text=product.id_producto,
                values=(
                    product.nombre_producto,
                    product.categoria_producto,
                    product.valor_producto,
                    product.cantidad_producto,
                    product.id_recurso,
                ),
            )
        pass
