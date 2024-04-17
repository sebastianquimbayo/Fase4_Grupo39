"""
Software de facturación y gestión de inventarios para la empresa Sweet Fruits S.A.S
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import Error
from tkinter import simpledialog
import random
import datetime


# Configuración de la conexión a la base de datos
conexion = mysql.connector.connect(
    host="",
    user="",
    password="*********",
    database="sweet_fruits",
    port=""
)


class Producto():

    def __init__(self, ventana):
        menubar = Menu(ventana)
        ventana.title("Software Sweet Fruits")
        ventana.config(bd=10, menu=menubar, bg="#E0FFCD")

        # *******************Menu******************************************
        # Acciones Menu
        facturacion = Menu(menubar, tearoff=0)
        inventarios = Menu(menubar, tearoff=0)
        informacion = Menu(menubar, tearoff=0)
        menubar.add_command(label="Facturación", command=self.widgets_facturacion, compound=LEFT)
        menubar.add_command(label="Inventarios", command=self.widgets_crud, compound=LEFT)
        menubar.add_command(label="Información de la empresa", command=self.widgets_informacion, compound=LEFT)

        # *************************Widgets**************************************
        # widgets crud
        self.Label_titulo_crud = LabelFrame(ventana)
        self.frame_logo = LabelFrame(ventana)
        self.frame_registro = LabelFrame(ventana, text="Informacion del producto",
                                         font=("Comic Sans", 10, "bold"), pady=5)
        self.frame_botones_registro = LabelFrame(ventana)
        self.frame_tabla_crud = LabelFrame(ventana)

        # widgets buscador
        self.Label_titulo_buscador = LabelFrame(ventana)
        self.frame_buscar_producto = LabelFrame(ventana, text="Buscar producto",
                                                font=("Comic Sans", 10, "bold"), pady=10)
        self.frame_botones_fac = LabelFrame(ventana)

        # Creación del panel costos
        self.frame_costos = LabelFrame(ventana, bd=1, relief=FLAT, bg="#FDFF85", padx=10)
        # Variables para los costos
        self.var_subtotal = StringVar()
        self.var_impuesto = StringVar()
        self.var_total = StringVar()
        self.sub_total = 0
        self.impuestos = 0
        self.total = 0

        # Creación del frame_factura dentro del panel_derecha
        self.frame_factura = Frame(ventana)
        self.texto_recibo = StringVar()

        # widgets informacion
        self.Label_informacion = LabelFrame(ventana)

        # Pantalla inicial
        self.abrir_widget_crud()

    def abrir_widget_crud(self):
        self.widgets_crud()

    def widgets_crud(self):

        self.Label_titulo_crud.config(bd=0)
        self.Label_titulo_crud.grid(row=0, column=0, padx=5, pady=5)
        # ************************ Titulo *********************************
        self.titulo_crud = Label(self.Label_titulo_crud, text="Inventarios Sweet Fruits", fg="black",
                                 font=("Comic Sans", 17, "bold"), bg="#E0FFCD")
        self.titulo_crud.grid(row=0, column=2)

        # ****************************** Logo empresa ***************************************
        self.frame_logo.config(bd=0, bg="#E0FFCD")
        self.frame_logo.grid(row=1, column=0, padx=5, pady=5)

        logo = Image.open("C:/Users/Sebastian Quimbayo/Documents/Cursos_Certificaciones/Programacion_Python/python/Proyecto_Grado/Logo_Sweet.png")
        nueva_imagen = logo.resize((60, 60))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(self.frame_logo, image=render)
        label_imagen.image = render
        label_imagen.grid(row=0, column=0, padx=15, pady=5)

        # ************************** Frame marco ********************************
        self.frame_registro.config(bd=2, bg="#FDFF85")
        self.frame_registro.grid(row=2, column=0, padx=5, pady=5)

        # ************************** Formulario Stock Productos ***********************************
        label_codigo = Label(self.frame_registro, text="Codigo del producto: ", bg="#FDFF85",
                             font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
        self.id_producto = Entry(self.frame_registro, width=25)
        self.id_producto.focus()
        self.id_producto.grid(row=0, column=1, padx=5, pady=8)

        label_nombre = Label(self.frame_registro, text="Nombre del producto: ", bg="#FDFF85",
                             font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
        self.nombre_producto = Entry(self.frame_registro, width=25)
        self.nombre_producto.grid(row=1, column=1, padx=5, pady=8)

        label_categoria = Label(self.frame_registro, text="Categoria: ", bg="#FDFF85",
                                font=("Comic Sans", 10, "bold")).grid(row=2,column=0, sticky='s', padx=5, pady=9)

        self.categoria_producto = ttk.Combobox(self.frame_registro, values=["Fruta Deshidratada", "Frutos Secos"],
                                               width=22, state="readonly")
        self.categoria_producto.current(0)
        self.categoria_producto.grid(row=2, column=1, padx=5, pady=0)

        label_precio = Label(self.frame_registro, text="Precio (S/.): ", bg="#FDFF85",
                             font=("Comic Sans", 10, "bold")).grid(row=0,column=2, sticky='s', padx=5, pady=8)
        self.valor_producto = Entry(self.frame_registro, width=25)
        self.valor_producto.grid(row=0, column=3, padx=5, pady=8)

        label_cantidad = Label(self.frame_registro, text="Cantidad: ", bg="#FDFF85",
                               font=("Comic Sans", 10, "bold")).grid(row=1,column=2, sticky='s', padx=5, pady=8)
        self.cantidad_producto = Entry(self.frame_registro, width=25)
        self.cantidad_producto.grid(row=1, column=3, padx=5, pady=8)

        label_recurso = Label(self.frame_registro, text="Código de recurso necesario: ", bg="#FDFF85",
                              font=("Comic Sans", 10, "bold")).grid(row=2, column=2, sticky='s', padx=10, pady=8)
        self.id_recurso = Entry(self.frame_registro, width=25)
        self.id_recurso.grid(row=2, column=3, padx=10, pady=8)

        # ************************* Frame botones ****************************
        self.frame_botones_registro.config(bd=0, bg="#E0FFCD")
        self.frame_botones_registro.grid(row=3, column=0, padx=5, pady=5)

        # ****************************** Botones Base de Datos **************************
        boton_registrar = Button(self.frame_botones_registro, text="REGISTRAR", command=self.agregar_producto, height=2,
                                 width=12, bg="#32EE11", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0,
                                    column=1, padx=10, pady=15)
        boton_editar = Button(self.frame_botones_registro, text="EDITAR", command=self.editar_producto, height=2,
                              width=12, fg="white", bg="#FF9200",
                              font=("Comic Sans", 10, "bold")).grid(row=0, column=2, padx=10, pady=15)
        boton_eliminar = Button(self.frame_botones_registro, text="ELIMINAR", command=self.eliminar_producto, height=2,
                                width=12, bg="red", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0, column=3,
                                                                                                      padx=10, pady=15)

        # *********************************** Tabla ***********************************
        self.frame_tabla_crud.config(bd=2)
        self.frame_tabla_crud.grid(row=4, column=0, padx=5, pady=5)

        self.tree = ttk.Treeview(self.frame_tabla_crud, height=11,
                                 columns=("columna1", "columna2", "columna3", "columna4", "columna5"))
        self.tree.heading("#0", text='ID Producto', anchor=CENTER)
        self.tree.column("#0", width=90, minwidth=75, stretch=NO)

        self.tree.heading("columna1", text='Nombre Producto', anchor=CENTER)
        self.tree.column("columna1", width=150, minwidth=75, stretch=NO)

        self.tree.heading("columna2", text='Categoria', anchor=CENTER)
        self.tree.column("columna2", width=150, minwidth=75, stretch=NO)

        self.tree.heading("columna3", text='Precio', anchor=CENTER)
        self.tree.column("columna3", width=70, minwidth=60, stretch=NO)

        self.tree.heading("columna4", text='Cantidad', anchor=CENTER)
        self.tree.column("columna4", width=70, minwidth=60, stretch=NO)

        self.tree.heading("columna5", text='ID Recurso', anchor=CENTER)

        self.tree.grid(row=0, column=0, sticky=E)

        self.obtener_productos()

        # REMOVER OTROS WIDGETS
        self.Label_informacion.grid_remove()
        self.widgets_facturacion_remove()

    def widgets_facturacion(self):

        self.Label_titulo_buscador.config(bd=0, bg="#E0FFCD")
        self.Label_titulo_buscador.grid(row=0, column=0, padx=5, pady=5)

        # ************************ Titulo *********************************
        self.titulo_buscador = Label(self.Label_titulo_buscador, text="Facturación Sweet Fruits", fg="black",
                                     font=("Comic Sans", 17, "bold"), bg="#E0FFCD")
        self.titulo_buscador.grid(row=0, column=0)

        # ****************************** Logo empresa ***************************************
        self.frame_logo.config(bd=0, bg="#E0FFCD")
        self.frame_logo.grid(row=0, column=1, padx=5, pady=5)

        logo = Image.open(
            "C:/Users/Sebastian Quimbayo/Documents/Cursos_Certificaciones/Programacion_Python/python/Proyecto_Grado/Logo_Sweet.png")
        nueva_imagen = logo.resize((60, 60))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(self.frame_logo, image=render)
        label_imagen.image = render
        label_imagen.grid(row=0, column=0, padx=15, pady=5)

        # ************************* Frame buscar *****************************
        self.frame_buscar_producto.config(bd=2, bg="#E0FFCD")
        self.frame_buscar_producto.grid(row=2, column=0, padx=5, pady=5)

        # ****************************** Formulario Buscar *****************************
        self.label_buscar = Label(self.frame_buscar_producto, text="Buscar Por: ", bg="#E0FFCD",
                                  font=("Comic Sans", 10, "bold"))
        self.label_buscar.grid(row=0, column=0, sticky='s', padx=5, pady=5)
        self.combo_buscar = ttk.Combobox(self.frame_buscar_producto, values=["Codigo", "Nombre"], width=22,
                                     state="readonly")
        self.combo_buscar.current(0)
        self.combo_buscar.grid(row=0, column=1, padx=5, pady=5)

        label_codigo_codigo = Label(self.frame_buscar_producto, text="Codigo / Nombre del producto: ",
                                font=("Comic Sans", 10, "bold"), bg="#E0FFCD")
        label_codigo_codigo.grid(row=0, column=2, sticky='s', padx=5, pady=5)
        self.codigo_nombre = Entry(self.frame_buscar_producto, width=25)
        self.codigo_nombre.focus()
        self.codigo_nombre.grid(row=0, column=3, padx=10, pady=5)

        # ******************************* Frame marco Botones *********************************
        self.frame_botones_fac.config(bd=0, bg="#E0FFCD")
        self.frame_botones_fac.grid(row=2, column=1, padx=5, pady=5)

        self.boton_buscar = Button(self.frame_botones_fac, text="BUSCAR", command=self.buscar_productos, height=2,
                                   width=20, bg="black", fg="white", font=("Comic Sans", 10, "bold"))
        self.boton_buscar.grid(row=0, column=0, padx=5, pady=5)

        self.boton_agregar = Button(self.frame_botones_fac, text="AGREGAR +", command=self.agregar_producto_fac,
                                    height=2, width=12, bg="#32EE11", fg="white",
                                    font=("Comic Sans", 10, "bold")).grid(row=0, column=2, padx=10, pady=15)

        self.boton_factura = Button(self.frame_botones_fac, text="FACTURAR", command=self.facturar,
                                    height=2, width=12, bg="#FF9200", fg="white",
                                    font=("Comic Sans", 10, "bold")).grid(row=0, column=4, padx=10, pady=15)

        self.boton_factura = Button(self.frame_botones_fac, text="LIMPIAR", command=self.limpiar,
                                    height=2, width=12, bg="blue", fg="white",
                                    font=("Comic Sans", 10, "bold")).grid(row=0, column=6, padx=10, pady=15)

        # Etiquetas de costo y campos de entrada para subtotal

        self.frame_costos.config(bd=2, bg="#FDFF85")
        self.frame_costos.grid(row=5, column=0, padx=5, pady=5)

        etiqueta_subtotal = Label(self.frame_costos, text="Subtotal", font=("Dosis", 12, "bold"),
                                  bg="#FDFF85", fg="black", height=2)
        etiqueta_subtotal.grid(row=1, column=0)

        texto_subtotal = Entry(self.frame_costos, font=("Dosis", 12, "bold"), bd=1, width=10,
                               state="readonly", textvariable=self.var_subtotal)
        texto_subtotal.grid(row=1, column=1, padx=10)

        # Etiquetas de costo y campos de entrada para IVA
        etiqueta_impuesto = Label(self.frame_costos, text="Impuesto", font=("Dosis", 12, "bold"),
                                  bg="#FDFF85", fg="black", height=2)
        etiqueta_impuesto.grid(row=1, column=2)

        texto_impuesto = Entry(self.frame_costos, font=("Dosis", 12, "bold"), bd=1, width=10,
                               state="readonly", textvariable=self.var_impuesto)
        texto_impuesto.grid(row=1, column=3, padx=10)

        # Etiquetas de costo y campos de entrada para Total
        etiqueta_total = Label(self.frame_costos, text="Total", font=("Dosis", 12, "bold"),
                               bg="#FDFF85", fg="black", height=2)
        etiqueta_total.grid(row=1, column=4)

        texto_total = Entry(self.frame_costos, font=("Dosis", 12, "bold"), bd=1, width=10,
                            state="readonly", textvariable=self.var_total)
        texto_total.grid(row=1, column=5, padx=10)

        # Etiquetas de factura
        self.frame_factura.config(bd=2, bg="#E0FFCD")
        self.frame_factura.grid(row=4, column=1, padx=5, pady=0, sticky='nsew')

        # Area de recibo
        self.texto_recibo = Text(self.frame_factura, font=("Dosis", 12, "bold"), bd=1, width=60, height=19)
        self.texto_recibo.grid(row=0, column=0, padx=5, pady=0, sticky='nsew')
        self.productos_seleccionados = []

        # REMOVER OTROS WIDGETS
        self.widgets_crud_remove()
        self.Label_informacion.grid_remove()

    def widgets_crud_remove(self):
        self.Label_titulo_crud.grid_remove()
        self.frame_registro.grid_remove()
        self.frame_botones_registro.grid_remove()

    def widgets_facturacion_remove(self):
        self.Label_titulo_buscador.grid_remove()
        self.frame_buscar_producto.grid_remove()
        self.frame_botones_fac.grid_remove()
        self.frame_costos.grid_remove()
        self.frame_factura.grid_remove()

    def widgets_informacion(self):
        self.Label_informacion.config(bd=0, bg="#E0FFCD")
        self.Label_informacion.grid(row=0, column=0)
        # *************************** Titulo ***************************
        self.Label_titulo = Label(self.Label_informacion, text="SOFTWARE DE FACTURACIÓN Y GESTIÓN DE INVENTARIOS",
                                  fg="black", bg="#E0FFCD", font=("Comic Sans", 25, "bold"), padx=137, pady=20)
        self.Label_titulo.grid(row=0, column=0)

        # ************************** Logo ******************************
        logo = Image.open("C:/Users/Sebastian Quimbayo/Documents/Cursos_Certificaciones/Programacion_Python/python/Proyecto_Grado/Logo_Sweet.png")
        nueva_imagen = logo.resize((170, 170))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(self.Label_informacion, image=render)
        label_imagen.image = render
        label_imagen.grid(row=1, column=0, padx=10, pady=15)

        # ******************* Información de la empresa *************************
        self.Label_titulo = Label(self.Label_informacion, text="> MISIÓN ", fg="black",
                                  font=("Comic Sans", 18, "bold"), bg="#E0FFCD")
        self.Label_titulo.grid(row=2, column=0, sticky=W, padx=30, pady=10)

        # Texto de la misión de la empresa
        texto_mision = (
            "Somos una organización que brinda alternativas de alimentación con bienestar, basados en productos "
            "de alta calidad y fortalecimiento de red de agricultores que permita promover el desarrollo "
            "sostenible en el sector rural colombiano.")

        self.Label_mision = Label(self.Label_informacion, text=texto_mision, fg="black",
                                     font=("Arial", 12), wraplength=700, justify="left", bg="#E0FFCD")
        self.Label_mision.grid(row=3, column=0, sticky="w", padx=30, pady=10)

        self.Label_titulo = Label(self.Label_informacion, text="> VISIÓN ", fg="black",
                                  font=("Comic Sans", 18, "bold"), bg="#E0FFCD")
        self.Label_titulo.grid(row=4, column=0, sticky=W, padx=30, pady=10)

        # Texto de la visión de la empresa
        texto_vision = (
            "Ser identificados nacional e internacionalmente para el año 2030 como una empresa referente "
            "en el sector de salud y bienestar, a través del posicionamiento de productos con óptimos indicadores "
            "de calidad y sostenibilidad corporativa.")

        self.Label_vision = Label(self.Label_informacion, text=texto_vision, fg="black",
                                  font=("Arial", 12), wraplength=700, justify="left", bg="#E0FFCD")
        self.Label_vision.grid(row=5, column=0, sticky="w", padx=30, pady=10)

        self.Label_titulo = Label(self.Label_informacion, text="Sweet Fruits", fg="black",
                                  font=("Comic Sans", 10, "bold"), bg="#E0FFCD")
        self.Label_titulo.grid(row=6, column=0, pady=60)

        # Remove
        self.widgets_crud_remove()
        self.widgets_facturacion_remove()

    # ********************************* CRUD *************************************

    def obtener_productos(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        query = 'SELECT * FROM producto ORDER BY nombre_producto DESC'
        db_rows = self.ejecutar_consulta(query)
        for row in db_rows:
            if len(row) >= 6:  # Verificar que la tupla tenga al menos 6 elementos
                self.tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
            else:
                print("La fila no tiene la cantidad correcta de elementos:", row)


    def agregar_producto(self):
        if self.validar_formulario_completo() and self.validar_registrar():
            try:
                # Establecer la conexión a la base de datos MySQL
                conexion = mysql.connector.connect(
                    host="",
                    user="",
                    password="*********",
                    database="",
                    port="")
                if conexion.is_connected():
                    query = ('INSERT INTO producto (id_producto, nombre_producto, categoria_producto, valor_producto, '
                             'cantidad_producto, id_recurso) VALUES(%s, %s, %s, %s, %s, %s)')
                    parameters = (
                        self.id_producto.get(), self.nombre_producto.get(), self.categoria_producto.get(),
                        self.valor_producto.get(), self.cantidad_producto.get(), self.id_recurso.get())
                    self.ejecutar_consulta(query, parameters)
                    messagebox.showinfo("REGISTRO EXITOSO", f'Producto registrado: {self.nombre_producto.get()}')
                    print('REGISTRADO')
                    self.limpiar_formulario()
            except Error as e:
                print("Error al conectar a MySQL:", e)
            finally:
                if conexion.is_connected():
                    conexion.close()
                    print("Conexión a MySQL cerrada")
        self.obtener_productos()

    def eliminar_producto(self):
        try:
            id_producto = self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            messagebox.showerror("ERROR", "Por favor selecciona un elemento")
            return

        nombre_producto = self.tree.item(self.tree.selection())['values'][0]

        query = "DELETE FROM producto WHERE id_producto = %s"
        respuesta = messagebox.askquestion("ADVERTENCIA", f"¿Seguro que desea eliminar el producto: {nombre_producto}?")
        if respuesta == 'yes':
            self.ejecutar_consulta(query, (id_producto,))
            self.obtener_productos()
            messagebox.showinfo('EXITO', f'Producto eliminado: {nombre_producto}')
        else:
            messagebox.showerror('ERROR', f'Error al eliminar el producto: {nombre_producto}')

    def editar_producto(self):
        try:
            id_producto = self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            messagebox.showerror("ERROR", "Por favor selecciona un elemento")
            return

        nombre_producto = self.tree.item(self.tree.selection())['values'][0]
        categoria_producto = self.tree.item(self.tree.selection())['values'][1]
        cantidad_producto = self.tree.item(self.tree.selection())['values'][2]
        precio_producto = self.tree.item(self.tree.selection())['values'][3]
        id_recurso = self.tree.item(self.tree.selection())['values'][4]

        self.Ventana_editar = Toplevel()
        self.Ventana_editar.title('EDITAR PRODUCTO')
        self.Ventana_editar.resizable(0, 0)

        # Valores ventana editar
        label_codigo = Label(self.Ventana_editar, text="Codigo del producto: ", font=("Comic Sans", 10, "bold")).grid(
            row=0, column=0, sticky='s', padx=5, pady=8)
        nuevo_id_producto = Entry(self.Ventana_editar, textvariable=StringVar(self.Ventana_editar, value=id_producto),
                                  width=25)
        nuevo_id_producto.grid(row=0, column=1, padx=5, pady=8)

        label_nombre = Label(self.Ventana_editar, text="Nombre del producto: ", font=("Comic Sans", 10, "bold")).grid(
            row=1, column=0, sticky='s', padx=5, pady=8)
        nuevo_nombre_producto = Entry(self.Ventana_editar, textvariable=StringVar(self.Ventana_editar, value=nombre_producto),
                             width=25)
        nuevo_nombre_producto.grid(row=1, column=1, padx=5, pady=8)

        label_categoria = Label(self.Ventana_editar, text="Categoria: ", font=("Comic Sans", 10, "bold")).grid(row=2,
                            column=0, sticky='s', padx=5, pady=9)
        nuevo_categoria_producto = ttk.Combobox(self.Ventana_editar,
                                             values=["Fruta Deshidratada", "Frutos Secos"], width=22, state="readonly")
        nuevo_categoria_producto.set(categoria_producto)
        nuevo_categoria_producto.grid(row=2, column=1, padx=5, pady=0)

        label_cantidad = Label(self.Ventana_editar, text="Precio (S/.): ", font=("Comic Sans", 10, "bold")).grid(row=0,
                                column=2, sticky='s', padx=5, pady=8)
        nueva_valor_producto = Entry(self.Ventana_editar,
                               textvariable=StringVar(self.Ventana_editar, value=cantidad_producto),
                               width=25)
        nueva_valor_producto.grid(row=0, column=3, padx=5, pady=8)

        label_precio = Label(self.Ventana_editar, text="Cantidad: ", font=("Comic Sans", 10, "bold")).grid(row=1,
                                column=2, sticky='s', padx=5, pady=8)
        nuevo_cantidad_producto = Entry(self.Ventana_editar, textvariable=StringVar(self.Ventana_editar, value=precio_producto),
                             width=25)
        nuevo_cantidad_producto.grid(row=1, column=3, padx=5, pady=8)

        label_recurso = Label(self.Ventana_editar, text="ID Recurso: ", font=("Comic Sans", 10, "bold")).grid(
            row=2, column=2, sticky='s', padx=10, pady=8)
        nueva_id_recurso = Entry(self.Ventana_editar,
                                  textvariable=StringVar(self.Ventana_editar, value=id_recurso),
                                  width=25)
        nueva_id_recurso.grid(row=2, column=3, padx=10, pady=8)

        boton_actualizar = Button(self.Ventana_editar, text="ACTUALIZAR",
                                  command=lambda: self.actualizar_producto(nuevo_id_producto.get(),
                                                                           nuevo_nombre_producto.get(),
                                                                           nuevo_categoria_producto.get(),
                                                                           nueva_valor_producto.get(),
                                                                           nuevo_cantidad_producto.get(),
                                                                           nueva_id_recurso.get(),
                                                                           id_producto),
                                  height=2, width=20, bg="black", fg="white",
                                  font=("Comic Sans", 10, "bold"))
        boton_actualizar.grid(row=3, column=1, columnspan=2, padx=10, pady=15)

        self.Ventana_editar.mainloop()

    def actualizar_producto(self, codigo, nombre, categoria, precio, cantidad, recurso, id_producto):
        query = ("UPDATE producto SET id_producto = %s, nombre_producto = %s, categoria_producto = %s, "
                 "valor_producto = %s, cantidad_producto = %s, id_recurso = %s WHERE id_producto = %s")
        parameters = (codigo, nombre, categoria, precio, cantidad, recurso, id_producto)
        self.ejecutar_consulta(query, parameters)
        self.obtener_productos()
        messagebox.showinfo('EXITO', 'Producto actualizado correctamente')

    def buscar_productos(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        if self.combo_buscar.get() == 'Codigo':
            query = "SELECT * FROM producto WHERE id_producto LIKE %s"
            parameters = (self.codigo_nombre.get() + "%",)
        else:
            query = "SELECT * FROM producto WHERE nombre_producto LIKE %s"
            parameters = ("%" + self.codigo_nombre.get() + "%",)

        db_rows = self.ejecutar_consulta(query, parameters)

        for row in db_rows:
           self.tree.insert("", 0, text=row[0], values=(row [1], row[2], row[3], row[4], row[5]))

        if not self.tree.get_children():
            messagebox.showerror("ERROR", "Producto no encontrado")

    def agregar_producto_fac(self):
        # Variables
        producto_sub_total = 0
        precio_producto = 0
        impuestos = 0
        total = 0


        try:
            id_producto = self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            messagebox.showerror("ERROR", "Por favor selecciona un elemento")
            return

        nombre_producto = self.tree.item(self.tree.selection())['values'][0]

        # Solicitar la cantidad de productos
        cantidad = simpledialog.askinteger("Cantidad", f"¿Cuántos {nombre_producto} deseas llevar?")

        if cantidad is None or cantidad <= 0:
            messagebox.showerror("ERROR", "Cantidad inválida")
            return

        precio_producto = float(self.tree.item(self.tree.selection())['values'][2])
        self.productos_seleccionados.append((nombre_producto, cantidad, precio_producto))
        producto_sub_total += precio_producto * cantidad
        self.sub_total += producto_sub_total
        producto_impuestos = producto_sub_total * 0.16
        self.impuestos += producto_impuestos
        self.total = self.sub_total + self.impuestos

        self.var_subtotal.set(f"$ {round(self.sub_total, 2)}")
        self.var_impuesto.set(f"$ {round(self.impuestos, 2)}")
        self.var_total.set(f"$ {round(self.total, 2)}")

    def facturar(self):

        # Actualiza la factura en el área de recibo
        self.texto_recibo.delete(1.0, END)
        num_recibo = f"N° - {random.randint(1000, 9999)}"
        fecha = datetime.datetime.now()
        fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
        self.texto_recibo.insert(END, f"Datos: \t{num_recibo}\t\t{fecha_recibo}\n")
        self.texto_recibo.insert(END, f"*" * 90 + "\n")
        self.texto_recibo.insert(END, "Items\t\tCant.\tCosto Items\n")
        self.texto_recibo.insert(END, f"-" * 108)

        for producto in self.productos_seleccionados:
            # Mostrar detalles del producto en la factura
            nombre_producto, cantidad, precio = producto
            costo_producto = cantidad * precio
            self.texto_recibo.insert(END, f"{nombre_producto}\t\t{cantidad}\t${costo_producto}\n")

        subtotal = self.var_subtotal.get()
        impuestos = self.var_impuesto.get()
        total = self.var_total.get()

        self.texto_recibo.insert(END, f"-" * 108)
        self.texto_recibo.insert(END, f" Sub-total: \t\t\t{subtotal}\n")
        self.texto_recibo.insert(END, f" Impuestos: \t\t\t{impuestos}\n")
        self.texto_recibo.insert(END, f" Total: \t\t\t{total}\n")
        self.texto_recibo.insert(END, f"*" * 90 + "\n")
        self.texto_recibo.insert(END, "Vuelva pronto")

    def limpiar(self):
        self.texto_recibo.delete(0.1, END)

        self.sub_total = 0
        self.impuestos = 0
        self.total = 0

        self.productos_seleccionados = []
        self.var_subtotal.set("")
        self.var_impuesto.set("")
        self.var_total.set("")


    # ************************* OTRAS FUNCIONES **************************************

    def ejecutar_consulta(self, query, parameters=()):
        try:
            conexion = mysql.connector.connect(
                host="",
                user="",
                password="*********",
                database="",
                port="")
            if conexion.is_connected():
                cursor = conexion.cursor()
                cursor.execute(query, parameters)
                results = cursor.fetchall()  # Obtener todos los resultados de la consulta
                conexion.commit()
                return results
        except Error as e:
            print("Error al ejecutar la consulta en MySQL:", e)
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'conexion' in locals() and conexion.is_connected():
                conexion.close()
                print("Conexión a MySQL cerrada")

        return None

    def validar_formulario_completo(self):
        if len(self.id_producto.get()) != 0 and len(self.nombre_producto.get()) != 0 and len(self.categoria_producto.get()) != 0 and len(
                self.valor_producto.get()) != 0 and len(self.cantidad_producto.get()) != 0 and len(self.id_recurso.get()) != 0:
            return True
        else:
            messagebox.showerror("ERROR", "Complete todos los campos del formulario")

    def limpiar_formulario(self):
        self.id_producto.delete(0, END)
        self.nombre_producto.delete(0, END)
        self.valor_producto.delete(0, END)
        self.cantidad_producto.delete(0, END)
        self.id_recurso.delete(0, END)

    def validar_registrar(self):
        # Establecer la conexión a la base de datos MySQL
        try:
            conexion = mysql.connector.connect(
                host="",
                user="",
                password="*********",
                database="",
                port="")
            if conexion.is_connected():
                parameters = (self.id_producto.get(),)
                query = "SELECT * FROM producto WHERE id_producto = %s"
                cursor = conexion.cursor()
                cursor.execute(query, parameters)
                dato = cursor.fetchall()
                if not dato:
                    return True
                else:
                    messagebox.showerror("ERROR EN REGISTRO", "Código registrado anteriormente")
        except Error as e:
            print("Error al conectar a MySQL:", e)
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
                print("Conexión a MySQL cerrada")

        return False

if __name__ == '__main__':
    ventana = Tk()
    label_crud = Label(ventana)
    application = Producto(ventana)
    ventana.mainloop()
