"""Valida os campos extraídos de uma nota fiscal."""

import re
from datetime import datetime


def validar_cnpj(cnpj):
    return bool(cnpj and re.fullmatch(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}", cnpj))


def validar_data(data):
    if not data:
        return False
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def validar_valor(valor):
    return bool(valor and re.fullmatch(r"R\$\s?\d{1,3}(?:\.\d{3})*,\d{2}", valor))


def validar_numero_nota(numero_nota):
    return bool(numero_nota and numero_nota.isdigit())


def validar_fornecedor(fornecedor):
    return bool(fornecedor and len(fornecedor.strip()) >= 3)


def validar_dados_nota(dados):
    verificacoes = [
        (validar_numero_nota(dados.get("numero_nota")), "Número da nota fiscal inválido ou não encontrado."),
        (validar_fornecedor(dados.get("fornecedor")), "Fornecedor inválido ou não encontrado."),
        (validar_cnpj(dados.get("cnpj")), "CNPJ inválido ou não encontrado."),
        (validar_data(dados.get("data_emissao")), "Data de emissão inválida ou não encontrada."),
        (validar_valor(dados.get("valor_total")), "Valor total inválido ou não encontrado."),
    ]
    erros = [mensagem for valido, mensagem in verificacoes if not valido]
    return {
        "valido": not erros,
        "status": "Processado" if not erros else "Necessita revisão manual",
        "erros": erros,
    }
