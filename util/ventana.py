def ventana_centrada(ventana, aplicacionA, aplicacionL):
    pantallaA = ventana.winfo_screenwidth()
    pantallaL = ventana.winfo_screenheight()
    x = int((pantallaA/2) - (aplicacionA/2))
    y = int((pantallaL/2) - (aplicacionL/2))
    return ventana.geometry(f"{aplicacionA}x{aplicacionL}+{x}+{y}")
    