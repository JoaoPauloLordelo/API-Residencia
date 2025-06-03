Repositório para a API do squad 7 de Residência de Software II

Lembrem do gitignore na venv de vocês por favor.

Usaremos o FastAPI

--Banco de Dados-- Como fazer o banco de dados funcionar:

Baixe o postgres 16 A versão 17 é mais instável e menos compativel com a técnologia de plpythonu que utilizamos

Pelo StackBuilder baixe o EDB Language Pack

Após isso será criada uma pasta edb com a Linguagem Python

Defina o caminho da pasta do Python (dentro da edb) no PATH (/Python3.11 e /Python3.11/Scripts)

Após isso, no banco de dados, digite CREATE EXTENSION 'plpython3u'

Por fim, importe o nosso arquivo para o seu banco de dados

            !! Função trigger para banco de dados SQL !!

-- 1. Criar a Função de Trigger
-- Esta função será chamada após cada inserção na tabela cs_acoes
CREATE OR REPLACE FUNCTION notificar_nova_acao_insert()
RETURNS TRIGGER AS $$
BEGIN
-- Envia o acao_id da nova linha como payload da notificação para o canal 'nova_acao_channel'.
-- O payload precisa ser uma string, então convertemos o ID para texto.
PERFORM pg_notify('nova_acao_channel', NEW.acao_id::text);

-- O valor de retorno é ignorado para triggers AFTER, mas é boa prática retornar NEW.
RETURN NEW;
END;

$$
LANGUAGE plpgsql;

-- 2. Criar o Trigger na Tabela cs_acoes
-- Este trigger acionará a função notificar_nova_acao_insert() após cada operação de INSERT.
CREATE TRIGGER trigger_cs_acoes_insert
AFTER INSERT ON cs_acoes
FOR EACH ROW
EXECUTE FUNCTION notificar_nova_acao_insert();




$$
