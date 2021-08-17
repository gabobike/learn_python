from tkinter import *


class MiApp:
    def __init__(self, parent=None, **configs):

        # ##################################################################
        # Ventana principal
        # ##################################################################
        self.my_parent = parent
        self.my_parent.geometry("700x600")

        # ##################################################################
        # Agrego contenedor
        # ##################################################################
        self.contenedor = Frame(self.my_parent, bg="#444")
        self.contenedor.pack(expand=YES, fill=BOTH)
        # ##################################################################
        # Agrego Secciones Principales
        # ##################################################################
        #####  CERRAR #####
        self.seccion_cerrar = Frame(
            self.contenedor, bg="#FF7F50", height=22, borderwidth=2, relief=RAISED
        )
        self.seccion_cerrar.pack(side=TOP, expand=NO, fill=X, padx=7)
        self.cerrar = Frame(self.seccion_cerrar, bg="#222", height=22)
        self.cerrar.pack(side=TOP, expand=NO, fill=X)

        #####  SECCIÓN CONTROLES #####
        self.seccion_controles = Frame(
            self.contenedor, bg="red", borderwidth=2, relief=RAISED
        )
        self.seccion_controles.pack(side=TOP, expand=NO, fill=BOTH, padx=7, pady=7)
        titulo_controles = "Controles"
        Label(
            self.seccion_controles,
            text=titulo_controles,
            bg="#222",
            fg="OrangeRed",
            justify=LEFT,
        ).pack(side=TOP, expand=NO, fill=X, anchor=W)
        self.controles = Frame(self.seccion_controles, bg="#222")
        self.controles.pack(side=TOP, expand=NO, fill=X)

        #####  SECCIÓN REPRESENTACIÓN #####
        self.seccion_representacion = Frame(
            self.contenedor, bg="red", borderwidth=2, relief=RAISED
        )
        self.seccion_representacion.pack(
            side=BOTTOM, expand=YES, fill=BOTH, padx=7, pady=7
        )
        titulo_grafico = "Representación gráfica"
        Label(
            self.seccion_representacion,
            text=titulo_grafico,
            bg="#222",
            fg="OrangeRed",
            justify=LEFT,
        ).pack(side=TOP, expand=NO, fill=X, anchor=W)
        self.representacion = Frame(self.seccion_representacion, bg="OrangeRed")
        self.representacion.pack(side=TOP, expand=YES, fill=BOTH)
        # ##################################################################
        # Controles
        # ##################################################################
        self.temas_opciones = Frame(self.controles, borderwidth=5, bg="#222")
        self.nombres_opciones = Frame(self.controles, borderwidth=5, bg="#222")
        self.side_contenedor = Frame(self.controles, borderwidth=5, bg="#222")
        self.fill_contenedor = Frame(self.controles, borderwidth=5, bg="#222")
        self.expand_contenedor = Frame(self.controles, borderwidth=5, bg="#222")
        self.anchor_contenedor = Frame(self.controles, borderwidth=5, bg="#222")

        self.temas_opciones.pack(side=LEFT, expand=NO, fill=Y, anchor=N)
        self.nombres_opciones.pack(side=LEFT, expand=YES, fill=Y, anchor=N)
        self.side_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.fill_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.expand_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.anchor_contenedor.pack(side=LEFT, expand=YES, anchor=N)

        Label(
            self.temas_opciones,
            borderwidth=4,
            relief=RAISED,
            text="Temas",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.nombres_opciones,
            borderwidth=4,
            relief=RAISED,
            text="Opciones",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.side_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Side",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.fill_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Fill",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.expand_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Expand",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.anchor_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Anchor",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)

        # ##################################################################
        # Representación
        # ##################################################################
        self.representacion_superior = Frame(self.representacion, bg="red")
        self.representacion_superior.pack(side=TOP, expand=YES, fill=BOTH)

        self.deslizador_central = Frame(
            self.representacion_superior,
            background="black",
            borderwidth=4,
            relief=SUNKEN,
            width=250,
        )
        self.deslizador_central.pack(side=LEFT, expand=YES, fill=BOTH)

        self.deslizador_vertical = Frame(
            self.representacion_superior,
            background="#FF7F50",
            borderwidth=4,
            relief=SUNKEN,
            width=50,
        )
        self.deslizador_vertical.pack(side=RIGHT, expand=NO, fill=Y)

        self.deslizador_horizontal = Frame(
            self.representacion, borderwidth=4, relief=SUNKEN, height=50, bg="OrangeRed"
        )
        self.deslizador_horizontal.pack(side=TOP, fill=X)


if __name__ == "__main__":
    root = Tk()
    MiApp(root)
    root.mainloop()
