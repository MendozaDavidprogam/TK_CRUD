import sqlalchemy as db
from sqlalchemy.orm import Session
from dominio.modelo import ProductoModel
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


class ProductoServicio():
    def __init__(self):
        self.engine = db.create_engine('sqlite:///bd/prueba.sqlite',echo=True, future=True)

    def register(self, nombre, precio):
        producto = ProductoModel()
        producto.nombre = nombre
        producto.precio = precio
        with Session(self.engine) as session:
            session.add(producto)
            session.commit()

    def modificar(self , nombre, precio, id_producto):
        try:
            # Buscamos el producto en la bd
            with Session(self.engine) as session:
                producto = session.query(ProductoModel).filter_by(id=id_producto).one()
                # Actualizar los atributos de producto
                producto.nombre = nombre
                producto.precio = precio
                # corfimamos los cambios en la bd 
                session.commit()
                print(f"productos con id {id_producto} se actualizo correctamente")


        except NoResultFound:
            print(f"no se encotro ningun producto con este ID")
            return False
        except Exception as e:
            print(f"Error al actualizar este producto: {e}")
            return False
    

    def obtenerProductos(self)-> list[ProductoModel]:
        producto: ProductoModel = None
        with Session(self.engine) as session:
            producto = session.query(ProductoModel).all()
        return producto

    def eliminar(self, id_producto):
        with Session(self.engine) as session:
            producto = session.query(ProductoModel).filter_by(id=id_producto).first()
            if producto:
                try:
                    session.delete(producto)
                    session.commit()
                    print(f"el producto con este id {id_producto} se a eliminado correctamente")
                except IntegrityError as e:
                    session.rollback()
                    print(f"no se ah podido eliminar este producto con este id {id_producto} Error: {e}")
            else:
                print(f"no se ah encontrado ningun producto con este id {id_producto}")