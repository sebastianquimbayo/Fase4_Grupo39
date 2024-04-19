from tkinter import (
    ttk,
    Frame,
    CENTER,
    NO,
    E,
    Misc,
    
    Entry,
    Label,
    LabelFrame,
    messagebox,
)
from tkmacosx import Button
from PIL import ImageTk, Image

from config.theme import colors, fonts
from features.inventory.controllers.inventory_controller import InventoryController
from common.domain.response_llistener import ResponseListener

logoRoute = "assets/images/Logo_Sweet.png"


class InventoryScreen(Frame):
    def __init__(self, parent) -> None:
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

    def build(self):
        self.label_titulo = LabelFrame(self)
        self.frame_logo = LabelFrame(self)
        self.frame_registro = LabelFrame(
            self,
            text="Informacion del producto",
            font=fonts.LABEL_SMALL,
            pady=5,
        )
        self.frame_botones_registro = LabelFrame(self)
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

        # ****************************** Logo empresa ***************************************
        self.frame_logo.config(bd=0, bg=colors.BACKGROUND_COLOR)
        self.frame_logo.grid(row=1, column=0, padx=5, pady=5)

        logo = Image.open(logoRoute)
        nueva_imagen = logo.resize((60, 60))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(self.frame_logo, image=render)
        label_imagen.image = render
        label_imagen.grid(row=0, column=0, padx=15, pady=5)

        # ************************** Frame marco ********************************
        self.frame_registro.config(bd=2, bg=colors.FORM_BAKGROUND)
        self.frame_registro.grid(row=2, column=0, padx=5, pady=5)

        # ************************** Formulario Stock Productos ***********************************
        self.createLabel(
            text="Codigo del producto: ",
        ).grid(row=0, column=0, sticky="s", padx=5, pady=8)
        self.id_producto = Entry(self.frame_registro, width=25)
        self.id_producto.focus()
        self.id_producto.grid(row=0, column=1, padx=5, pady=8)

        self.createLabel(
            text="Nombre del producto: ",
        ).grid(row=1, column=0, sticky="s", padx=5, pady=8)

        self.nombre_producto = Entry(self.frame_registro, width=25)
        self.nombre_producto.grid(row=1, column=1, padx=5, pady=8)

        self.createLabel(
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

        self.createLabel(
            text="Precio (S/.): ",
        ).grid(row=0, column=2, sticky="s", padx=5, pady=8)
        self.valor_producto = Entry(self.frame_registro, width=25)
        self.valor_producto.grid(row=0, column=3, padx=5, pady=8)

        self.createLabel(
            text="Cantidad: ",
        ).grid(row=1, column=2, sticky="s", padx=5, pady=8)
        self.cantidad_producto = Entry(self.frame_registro, width=25)
        self.cantidad_producto.grid(row=1, column=3, padx=5, pady=8)

        self.createLabel(
            text="Código de recurso necesario: ",
        ).grid(row=2, column=2, sticky="s", padx=10, pady=8)
        self.id_recurso = Entry(self.frame_registro, width=25)
        self.id_recurso.grid(row=2, column=3, padx=10, pady=8)

        # ************************* Frame botones ****************************
        self.frame_botones_registro.config(bd=0, bg=colors.BACKGROUND_COLOR)
        self.frame_botones_registro.grid(row=3, column=0, padx=5, pady=5)

        # ****************************** Botones Base de Datos **************************
        # Button(
        #     self.frame_botones_registro,
        #     text="REGISTRAR",
        #     command=self.agregar_producto,
        #     height=2,
        #     width=12,
        #     bg="#32EE11",
        #     fg="white",
        #     font=fonts.LABEL_SMALL,
        # ).grid(row=0, column=1, padx=10, pady=15)
        # Button(
        #     self.frame_botones_registro,
        #     text="EDITAR",
        #     command=self.editar_producto,
        #     height=2,
        #     width=12,
        #     fg="white",
        #     bg="#FF9200",
        #     font=fonts.LABEL_SMALL,
        # ).grid(row=0, column=2, padx=10, pady=15)
        Button(
            self.frame_botones_registro,
            text="ELIMINAR",
            command=self.eliminar_producto,
            # height=2,
            # width=12,
            bg=colors.PRIMARY,
            # fg="red",
            font=fonts.LABEL_SMALL,
        ).grid(row=0, column=3, padx=10, pady=15)

        # *********************************** Tabla ***********************************
        self.frame_tabla_crud.config(bd=2)
        self.frame_tabla_crud.grid(row=4, column=0, padx=5, pady=5)

        self.inventory_table_create()

        # self.obtener_productos()
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

    def createLabel(
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

    def eliminar_producto(self):
        try:
            info = self.inventory_table.item(self.inventory_table.selection())
            nombre_producto = info["values"][0]
            idProducto = info["text"]
        except IndexError:
            messagebox.showerror("ERROR", "Por favor selecciona un elemento")
            return

        respuesta = messagebox.askquestion(
            "ADVERTENCIA", f"¿Seguro que desea eliminar el producto: {nombre_producto}?"
        )
        if respuesta == "yes":
            self.inventory_controller.eliminarProductoById(
                idProducto,
                responseListener=ResponseListener(
                    onSuccess=lambda: self.cleanTableAndUpdate(),
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
