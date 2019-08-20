from pymongo import MongoClient

#conexion a bd cloud de mongo db
MONGO_URI = ""


if __name__ == '__main__':
    print("MongoClient imported successfully!")
    ''' generar un solo usuario en la base de datos
    #se crea la base de datos
    database = client['mi_app']
    #se crea una coleccion
    users = database['users']
    #creamos un usuario demo en la coleccion
    usuario_demo = {
        "user": "Luis Luna",
        "email": "ljlunan@gmail.com"
    }
    users.insert_one(usuario_demo)
    '''

def db_connect(MONGO_URI, db_name, col_name):
    client = MongoClient(MONGO_URI)
    database = client[db_name]
    collection = database[col_name]
    return collection

#insertar desde el web app
def db_insert_user(collection, user):
    return collection.insert_one(user)

#si query se envía vacio muestra toda la coleccion
def db_fetch_all(collection, query={}):
    return collection.find(query)
