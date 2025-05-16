from fastapi import FastAPI, HTTPException
import psycopg2
from medolo import analisadorSentimento
#uvicorn main:app --host 127.0.0.1 --port 8000

app = FastAPI()

conn = psycopg2.connect(
    dbname="teste02",
    user="postgres",
    password="JPV0510!",
    host="localhost",
    port="5432"
)

def salvar_sentimento(sentimento, acao_id):
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO cs_sentimentos (sentimento, acao_id)
            VALUES (%s, %s)
        """, (sentimento, acao_id))
        conn.commit()
        cur.close()
        return "Deu certo"
    except Exception:
        return "[ERRO AO INSERIR NO BANCO]"
    
@app.get("/")
def  after_insert_hook():
    try:
        cur = conn.cursor()
        cur.execute("SELECT descricao,acao_id FROM cs_acoes ORDER BY acao_id DESC LIMIT 1;")
        msg = cur.fetchone()
        # r = analisadorSentimento(msg) #--Analisa o sentimento ( Temporariamente desativado para deixar mais leve)
        cur.close()
        return salvar_sentimento(msg[0],msg[1])
    except HTTPException:
         return "Erro ao conectar com o banco"
 

