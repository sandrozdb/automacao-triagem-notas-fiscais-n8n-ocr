"""Persistência opcional das notas fiscais em MySQL."""

import os
from datetime import datetime
from decimal import Decimal

try:
    import mysql.connector
except ImportError:
    mysql = None


def obter_configuracao_banco():
    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", "3306")),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", ""),
        "database": os.getenv("DB_NAME", "triagem_notas_fiscais"),
    }


def conectar_banco():
    if mysql is None:
        return None
    return mysql.connector.connect(**obter_configuracao_banco())


def _converter_data(valor):
    return datetime.strptime(valor, "%d/%m/%Y").date() if isinstance(valor, str) else valor


def _converter_valor(valor):
    if not isinstance(valor, str):
        return valor
    normalizado = valor.replace("R$", "").strip().replace(".", "").replace(",", ".")
    return Decimal(normalizado)


def salvar_nota_fiscal(dados):
    conexao = conectar_banco()
    if conexao is None:
        print("Modo demonstração: configure o MySQL para persistir os dados.")
        return False
    query = """INSERT INTO notas_fiscais
        (numero_nota, fornecedor, cnpj, data_emissao, valor_total, categoria, status_processamento)
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    valores = (
        dados.get("numero_nota"), dados.get("fornecedor"), dados.get("cnpj"),
        _converter_data(dados.get("data_emissao")), _converter_valor(dados.get("valor_total")),
        dados.get("categoria"), dados.get("status"),
    )
    try:
        with conexao.cursor() as cursor:
            cursor.execute(query, valores)
        conexao.commit()
        return True
    finally:
        conexao.close()
