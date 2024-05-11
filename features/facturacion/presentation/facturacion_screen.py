from tkinter import (
    ttk,
    Frame,
    Label,
    Button,
    Entry,
    Text,
    LabelFrame,
    FLAT,
    StringVar,
    CENTER,
    NO,
    E,
)


# theme
from config.theme import colors, fonts

from common.presentation.frame_logo import frame_logo
from features.facturacion.controllers.facturacion_controller import (
    FacturacionController,
)
from features.facturacion.domain.search_type import SearchType
from features.facturacion.presentation.facturacion_functions import (
    agregar_producto,
    buscar_producto,
    clear_info,
)


class FacturacionScreen(Frame):
    def __init__(self, parent) -> None:
        self.facturacion_controller = FacturacionController()
        Frame.__init__(self, parent)

        # Variables
        self.var_subtotal = StringVar()
        self.var_impuesto = StringVar()
        self.var_total = StringVar()
        # self.sub_total = 0
        # self.impuestos = 0
        # self.total = 0
        self.build()
        # self.productos_seleccionados = []
        pass

    def cleanTableAndUpdate(self):
        children = self.facturacion_table.get_children()
        for item in children:
            self.facturacion_table.delete(item)
        list = self.facturacion_controller.facturacion_state.productList
        for product in list:
            self.facturacion_table.insert(
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

    def update_info(self):
        data = self.facturacion_controller.facturacion_state
        self.var_subtotal.set(str(data.subtotal))
        self.var_impuesto.set(str(data.impuestos))
        self.var_total.set(str(data.total))
        pass

    def facturacion_table_create(self):
        self.frame_tabla_crud.config(bd=2)
        self.frame_tabla_crud.grid(row=4, column=0, padx=5, pady=5)
        self.facturacion_table = ttk.Treeview(
            self.frame_tabla_crud,
            height=11,
            columns=("columna1", "columna2", "columna3", "columna4", "columna5"),
        )
        # self.facturacion_table.bind("<<TreeviewSelect>>", self.table_item_selected)
        self.facturacion_table.heading("#0", text="ID Producto", anchor=CENTER)
        self.facturacion_table.column("#0", width=90, minwidth=75, stretch=NO)

        self.facturacion_table.heading(
            "columna1", text="Nombre Producto", anchor=CENTER
        )
        self.facturacion_table.column("columna1", width=150, minwidth=75, stretch=NO)

        self.facturacion_table.heading("columna2", text="Categoria", anchor=CENTER)
        self.facturacion_table.column("columna2", width=150, minwidth=75, stretch=NO)

        self.facturacion_table.heading("columna3", text="Precio", anchor=CENTER)
        self.facturacion_table.column("columna3", width=70, minwidth=60, stretch=NO)

        self.facturacion_table.heading("columna4", text="Cantidad", anchor=CENTER)
        self.facturacion_table.column("columna4", width=70, minwidth=60, stretch=NO)

        self.facturacion_table.heading("columna5", text="ID Recurso", anchor=CENTER)

        self.facturacion_table.grid(row=0, column=0, sticky=E)

        list = self.facturacion_controller.facturacion_state.productList

        for product in list:
            self.facturacion_table.insert(
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

    def build(self):
        # configuraciones
        self.frame_tabla_crud = LabelFrame(self)
        self.config(bd=0, bg=colors.BACKGROUND_COLOR)
        self.grid(row=0, column=0, padx=5, pady=5)
        self.facturacion_table_create()

        # ************************ Titulo *********************************
        self.titulo_buscador = Label(
            self,
            text="Facturación Sweet Fruits",
            fg="black",
            font=fonts.LABEL_LARGE,
            bg=colors.BACKGROUND_COLOR,
        )
        self.titulo_buscador.grid(row=0, column=0)

        # ****************************** Logo empresa ***************************************
        frame_logo(self)

        # ************************* Frame buscar *****************************
        self.Label_titulo_buscador = LabelFrame(self)
        self.frame_buscar_producto = LabelFrame(
            self, text="Buscar producto", font=fonts.LABEL_SMALL, pady=10
        )
        self.frame_buscar_producto.config(bd=2, bg=colors.BACKGROUND_COLOR)
        self.frame_buscar_producto.grid(row=2, column=0, padx=5, pady=5)

        # ****************************** Formulario Buscar *****************************
        self.label_buscar = Label(
            self.frame_buscar_producto,
            text="Buscar Por: ",
            bg=colors.BACKGROUND_COLOR,
            font=fonts.LABEL_SMALL,
        )
        self.label_buscar.grid(row=0, column=0, sticky="s", padx=5, pady=5)
        self.combo_buscar = ttk.Combobox(
            self.frame_buscar_producto,
            values=[SearchType.CODIGO.name, SearchType.NOMBRE.name],
            width=22,
            state="readonly",
        )
        self.combo_buscar.current(0)
        self.combo_buscar.grid(row=0, column=1, padx=5, pady=5)

        label_codigo_codigo = Label(
            self.frame_buscar_producto,
            text="Codigo / Nombre del producto: ",
            font=fonts.LABEL_SMALL,
            bg=colors.BACKGROUND_COLOR,
        )
        label_codigo_codigo.grid(row=0, column=2, sticky="s", padx=5, pady=5)
        self.codigo_nombre = Entry(self.frame_buscar_producto, width=25)
        self.codigo_nombre.focus()
        self.codigo_nombre.grid(row=0, column=3, padx=10, pady=5)

        # ******************************* Frame marco Botones *********************************

        self.frame_botones_fac = LabelFrame(self)
        self.frame_botones_fac.config(bd=0, bg=colors.BACKGROUND_COLOR)
        self.frame_botones_fac.grid(row=2, column=1, padx=5, pady=5)

        self.boton_buscar = Button(
            self.frame_botones_fac,
            text="BUSCAR",
            command=lambda: buscar_producto(
                self.facturacion_controller,
                on_success=lambda: self.cleanTableAndUpdate(),
                search_text=self.codigo_nombre.get(),
                search_type=getattr(SearchType, self.combo_buscar.get()),
            ),
            height=2,
            width=20,
            bg="black",
            fg="white",
            font=fonts.LABEL_SMALL,
        )
        self.boton_buscar.grid(row=0, column=0, padx=5, pady=5)

        self.boton_agregar = Button(
            self.frame_botones_fac,
            text="AGREGAR +",
            command=lambda: agregar_producto(
                self.facturacion_controller,
                on_success=lambda: self.update_info(),
                facturacion_table=self.facturacion_table,
            ),
            height=2,
            width=12,
            bg="#32EE11",
            fg="white",
            font=fonts.LABEL_SMALL,
        ).grid(row=0, column=2, padx=10, pady=15)

        self.boton_factura = Button(
            self.frame_botones_fac,
            text="FACTURAR",
            # command=self.facturar,
            height=2,
            width=12,
            bg="#FF9200",
            fg="white",
            font=fonts.LABEL_SMALL,
        ).grid(row=0, column=4, padx=10, pady=15)

        self.boton_factura = Button(
            self.frame_botones_fac,
            text="LIMPIAR",
            command=lambda: clear_info(
                self.facturacion_controller, on_success=lambda: self.update_info()
            ),
            height=2,
            width=12,
            bg="blue",
            fg="white",
            font=fonts.LABEL_SMALL,
        ).grid(row=0, column=6, padx=10, pady=15)

        # Etiquetas de costo y campos de entrada para subtotal

        self.frame_costos = LabelFrame(self, bd=1, relief=FLAT, bg="#FDFF85", padx=10)

        self.frame_costos.config(bd=2, bg="#FDFF85")
        self.frame_costos.grid(row=5, column=0, padx=5, pady=5)

        etiqueta_subtotal = Label(
            self.frame_costos,
            text="Subtotal",
            font=("Dosis", 12, "bold"),
            bg="#FDFF85",
            fg="black",
            height=2,
        )
        etiqueta_subtotal.grid(row=1, column=0)

        texto_subtotal = Entry(
            self.frame_costos,
            font=("Dosis", 12, "bold"),
            bd=1,
            width=10,
            state="readonly",
            textvariable=self.var_subtotal,
        )
        texto_subtotal.grid(row=1, column=1, padx=10)

        # Etiquetas de costo y campos de entrada para IVA
        etiqueta_impuesto = Label(
            self.frame_costos,
            text="Impuesto",
            font=("Dosis", 12, "bold"),
            bg="#FDFF85",
            fg="black",
            height=2,
        )
        etiqueta_impuesto.grid(row=1, column=2)

        texto_impuesto = Entry(
            self.frame_costos,
            font=("Dosis", 12, "bold"),
            bd=1,
            width=10,
            state="readonly",
            textvariable=self.var_impuesto,
        )
        texto_impuesto.grid(row=1, column=3, padx=10)

        # Etiquetas de costo y campos de entrada para Total
        etiqueta_total = Label(
            self.frame_costos,
            text="Total",
            font=("Dosis", 12, "bold"),
            bg="#FDFF85",
            fg="black",
            height=2,
        )
        etiqueta_total.grid(row=1, column=4)

        texto_total = Entry(
            self.frame_costos,
            font=("Dosis", 12, "bold"),
            bd=1,
            width=10,
            state="readonly",
            textvariable=self.var_total,
        )
        texto_total.grid(row=1, column=5, padx=10)

        # Etiquetas de factura
        self.frame_factura = Frame(self)
        self.frame_factura.config(bd=2, bg=colors.BACKGROUND_COLOR)
        self.frame_factura.grid(row=4, column=1, padx=5, pady=0, sticky="nsew")

        # Area de recibo
        self.texto_recibo = Text(
            self.frame_factura, font=("Dosis", 12, "bold"), bd=1, width=60, height=19
        )
        self.texto_recibo.grid(row=0, column=0, padx=5, pady=0, sticky="nsew")

        pass
