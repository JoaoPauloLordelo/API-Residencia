from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import event, update
@event.listens_for(cs_actions, "after_insert")
#after_insert_hook(mapper, connection: Connection, target):
    #try:
        #resultado = analisar_mensagem(target.descricao)

        #stmt = (
            #update(CsActions)
            #.where(CsActions.acao_id == target.acao_id)
            #.values(sentimento=resultado)
       # )
        #connection.execute(stmt)

   # except Exception as e:
       # print(f"Erro no hook: {str(e)}")

#obs: função não será utilizada, esperando um metodo get pra modificar, cs_actions é referente ao modelo no banco postgres, nome pode ser mudado.