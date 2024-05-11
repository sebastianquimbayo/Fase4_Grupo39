from mysql.connector import Error
from tkinter import (
    messagebox,
    END
)

import mysql.connector

import random
import datetime

# theme



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
      
        # self.texto_recibo = StringVar()

        # # widgets informacion
        # self.Label_informacion = LabelFrame(ventana)

        # # Pantalla inicial
        
    # ********************************* CRUD *************************************
   




    def facturar(self):
        # Actualiza la factura en el área de recibo
        self.texto_recibo.delete(1.0, END)
        num_recibo = f"N° - {random.randint(1000, 9999)}"
        fecha = datetime.datetime.now()
        fecha_recibo = (
            f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
        )
        self.texto_recibo.insert(END, f"Datos: \t{num_recibo}\t\t{fecha_recibo}\n")
        self.texto_recibo.insert(END, "*" * 90 + "\n")
        self.texto_recibo.insert(END, "Items\t\tCant.\tCosto Items\n")
        self.texto_recibo.insert(END, "-" * 108)

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

        self.texto_recibo.insert(END, "-" * 108)
        self.texto_recibo.insert(END, f" Sub-total: \t\t\t{subtotal}\n")
        self.texto_recibo.insert(END, f" Impuestos: \t\t\t{impuestos}\n")
        self.texto_recibo.insert(END, f" Total: \t\t\t{total}\n")
        self.texto_recibo.insert(END, "*" * 90 + "\n")
        self.texto_recibo.insert(END, "Vuelva pronto")

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

