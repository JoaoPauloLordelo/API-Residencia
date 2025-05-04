from fastapi import FastAPI
import psycopg2

#uvicorn main:app --host 127.0.0.1 --port 8000

app = FastAPI()

conn = psycopg2.connect(
    dbname="teste",
    user="postgres",
    password="JPV0510!",
    host="localhost",
    port="5432"
)

@app.get("/")
def hello():
    cur = conn.cursor()
    cur.execute("SELECT descricao FROM cs_acoes;")
    msg = cur.fetchall()
    cur.close()
@app.post("/")
def enviar():
    return {}