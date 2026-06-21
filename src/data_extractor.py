# Extrator de Dados para Automação de Triagem de Notas Fiscais

# Este arquivo centraliza as funções responsáveis por extrair informações

# relevantes de uma nota fiscal a partir do texto obtido pelo OCR.

# Autor: Sandro Ferreira

import re

def extrair_cnpj(texto):
padrao = r"\d{2}.\d{3}.\d{3}/\d{4}-\d{2}"
resultado = re.search(padrao, texto)
return resultado.group(0) if resultado else None

def extrair_valor_total(texto):
padrao = r"R$\s?\d{1,3}(?:.\d{3})*,\d{2}"
resultado = re.search(padrao, texto)
return resultado.group(0) if resultado else None

def extrair_data_emissao(texto):
padrao = r"\d{2}/\d{2}/\d{4}"
resultado = re.search(padrao, texto)
return resultado.group(0) if resultado else None

def extrair_numero_nota(texto):
padrao = r"(?:NF|Nota Fiscal|Número|Numero)[:\s]*([0-9]{3,})"
resultado = re.search(padrao, texto, re.IGNORECASE)
return resultado.group(1) if resultado else None

def extrair_fornecedor(texto):
padrao = r"Fornecedor[:\s]*(.+)"
resultado = re.search(padrao, texto, re.IGNORECASE)
return resultado.group(1).strip() if resultado else None

def extrair_categoria(texto):
padrao = r"Categoria[:\s]*(.+)"
resultado = re.search(padrao, texto, re.IGNORECASE)
return resultado.group(1).strip() if resultado else "Não classificado"

def extrair_dados_nota(texto_ocr):
dados = {
"numero_nota": extrair_numero_nota(texto_ocr),
"fornecedor": extrair_fornecedor(texto_ocr),
"cnpj": extrair_cnpj(texto_ocr),
"data_emissao": extrair_data_emissao(texto_ocr),
"valor_total": extrair_valor_total(texto_ocr),
"categoria": extrair_categoria(texto_ocr)
}

```
return dados
```

if **name** == "**main**":
texto_exemplo = """
Nota Fiscal: 123456
Fornecedor: Empresa Exemplo LTDA
CNPJ: 12.345.678/0001-90
Data de Emissão: 20/06/2026
Valor Total: R$ 1.250,00
Categoria: Serviços
"""

```
dados_extraidos = extrair_dados_nota(texto_exemplo)

print("Dados extraídos:")
for campo, valor in dados_extraidos.items():
    print(f"{campo}: {valor}")
```
