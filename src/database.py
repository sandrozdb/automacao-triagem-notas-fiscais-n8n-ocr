# Módulo de Banco de Dados para Automação de Triagem de Notas Fiscais

# Este arquivo representa a etapa de armazenamento dos dados extraídos.

# Autor: Sandro Ferreira

import os

try:
import mysql.connector
except ImportError:
mysql = None

def obter_configuracao_banco():
config = {
"host": os.getenv("DB_HOST", "localhost"),
"port": os.getenv("DB_PORT", "3306"),
"user": os.getenv("DB_USER", "root"),
"password": os.getenv("DB_PASSWORD", ""),
"database": os.getenv("DB_NAME", "triagem_notas_fiscais")
}

```
return config
```

def conectar_banco():
if mysql is None:
print("Biblioteca mysql-connector-python não instalada.")
return None

```
config = obter_configuracao_banco()

try:
    conexao = mysql.connector.connect(
        host=config["host"],
        port=config["port"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

    return conexao

except Exception as erro:
    print(f"Erro ao conectar ao banco de dados: {erro}")
    return None
```

def salvar_nota_fiscal(dados):
conexao = conectar_banco()

```
if conexao is None:
    print("Modo simulação: dados não foram salvos no banco.")
    print(dados)
    return False

try:
    cursor = conexao.cursor()

    query = """
    INSERT INTO notas_fiscais (
        numero_nota,
        fornecedor,
        cnpj,
        data_emissao,
        valor_total,
        categoria,
        status_processamento
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        dados.get("numero_nota"),
        dados.get("fornecedor"),
        dados.get("cnpj"),
        dados.get("data_emissao"),
        dados.get("valor_total"),
        dados.get("categoria"),
        dados.get("status")
    )

    cursor.execute(query, valores)
    conexao.commit()

    print("Nota fiscal salva com sucesso no banco de dados.")

    cursor.close()
    conexao.close()

    return True

except Exception as erro:
    print(f"Erro ao salvar nota fiscal: {erro}")
    return False
```

if **name** == "**main**":
nota_exemplo = {
"numero_nota": "123456",
"fornecedor": "Empresa Exemplo LTDA",
"cnpj": "12.345.678/0001-90",
"data_emissao": "2026-06-20",
"valor_total": 1250.00,
"categoria": "Serviços",
"status": "Processado"
}

```
salvar_nota_fiscal(nota_exemplo)
```
