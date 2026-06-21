# Validador de Dados para Automação de Triagem de Notas Fiscais

# Este arquivo valida as informações extraídas da nota fiscal.

# Autor: Sandro Ferreira

import re
from datetime import datetime

def validar_cnpj(cnpj):
if not cnpj:
return False

```
padrao = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
return bool(re.match(padrao, cnpj))
```

def validar_data(data):
if not data:
return False

```
try:
    datetime.strptime(data, "%d/%m/%Y")
    return True
except ValueError:
    return False
```

def validar_valor(valor):
if not valor:
return False

```
padrao = r"^R\$\s?\d{1,3}(?:\.\d{3})*,\d{2}$"
return bool(re.match(padrao, valor))
```

def validar_numero_nota(numero_nota):
if not numero_nota:
return False

```
return numero_nota.isdigit()
```

def validar_fornecedor(fornecedor):
if not fornecedor:
return False

```
return len(fornecedor.strip()) >= 3
```

def validar_dados_nota(dados):
erros = []

```
if not validar_numero_nota(dados.get("numero_nota")):
    erros.append("Número da nota fiscal inválido ou não encontrado.")

if not validar_fornecedor(dados.get("fornecedor")):
    erros.append("Fornecedor inválido ou não encontrado.")

if not validar_cnpj(dados.get("cnpj")):
    erros.append("CNPJ inválido ou não encontrado.")

if not validar_data(dados.get("data_emissao")):
    erros.append("Data de emissão inválida ou não encontrada.")

if not validar_valor(dados.get("valor_total")):
    erros.append("Valor total inválido ou não encontrado.")

if erros:
    return {
        "valido": False,
        "status": "Necessita revisão manual",
        "erros": erros
    }

return {
    "valido": True,
    "status": "Processado",
    "erros": []
}
```

if **name** == "**main**":
nota_exemplo = {
"numero_nota": "123456",
"fornecedor": "Empresa Exemplo LTDA",
"cnpj": "12.345.678/0001-90",
"data_emissao": "20/06/2026",
"valor_total": "R$ 1.250,00",
"categoria": "Serviços"
}

```
resultado_validacao = validar_dados_nota(nota_exemplo)

print("Resultado da validação:")
print(resultado_validacao)
```
