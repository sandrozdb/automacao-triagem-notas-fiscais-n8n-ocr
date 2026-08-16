"""Extrai campos estruturados do texto obtido por OCR."""

import re


def _buscar(padrao, texto, grupo=0, flags=0):
    resultado = re.search(padrao, texto, flags)
    return resultado.group(grupo).strip() if resultado else None


def extrair_cnpj(texto):
    return _buscar(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}", texto)


def extrair_valor_total(texto):
    return _buscar(r"R\$\s?\d{1,3}(?:\.\d{3})*,\d{2}", texto)


def extrair_data_emissao(texto):
    return _buscar(r"\d{2}/\d{2}/\d{4}", texto)


def extrair_numero_nota(texto):
    return _buscar(
        r"(?:NF|Nota Fiscal|Número|Numero)[:\s]*([0-9]{3,})",
        texto,
        grupo=1,
        flags=re.IGNORECASE,
    )


def extrair_fornecedor(texto):
    return _buscar(r"Fornecedor[:\s]*([^\r\n]+)", texto, grupo=1, flags=re.IGNORECASE)


def extrair_categoria(texto):
    return _buscar(r"Categoria[:\s]*([^\r\n]+)", texto, grupo=1, flags=re.IGNORECASE) or "Não classificado"


def extrair_dados_nota(texto_ocr):
    return {
        "numero_nota": extrair_numero_nota(texto_ocr),
        "fornecedor": extrair_fornecedor(texto_ocr),
        "cnpj": extrair_cnpj(texto_ocr),
        "data_emissao": extrair_data_emissao(texto_ocr),
        "valor_total": extrair_valor_total(texto_ocr),
        "categoria": extrair_categoria(texto_ocr),
    }


if __name__ == "__main__":
    from ocr_processor import simular_texto_ocr

    for campo, valor in extrair_dados_nota(simular_texto_ocr()).items():
        print(f"{campo}: {valor}")
