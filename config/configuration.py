import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

#DBURL = os.getenv("URL")

#Vamos a conectar con la base de datos de mongo en local
#if not (DBURL):
 #   raise ValueError("Tienes que especificar una URL pls")


conn = MongoClient("localhost:27017")
db = conn.get_database("office")
