from fastapi import FastAPI
import psycopg2
from medolo import analisadorSentimento
#uvicorn main:app --host 127.0.0.1 --port 8000

app = FastAPI()

conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="",
    port=""
)

@app.get("/")
def hello():
    cur = conn.cursor()
    cur.execute("SELECT descricao FROM cs_acoes;")
    msg = cur.fetchall()[::-1][0][0]
    cur.close()
    r = analisadorSentimento(msg)
    return r