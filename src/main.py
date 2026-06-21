# Automação de Triagem de Notas Fiscais com OCR e n8n

# Este arquivo simula o processamento inicial de uma nota fiscal,

# extraindo informações básicas a partir de um texto obtido por OCR.

# Autor: Sandro Ferreira

import re
from datetime import datetime

def extrair_cnpj(texto):
padrao = r"\d{2}.\d{3}.\d{3}/\d{4}-\d{2}"
resultado = re.search(padrao, texto)
return resultado.group(0) if resultado else None

def extrair_valor_total(texto):
padrao = r"R$\s?\d{1,3}(?:.\d{3})*,\d{2}"
resultado = re.search(padrao, texto)
return resultado.group(0) if resultado else None

def extrair_data(texto):
padrao = r"\d{2}/\d{2}/\d{4}"
resultado = re.search(padrao, texto)
return resultado.group(0) if resultado else None

def extrair_numero_nota(texto):
padrao = r"(?:NF|Nota Fiscal|Número)[:\s]*([0-9]{3,})"
resultado = re.search(padrao, texto, re.IGNORECASE)
return resultado.group(1) if resultado else None

def processar_nota_fiscal(texto_ocr):
dados = {
"numero_nota": extrair_numero_nota(texto_ocr),
"cnpj": extrair_cnpj(texto_ocr),
"data_emissao": extrair_data(texto_ocr),
"valor_total": extrair_valor_total(texto_ocr),
"status": "Processado",
"data_processamento": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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
"""

```
resultado = processar_nota_fiscal(texto_exemplo)

print("Dados extraídos da nota fiscal:")
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")
```
