from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import event, update
import psycopg2
from sqlalchemy.engine import Connection
from psycopg2.extras import RealDictCursor
conexao = psycopg2.connect(database = "sq07_db", host = "191.195.32.239", user = "squad07", password = "itpSquad07" , port = "5432")

def get_acao_by_id(acao_id: int):
    # Retorna uma única ação pelo seu acao_id.

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
@event.listens_for(cs_actions, "after_insert")
def  after_insert_hook(mapper, connection: Connection, target):
    acao_id = target.acao_id
    try:
        acao = get_acao_by_id(acao_id)
        print("Ação inserida:", acao)
    except HTTPException as e:
        print("Erro ao buscar ação após insert:", str(e.detail))


##mapper: mapeador do sqlalchemy, nesse caso pegaria o parametro cs_actions
##connection, conexão com o banco de dados
##target: instancia da classe do modelo
