from datetime import datetime
from bson import ObjectId
from .init_db import get_database

db = get_database()

# Funciones para coleccion1
## create. crea un documento para la coleccion1, utilizando docstring.
def create_doc_coleccion1(docstring):
    """Crea un documento en la colección coleccion1."""
    doc = {
        "name": docstring,
        "created_at": datetime.now()
    }
    db.coleccion1.insert_one(doc)
    return doc

## read. lee un documento de la coleccion1. Describir con docstring. 
def read_doc_coleccion1(doc_id):
    """Lee un documento de la colección coleccion1."""
    doc = db.coleccion1.find_one({"_id": ObjectId(doc_id)})
    return doc

## update. actualiza un documento de la coleccion1. Describir con docstring.
def update_doc_coleccion1(doc_id, docstring):
    """Actualiza un documento de la colección coleccion1."""
    db.coleccion1.update_one(
        {"_id": ObjectId(doc_id)},
        {"$set": {"name": docstring}}
    )

## delete. elimina un documento de la coleccion1. Describir con docstring.
def delete_doc_coleccion1(doc_id):
    """Elimina un documento de la colección coleccion1."""
    db.coleccion1.delete_one({"_id": ObjectId(doc_id)})

# Funciones para coleccion2
## create. crea un documento para la coleccion2, utilizando docstring.
## read. lee un documento de la coleccion2. Describir con docstring.
## update. actualiza un documento de la coleccion2. Describir con docstring.
## delete. elimina un documento de la coleccion2. Describir con docstring.

# Funciones para coleccion3
## create. crea un documento para la coleccion3, utilizando docstring.
## read. lee un documento de la coleccion3. Describir con docstring.
## update. actualiza un documento de la coleccion3. Describir con docstring.
## delete. elimina un documento de la coleccion3. Describir con docstring.
  


# Significado de CRUD. {Create, Read, Update, Delete}.
# CRUD es un acrónimo que significa Crear, Leer, Actualizar y Eliminar.
# Estas son las operaciones básicas que se pueden realizar en cualquier 
# base de datos o sistema de almacenamiento de datos.