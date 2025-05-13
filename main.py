from fastapi import FastAPI, HTTPException
from sqlalchemy import event, update
import psycopg2
from sqlalchemy.engine import Connection
from medolo import analisadorSentimento
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey,String,TIMESTAMP
#uvicorn main:app --host 127.0.0.1 --port 8000

app = FastAPI()

conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="",
    port=""
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
        conn.close()
        return "Deu certo"
    except Exception:
        return "[ERRO AO INSERIR NO BANCO]"
    
def verificar_funcoes():
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM pg_proc WHERE proname = 'notify_cs_acoes';")
    func_exists = cur.fetchone() is not None

    cur.execute("""
        SELECT 1
        FROM information_schema.triggers
        WHERE event_object_table = 'cs_acoes'
          AND trigger_name = 'trg_cs_acoes_notify';
    """)
    trigger_exists = cur.fetchone() is not None
    if func_exists and trigger_exists == True:
        return True
    else:
        return False
    
def criarTrigger():
    cur = conn.cursor()

@app.get("/")
def  after_insert_hook():
    try:
        # cur = conn.cursor()
        # cur.execute("SELECT descricao,acao_id FROM cs_acoes ORDER BY acao_id DESC LIMIT 1;")
        # msg = cur.fetchall()
        # cur.close()
        # # r = analisadorSentimento(msg) #--Analisa o sentimento ( Temporariamente desativado para deixar mais leve)
        # salvar_sentimento(msg[0],msg[1])
        # return True
        if verificar_funcoes() == True:
            return "Deu merda"
        else:
            return "Deu bom"
    
    except HTTPException:
         return "Erro ao conectar com o banco"
 

