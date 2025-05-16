# API-Residencia
Repositório para a API do squad 7 de Residência de Software II

Lembrem do gitignore na venv de vocês por favor.

Usaremos o FastAPI

--Banco de Dados--
Como fazer o banco de dados funcionar:
- Baixe o postgres 16
A versão 17 é mais instável e menos compativel com a técnologia de plpythonu que utilizamos

- Pelo StackBuilder baixe o EDB Language Pack

- Após isso será criada uma pasta edb com a Linguagem Python

- Defina o caminho da pasta do Python (dentro da edb) no PATH (/Python3.11 e /Python3.11/Scripts)

- Após isso, no banco de dados, digite CREATE EXTENSION 'plpython3u'

- Por fim, importe o nosso arquivo para o seu banco de dados