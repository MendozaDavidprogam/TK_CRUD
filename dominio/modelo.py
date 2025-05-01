from sqlalchemy import Column
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProductoModel(Base):
    __tablename__="Productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200))
    precio = Column(Float)
    
    def __repr__(self):
        return f'productos({self.id},{self.nombre},{self.precio})'

    def __str__(self):
        return f'productos({self.id}, {self.nombre}, {self.precio})'
        