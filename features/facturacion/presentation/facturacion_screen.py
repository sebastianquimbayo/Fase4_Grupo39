from tkinter import ttk, Frame, Label, Button, Entry, Text
from PIL import ImageTk, Image


# theme
from config.theme import colors, fonts


logoRoute = "assets/images/Logo_Sweet.png"


class FacturacionScreen(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.config(bd=0, bg=colors.BACKGROUND_COLOR)
        self.grid(row=0, column=0, padx=5, pady=5)

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
        self.frame_logo.config(bd=0, bg=colors.BACKGROUND_COLOR)
        self.frame_logo.grid(row=0, column=1, padx=5, pady=5)

        logo = Image.open(logoRoute)
        nueva_imagen = logo.resize((60, 60))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(self.frame_logo, image=render)
        label_imagen.image = render
        label_imagen.grid(row=0, column=0, padx=15, pady=5)

        # ************************* Frame buscar *****************************
        self.frame_buscar_producto.config(bd=2, bg=colors.BACKGROUND_COLOR)
        self.frame_buscar_producto.grid(row=2, column=0, padx=5, pady=5)

        # ****************************** Formulario Buscar *****************************
        self.label_buscar = Label(
            self.frame_buscar_producto,
            text="Buscar Por: ",
            bg=colors.BACKGROUND_COLOR,
            font=("Comic Sans", 10, "bold"),
        )
        self.label_buscar.grid(row=0, column=0, sticky="s", padx=5, pady=5)
        self.combo_buscar = ttk.Combobox(
            self.frame_buscar_producto,
            values=["Codigo", "Nombre"],
            width=22,
            state="readonly",
        )
        self.combo_buscar.current(0)
        self.combo_buscar.grid(row=0, column=1, padx=5, pady=5)

        label_codigo_codigo = Label(
            self.frame_buscar_producto,
            text="Codigo / Nombre del producto: ",
            font=("Comic Sans", 10, "bold"),
            bg=colors.BACKGROUND_COLOR,
        )
        label_codigo_codigo.grid(row=0, column=2, sticky="s", padx=5, pady=5)
        self.codigo_nombre = Entry(self.frame_buscar_producto, width=25)
        self.codigo_nombre.focus()
        self.codigo_nombre.grid(row=0, column=3, padx=10, pady=5)

        # ******************************* Frame marco Botones *********************************
        self.frame_botones_fac.config(bd=0, bg=colors.BACKGROUND_COLOR)
        self.frame_botones_fac.grid(row=2, column=1, padx=5, pady=5)

        self.boton_buscar = Button(
            self.frame_botones_fac,
            text="BUSCAR",
            command=self.buscar_productos,
            height=2,
            width=20,
            bg="black",
            fg="white",
            font=("Comic Sans", 10, "bold"),
        )
        self.boton_buscar.grid(row=0, column=0, padx=5, pady=5)

        self.boton_agregar = Button(
            self.frame_botones_fac,
            text="AGREGAR +",
            command=self.agregar_producto_fac,
            height=2,
            width=12,
            bg="#32EE11",
            fg="white",
            font=("Comic Sans", 10, "bold"),
        ).grid(row=0, column=2, padx=10, pady=15)

        self.boton_factura = Button(
            self.frame_botones_fac,
            text="FACTURAR",
            command=self.facturar,
            height=2,
            width=12,
            bg="#FF9200",
            fg="white",
            font=("Comic Sans", 10, "bold"),
        ).grid(row=0, column=4, padx=10, pady=15)

        self.boton_factura = Button(
            self.frame_botones_fac,
            text="LIMPIAR",
            command=self.limpiar,
            height=2,
            width=12,
            bg="blue",
            fg="white",
            font=("Comic Sans", 10, "bold"),
        ).grid(row=0, column=6, padx=10, pady=15)

        # Etiquetas de costo y campos de entrada para subtotal

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
        self.frame_factura.config(bd=2, bg=colors.BACKGROUND_COLOR)
        self.frame_factura.grid(row=4, column=1, padx=5, pady=0, sticky="nsew")

        # Area de recibo
        self.texto_recibo = Text(
            self.frame_factura, font=("Dosis", 12, "bold"), bd=1, width=60, height=19
        )
        self.texto_recibo.grid(row=0, column=0, padx=5, pady=0, sticky="nsew")
        self.productos_seleccionados = []
        pass
