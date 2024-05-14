from config.theme import colors

from tkinter import   W, Label, LabelFrame,Frame
from common.presentation.frame_logo import frame_logo


class InformationScreen(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.Label_informacion = LabelFrame(self)

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
        frame_logo(self,(170, 170), padx=10, pady=15, row =1)

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

        pass