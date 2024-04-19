from tkinter import Tk, Menu


from config.theme import colors
from config.config_singleton import ConfigSingleton

# SCREENS
from features.facturacion.presentation.facturacion_screen import FacturacionScreen
from features.inventory.presentation.inventory_screen import InventoryScreen


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # label_crud = Label(self)

        # Creando la primera instancia, al ser singleton, siempre sera el mismo
        configSingleton = ConfigSingleton()

        # inyectando dependencias en singleton
        configSingleton.load_data()

        self.current_screen = None

        self.title("Software Sweet Fruits")
        self.config(bd=10, menu=self.createMenu(), bg=colors.BACKGROUND_COLOR)
        pass

    def show_screen(self, screen_class):
        if self.current_screen:
            self.current_screen.pack_forget()
        self.current_screen = screen_class(self)
        self.current_screen.pack()

    def createMenu(self) -> Menu:
        menubar = Menu(self)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Screens", menu=file_menu)
        file_menu.add_command(
            label="Screen 1", command=lambda: self.show_screen(FacturacionScreen)
        )
        file_menu.add_command(
            label="Inventory", command=lambda: self.show_screen(InventoryScreen)
        )
        # file_menu.add_command(
        #     label="Screen 2", command=lambda: self.show_screen(Screen2)
        # )
        # file_menu.add_command(
        #     label="Screen 3", command=lambda: self.show_screen(Screen3)
        # )
        self.show_screen(InventoryScreen)

        return menubar

    def initLoop(self):
        self.mainloop()
        pass

    # def navigateToScreen(self, screen):
