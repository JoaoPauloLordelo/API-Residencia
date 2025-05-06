from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import event, update, text
import psycopg2
from sqlalchemy.engine import Connection
from psycopg2.extras import RealDictCursor


@event.listens_for(cs_actions, "after_insert")
def after_insert_hook(mapper, connection, target):
    acao_id = target.acao_id
    try:

        resultado = connection.execute(
            text("SELECT acao_id, descricao FROM cs_acoes WHERE acao_id = :acao_id"),
            {"acao_id": acao_id}
        ).fetchone()

        if resultado:
            print("Ação inserida:", dict(resultado))
        else:
            print(f"[Aviso] Ação ID {acao_id} não encontrada após inserção.")
    except Exception as e:
        print(f"[Erro] Falha ao buscar ação {acao_id}: {str(e)}")

##Essa versão é utilizada em caso de conexão direta com o próprio sqlalchemy, evitando erros e conflitos com a conexão da outra versão do hook.



#obs: função não será utilizada, esperando um metodo get pra modificar, cs_actions é referente ao modelo no banco postgres, nome pode ser mudado.
##mapper: mapeador do sqlalchemy, nesse caso pegaria o parametro cs_actions
##connection, conexão com o banco de dados
##target: instancia da classe do modelo