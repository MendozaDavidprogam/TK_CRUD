from tkinter import messagebox
from aplicacion.producto_servicio import ProductoServicio
from forma.f_registro import FormularioRegistro

class FormularioRegistro(FormularioRegistro):

    def __init__(self):
        self.producto_servicio = ProductoServicio()
        super().__init__()

    def registro_producto(self):
        nombre = self.nombre_campo.get()
        precio = self.precio_campo.get()

        if not nombre or not precio:
            messagebox.showerror("Error", "ingrese por favor el nombre y precio de producto")
        
        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un numero valido")

        try:
            self.producto_servicio.register(nombre,precio)
            messagebox.showinfo("Exito", "producto registrado correctamente")
            self.actualizarList()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registro_producto el produto {e}")
            

    def actualizarList(self):
        registros = self.tree.get_children()
        for registro in registros:
            self.tree.delete(registro)
        
        productos = self.producto_servicio.obtenerProductos()
        for ref, producto in enumerate(productos):
            color = ('evenrow',) if ref % 2 else ('oddrow',)
            
            
            self.tree.insert(
                parent='', 
                index=ref, 
                iid=ref, 
                text='', 
                tags=color, 
                values=(producto.id, producto.nombre, producto.precio)
            )

    def al_seleccionar_treeview(self, event):
        seleccion = event.widget.selection()
        if seleccion:
            item = event.widget.item(seleccion[0], 'values')
            if item:
                self.limpiar()
                self.id_campo.config(state="normal")
                self.id_campo.insert(0,item[0])
                self.id_campo.config(state="readonly")
                self.nombre_campo.insert(0,item[1])
                self.precio_campo.insert(0, item[2])
                self.eliminarBTN.pack(**self.obtener_Config_BTN())
                self.modificarBTN.pack(**self.obtener_Config_BTN())
                self.registroBTN.pack_forget()

    def modificar_producto(self):

        try:
            id = self.tree.item(self.tree.selection())["values"][0]
            nombre = self.nombre_campo.get()
            precio = self.precio_campo.get()
            self.producto_servicio.modificar(nombre,precio,id)
            self.limpiar()
            self.actualizarList()
        except IndexError as e:
            messagebox.showerror("Error", f"por favor selecciona una fila: {e}")

    
    def eliminar_producto(self):
        try:
            id = self.tree.item(self.tree.selection())["values"][0]
            self.producto_servicio.eliminar(id)
            self.actualizarList()
            self.limpiar()
        except IndexError as e:
            messagebox.showerror("Error", f"por favor selecciona una fila: {e}")