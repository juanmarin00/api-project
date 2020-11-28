import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()
print("pollaaaaaa!!!\n\n\n")

DBURL = os.getenv("DBURL")
print(DBURL)
#vamos a conectar mogno en local

if not (DBURL):
    raise ValueError("Tienes que especificar una url pls")

client = MongoClient(DBURL)
db = client.get_database()
collection = db["frases"]


