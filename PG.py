"""
Software de facturación y gestión de inventarios para la empresa Sweet Fruits S.A.S
"""

from mysql.connector import Error
from tkinter import (
    messagebox,
    END,
    W,
    Label,
    simpledialog
)
from PIL import ImageTk, Image

import mysql.connector

import random
import datetime

# theme
from config.theme import colors
from config.config_singleton import ConfigSingleton

from app import App


logoRoute = "assets/images/Logo_Sweet.png"


class Producto:
    def __init__(self, ventana):
        print("hello")

        # menubar.add_command(
        #     label="Inventarios", command=self.widgets_crud, compound=LEFT
        # )
        # menubar.add_command(
        #     label="Información de la empresa",
        #     command=self.widgets_informacion,
        #     compound=LEFT,
        # )

        # # *************************Widgets**************************************
        # # widgets crud
       
        

        # # widgets buscador
        # self.Label_titulo_buscador = LabelFrame(ventana)
        # self.frame_buscar_producto = LabelFrame(
        #     ventana, text="Buscar producto", font=("Comic Sans", 10, "bold"), pady=10
        # )
        # self.frame_botones_fac = LabelFrame(ventana)

        # # Creación del panel costos
        # self.frame_costos = LabelFrame(
        #     ventana, bd=1, relief=FLAT, bg="#FDFF85", padx=10
        # )
        # # Variables para los costos
        # self.var_subtotal = StringVar()
        # self.var_impuesto = StringVar()
        # self.var_total = StringVar()
        # self.sub_total = 0
        # self.impuestos = 0
        # self.total = 0

        # # Creación del frame_factura dentro del panel_derecha
        # self.frame_factura = Frame(ventana)
        # self.texto_recibo = StringVar()

        # # widgets informacion
        # self.Label_informacion = LabelFrame(ventana)

        # # Pantalla inicial
        # self.abrir_widget_crud()

    def abrir_widget_crud(self):
        self.widgets_crud()

    def widgets_crud(self):
        

        # REMOVER OTROS WIDGETS
        self.Label_informacion.grid_remove()
        self.widgets_facturacion_remove()

    def widgets_facturacion(self):
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
        self.Label_informacion.config(bd=0, bg=colors.BACKGROUND_COLOR)
        self.Label_informacion.grid(row=0, column=0)
        # *************************** Titulo ***************************
        self.Label_titulo = Label(
            self.Label_informacion,
            text="SOFTWARE DE FACTURACIÓN Y GESTIÓN DE INVENTARIOS",
            fg="black",
            bg=colors.BACKGROUND_COLOR,
            font=("Comic Sans", 25, "bold"),
            padx=137,
            pady=20,
        )
        self.Label_titulo.grid(row=0, column=0)

        # ************************** Logo ******************************
        logo = Image.open(logoRoute)
        nueva_imagen = logo.resize((170, 170))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(self.Label_informacion, image=render)
        label_imagen.image = render
        label_imagen.grid(row=1, column=0, padx=10, pady=15)

        # ******************* Información de la empresa *************************
        self.Label_titulo = Label(
            self.Label_informacion,
            text="> MISIÓN ",
            fg="black",
            font=("Comic Sans", 18, "bold"),
            bg=colors.BACKGROUND_COLOR,
        )
        self.Label_titulo.grid(row=2, column=0, sticky=W, padx=30, pady=10)

        # Texto de la misión de la empresa
        texto_mision = (
            "Somos una organización que brinda alternativas de alimentación con bienestar, basados en productos "
            "de alta calidad y fortalecimiento de red de agricultores que permita promover el desarrollo "
            "sostenible en el sector rural colombiano."
        )

        self.Label_mision = Label(
            self.Label_informacion,
            text=texto_mision,
            fg="black",
            font=("Arial", 12),
            wraplength=700,
            justify="left",
            bg=colors.BACKGROUND_COLOR,
        )
        self.Label_mision.grid(row=3, column=0, sticky="w", padx=30, pady=10)

        self.Label_titulo = Label(
            self.Label_informacion,
            text="> VISIÓN ",
            fg="black",
            font=("Comic Sans", 18, "bold"),
            bg=colors.BACKGROUND_COLOR,
        )
        self.Label_titulo.grid(row=4, column=0, sticky=W, padx=30, pady=10)

        # Texto de la visión de la empresa
        texto_vision = (
            "Ser identificados nacional e internacionalmente para el año 2030 como una empresa referente "
            "en el sector de salud y bienestar, a través del posicionamiento de productos con óptimos indicadores "
            "de calidad y sostenibilidad corporativa."
        )

        self.Label_vision = Label(
            self.Label_informacion,
            text=texto_vision,
            fg="black",
            font=("Arial", 12),
            wraplength=700,
            justify="left",
            bg=colors.BACKGROUND_COLOR,
        )
        self.Label_vision.grid(row=5, column=0, sticky="w", padx=30, pady=10)

        self.Label_titulo = Label(
            self.Label_informacion,
            text="Sweet Fruits",
            fg="black",
            font=("Comic Sans", 10, "bold"),
            bg=colors.BACKGROUND_COLOR,
        )
        self.Label_titulo.grid(row=6, column=0, pady=60)

        # Remove
        self.widgets_crud_remove()
        self.widgets_facturacion_remove()

    # ********************************* CRUD *************************************

    def editar_producto(self):
        try:
            id_producto = self.tree.item(self.tree.selection())["text"]
        except IndexError as e:
            messagebox.showerror("ERROR", "Por favor selecciona un elemento")
            return

        nombre_producto = self.tree.item(self.tree.selection())["values"][0]
        categoria_producto = self.tree.item(self.tree.selection())["values"][1]
        cantidad_producto = self.tree.item(self.tree.selection())["values"][2]
        precio_producto = self.tree.item(self.tree.selection())["values"][3]
        id_recurso = self.tree.item(self.tree.selection())["values"][4]

        
        
        self.Ventana_editar.mainloop()

    def actualizar_producto(
        self, codigo, nombre, categoria, precio, cantidad, recurso, id_producto
    ):
        query = (
            "UPDATE producto SET id_producto = %s, nombre_producto = %s, categoria_producto = %s, "
            "valor_producto = %s, cantidad_producto = %s, id_recurso = %s WHERE id_producto = %s"
        )
        parameters = (codigo, nombre, categoria, precio, cantidad, recurso, id_producto)
        ConfigSingleton().dbUtils.ejecutar_consulta(query, parameters)
        self.obtener_productos()
        messagebox.showinfo("EXITO", "Producto actualizado correctamente")

    def buscar_productos(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        if self.combo_buscar.get() == "Codigo":
            query = "SELECT * FROM producto WHERE id_producto LIKE %s"
            parameters = (self.codigo_nombre.get() + "%",)
        else:
            query = "SELECT * FROM producto WHERE nombre_producto LIKE %s"
            parameters = ("%" + self.codigo_nombre.get() + "%",)

        db_rows = ConfigSingleton().dbUtils.ejecutar_consulta(query, parameters)

        for row in db_rows:
            self.tree.insert(
                "", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5])
            )

        if not self.tree.get_children():
            messagebox.showerror("ERROR", "Producto no encontrado")

    def agregar_producto_fac(self):
        # Variables
        producto_sub_total = 0
        precio_producto = 0
        impuestos = 0
        total = 0

        try:
            id_producto = self.tree.item(self.tree.selection())["text"]
        except IndexError as e:
            messagebox.showerror("ERROR", "Por favor selecciona un elemento")
            return

        nombre_producto = self.tree.item(self.tree.selection())["values"][0]

        # Solicitar la cantidad de productos
        cantidad = simpledialog.askinteger(
            "Cantidad", f"¿Cuántos {nombre_producto} deseas llevar?"
        )

        if cantidad is None or cantidad <= 0:
            messagebox.showerror("ERROR", "Cantidad inválida")
            return

        precio_producto = float(self.tree.item(self.tree.selection())["values"][2])
        self.productos_seleccionados.append(
            (nombre_producto, cantidad, precio_producto)
        )
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
        fecha_recibo = (
            f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
        )
        self.texto_recibo.insert(END, f"Datos: \t{num_recibo}\t\t{fecha_recibo}\n")
        self.texto_recibo.insert(END, f"*" * 90 + "\n")
        self.texto_recibo.insert(END, "Items\t\tCant.\tCosto Items\n")
        self.texto_recibo.insert(END, f"-" * 108)

        for producto in self.productos_seleccionados:
            # Mostrar detalles del producto en la factura
            nombre_producto, cantidad, precio = producto
            costo_producto = cantidad * precio
            self.texto_recibo.insert(
                END, f"{nombre_producto}\t\t{cantidad}\t${costo_producto}\n"
            )

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

    def validar_formulario_completo(self):
        if (
            len(self.id_producto.get()) != 0
            and len(self.nombre_producto.get()) != 0
            and len(self.categoria_producto.get()) != 0
            and len(self.valor_producto.get()) != 0
            and len(self.cantidad_producto.get()) != 0
            and len(self.id_recurso.get()) != 0
        ):
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
                host="", user="", password="*********", database="", port=""
            )
            if conexion.is_connected():
                parameters = (self.id_producto.get(),)
                query = "SELECT * FROM producto WHERE id_producto = %s"
                cursor = conexion.cursor()
                cursor.execute(query, parameters)
                dato = cursor.fetchall()
                if not dato:
                    return True
                else:
                    messagebox.showerror(
                        "ERROR EN REGISTRO", "Código registrado anteriormente"
                    )
        except Error as e:
            print("Error al conectar a MySQL:", e)
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
                print("Conexión a MySQL cerrada")

        return False


if __name__ == "__main__":
    App().initLoop()
