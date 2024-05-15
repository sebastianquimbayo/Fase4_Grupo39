from PIL import ImageTk, Image
from tkinter import Label, LabelFrame

# theme
from config.theme import colors

logoRoute = (
    "/home/daniel/Documents/Proyectos/Fase4_Grupo39/assets/images/Logo_Sweet.png"
)


def frame_logo(
    master,
    size: tuple[int, int] = (60, 60),
    padx=15,
    pady=5,
    row=0,
    column=0,
):
    try:
    
        frame_logo = LabelFrame(master)
        frame_logo.config(bd=0, bg=colors.BACKGROUND_COLOR)
        frame_logo.grid(row=0, column=1, padx=5, pady=5)

        logo = Image.open(logoRoute)
        nueva_imagen = logo.resize(size)
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(frame_logo, image=render)
        label_imagen.image = render
        label_imagen.grid(row=row, column=column, padx=padx, pady=pady)
        return frame_logo
    except Exception as e:
        print(e)
    pass
