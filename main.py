from fastapi import FastAPI, HTTPException
import psycopg2
from medolo import analisadorSentimento
from time import sleep
#uvicorn main:app --host 127.0.0.1 --port 8008

app = FastAPI()

conn = psycopg2.connect(
    dbname="teste02",
    user="postgres",
    password="JPV0510!",
    host="localhost",
    port="5432"
)

def salvar_sentimento(sentimento :str, acao_id:int):
    try:
        print('Fase 1:ok')
        cur = conn.cursor()
        print('Fase 2:ok')
        cur.execute("INSERT INTO cs_sentimentos (sentimento, acao_id) VALUES (%s, %s);",(sentimento,acao_id))
        conn.commit()
        print('Fase 3:ok')
        cur.close()
        print("Deu bom")
        return "Deu certo"
    except Exception as e:
        conn.rollback()
        print(sentimento)
        print(type(sentimento))
        print(acao_id)
        print(type(acao_id))
        print("ERROR")
        print(e)
        return "[ERRO AO INSERIR NO BANCO]"
@app.get('/')
def teste():
    return "oi"
@app.post("/msg")
def  after_insert_hook(json: dict):
    try:
        
        # cur = conn.cursor()
        # cur.execute("SELECT descricao,acao_id FROM cs_acoes ORDER BY acao_id DESC LIMIT 1;")
        # msg = cur.fetchone()
        # cur.close()\
        # r = analisadorSentimento(msg) #--Analisa o sentimento ( Temporariamente desativado para deixar mais leve)
        print("Ateagr tudo certo")
        return salvar_sentimento(json['message'][0],json['message'][1])
    except HTTPException:
         print("Deu ruim chefia")
         return "Erro ao conectar com o banco"
