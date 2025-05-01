import sqlalchemy as db 
import dominio.modelo as modelo
import util.g as gen

# nombre de la carpeta donde se almacenaran los datos de la bd
carpetaNombre = "bd"

# ruta donde se crea la carpeta para los datos de la bd
ruta = "./"

# se crea la carpeta si no existe
gen.crearCarpeta_Si_No_Existe(ruta, carpetaNombre)
engine = db.create_engine('sqlite:///bd/prueba.sqlite', echo=True, future=True)
modelo.Base.metadata.create_all(engine)

