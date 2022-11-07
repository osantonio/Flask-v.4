from pymongo import MongoClient
import certifi
ca = certifi.where()

def dbconnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client['DB_BARBERIA']
    except ConnectionError:
        print('Error de conexion a la base de datos')
    return db

MONGO_URI='mongodb+srv://osantonio:Google123$@cluster0.pjudx11.mongodb.net/?retryWrites=true&w=majority'