from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
import traceback

# ===== Modelo de dados =====
class Sentimento(BaseModel):
    sentimento_id: int
    sentimento: str
    acao_id: int

# ===== Configuracao do banco de dados =====
DB_CONFIG = {
    "host": "191.195.32.239",
    "dbname": "sq07_db",  # nome do banco no pgAdmin
    "user": "squad07",
    "password": "itpSquad07",
    "port": 5432,
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

# ===== Insercao no banco =====
def salvar_sentimento(sentimento_id, sentimento, acao_id):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO cs_sentimentos (sentimento_id, sentimento, acao_id)
            VALUES (%s, %s, %s)
        """, (sentimento_id, sentimento, acao_id))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception:
        print("[ERRO AO INSERIR NO BANCO]")
        traceback.print_exc()
        return False

# ===== API =====
app = FastAPI()

@app.post("/sentimento")
def registrar_sentimento(dado: Sentimento):
    sucesso = salvar_sentimento(dado.sentimento_id, dado.sentimento, dado.acao_id)
    if sucesso:
        return {
            "mensagem": "Sentimento registrado com sucesso!",
            "dados": dado.dict()
        }
    else:
        raise HTTPException(status_code=500, detail="Erro ao salvar sentimento no banco.")
