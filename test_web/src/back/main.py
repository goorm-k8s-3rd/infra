from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import os

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_address = os.getenv('DB_ADDRESS')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_password = os.getenv('DB_PASSWORD')
db_dbname = os.getenv('DB_DBNAME')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
def read_users():
    mydb = mysql.connector.connect(
        host=db_address,
        port=db_port,
        user=db_name,
        password=db_password,
        database=db_dbname,
        charset='utf8'
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return result
