from fastapi import FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

conexao = psycopg2.connect(database = "sq07_db", host = "191.195.32.239", user = "squad07", password = "itpSquad07" , port = "5432")

print(conexao.status) #checkando conexão, se retornar 1 deu certo 

@app.get("/") #rota, local onde deve ser colocado no site

def home():
    return " Api online"

@app.get("/acoes")
def get_all_acoes():

    #Retorna todas as ações, com acao_id e descricao.
    try:
        with conexao.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT acao_id, descricao FROM cs_acoes;")
            resultados = cur.fetchall()
        return resultados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/acoes/{acao_id}")
def get_acao_by_id(acao_id: int):

    #Retorna uma única ação pelo seu acao_id.
 
    try:
        with conexao.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT acao_id, descricao FROM cs_acoes WHERE acao_id = %s;",
                (acao_id,)
            )
            resultado = cur.fetchone()
        if not resultado:
            raise HTTPException(status_code=404, detail="Ação não encontrada")
        return resultado
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))