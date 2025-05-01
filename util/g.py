import os

def crearCarpeta_Si_No_Existe(ruta, carpetaNombre):
    ruta_completa = os.path.join(ruta, carpetaNombre)

    if not os.path.exists(ruta_completa):
        os.makedirs(ruta_completa)
        return True, f"carpeta creada'{carpetaNombre}' en {ruta}"
    else:
        return False, f"esta carpeta '{carpetaNombre}' ya existe en'{ruta}'"