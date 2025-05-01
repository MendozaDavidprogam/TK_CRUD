import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import util.ventana as ventana

COLOR_D_FONDO = "#fff"
COLOR_D_FONDO_BUSQUEDA = "#f7f8fa"

class FormularioRegistro(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config_ventana()
        self.paneles()
        self.controles()

    def config_ventana(self):
        self.title("CRUD")
        w,h = 800, 600
        ventana.ventana_centrada(self, w, h)
        self.configure(bg=COLOR_D_FONDO_BUSQUEDA)

    def paneles(self):
        self.marcoTitulo = tk.Frame(
            self, bg=COLOR_D_FONDO_BUSQUEDA, height=60)
        self.marcoTitulo.pack(side=tk.TOP, fill='both')

        self.marcoRegistro = tk.Frame(
            self, bg=COLOR_D_FONDO, height=60)
        self.marcoRegistro.pack(side=tk.TOP, fill='both', pady=12)

        self.marcoAcciones = tk.Frame(
            self, bg=COLOR_D_FONDO, height=60)
        self.marcoAcciones.pack(side=tk.TOP, fill='both')

        self.marcoProductos = tk.Frame(
            self, bg=COLOR_D_FONDO)
        self.marcoProductos.pack(
            side=tk.TOP, fill='both', padx=40, pady=20, expand=True
        )

    def controles(self):
        title = tk.Label(self.marcoTitulo, text = "Registro De Producto", font=('Roboto', 25), fg="#40484F", bg=COLOR_D_FONDO_BUSQUEDA, pady=25)
        title.pack(expand=True, fill=tk.BOTH)

        id_etiqueta = tk.Label(self.marcoRegistro, text="Id", font=(
            'Times', 15), fg="#8085AB", bg=COLOR_D_FONDO, width=6)
        id_etiqueta.pack(side="left",padx=6,pady=11)

        self.id_campo = ttk.Entry(self.marcoRegistro, font=(
            'Times', 15), state="readonly", width=6)
        self.id_campo.pack(side="left", pady=6,padx=11)

        nombre_etiqueta = tk.Label(self.marcoRegistro, text="Producto", font=(
            'Times', 15), fg="#8085AB", bg=COLOR_D_FONDO)
        nombre_etiqueta.pack(side="left",padx=6,pady=11)

        self.nombre_campo = ttk.Entry(self.marcoRegistro, font=('Times', 15))
        self.nombre_campo.pack(side="left", padx=6,pady=11)


        precio_etiqueta = tk.Label(self.marcoRegistro, text="Precio", font=(
            'Times', 15), fg="#8085AB", bg=COLOR_D_FONDO)
        precio_etiqueta.pack(side="left",padx=6,pady=11)

        self.precio_campo = ttk.Entry(self.marcoRegistro, font=('Times', 15))
        self.precio_campo.pack(side="left", padx=6,pady=11)

        self.registroBTN = tk.Button(self.marcoAcciones, text="Registrar", font=(
            'Times', 12), bg="#4A9DD9", bd=0, fg="#fff", padx=14, command=self.registro_producto)
        self.registroBTN.pack(**self.obtener_Config_BTN())
        self.registroBTN.bind("<Return>", (lambda event: self.registro_producto()))


        self.eliminarBTN = tk.Button(self.marcoAcciones, text="Eliminar", font=(
            'Times', 12), bg="#D14749", bd=0, fg="#fff", padx=14, command=self.eliminar_producto)
        self.eliminarBTN.pack(**self.obtener_Config_BTN())
        self.eliminarBTN.bind("<Return>", (lambda event: self.eliminar_producto()))
        self.eliminarBTN.pack_forget()
        

        self.modificarBTN = tk.Button(self.marcoAcciones, text="Modificar", font=(
            'Times', 12), bg="#51986E", bd=0, fg="#fff", padx=14, command=self.modificar_producto)
        self.modificarBTN.pack(**self.obtener_Config_BTN())
        self.modificarBTN.bind("<Return>", (lambda event: self.modificar_producto()))
        self.modificarBTN.pack_forget()


        self.limpiarBTN = tk.Button(self.marcoAcciones, text="limpiar campos", font=(
            'Times', 12), bg="#e39531", bd=0, fg="#fff", padx=14, command=self.limpiar)
        self.limpiarBTN.pack(**self.obtener_Config_BTN())
        self.limpiarBTN.bind("<Return>", (lambda event: self.limpiar()))

        # Tabla
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", background="#eafbea",
            foreground="#000")
        style.configure('Treeview.Heading', background="#6f9a8d", foreground="#fff")
        tree_s = ttk.Scrollbar(self.marcoProductos)
        tree_s.pack(side=tk.RIGHT, fill=tk.Y)
        #self.tree = ttk.Scrollbar(self.marcoProductos, 
         #                         show='headings', ysrollcomand=tree_s.set)
        self.tree = ttk.Treeview(self.marcoProductos, show='headings', yscrollcommand=tree_s.set)
        self.tree['columns'] = ('Id', 'Nombre', 'Precio')
        self.tree.column('#0')
        self.tree.column('Id')
        self.tree.column('Nombre')
        self.tree.column('Precio')

        self.tree.heading('#0', text='')
        self.tree.heading('Id', text='Id')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Precio', text='Precio')

        self.tree.pack(expand=True, fill='both')
        self.tree.bind("<<TreeviewSelect>>", self.al_seleccionar_treeview)

        self.tree.tag_configure('oddrow', background='#ffffe0')
        self.tree.tag_configure('evenrow', background='#eafbea')

        self.actualizarList()

    def actualizarList(self):
        pass

    def registro_producto(self):
        pass

    def eliminar_producto(self):
        pass

    def modificar_producto(self):
        pass

    def al_seleccionar_treeview(self, event):
        pass

    def obtener_Config_BTN(self):
        return {"side": tk.RIGHT, "padx":10, "pady":10}

    def limpiar(self):
        try:
            self.nombre_campo.delete(0,'end')
            self.precio_campo.delete(0,'end')
            self.id_campo.config(state="normal")
            self.id_campo.delete(0,'end')
            self.id_campo.config(state="readonly")
            self.registroBTN.pack(**self.obtener_Config_BTN())
            self.eliminarBTN.pack_forget()
            self.modificarBTN.pack_forget()
        except Exception as e:
            messagebox.showerror("Error", f" Error en la limpieza {e}")
        