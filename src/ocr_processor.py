# Processador OCR para Automação de Triagem de Notas Fiscais

# Este arquivo representa a etapa responsável por ler documentos fiscais

# em imagem ou PDF e transformar o conteúdo em texto processável.

# Autor: Sandro Ferreira

import os

try:
import pytesseract
from PIL import Image
except ImportError:
pytesseract = None
Image = None

def validar_arquivo(caminho_arquivo):
if not os.path.exists(caminho_arquivo):
raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

```
extensoes_permitidas = [".png", ".jpg", ".jpeg", ".pdf"]

_, extensao = os.path.splitext(caminho_arquivo)

if extensao.lower() not in extensoes_permitidas:
    raise ValueError("Formato de arquivo não suportado para OCR.")

return True
```

def extrair_texto_imagem(caminho_imagem, idioma="por"):
if pytesseract is None or Image is None:
return "Bibliotecas de OCR não instaladas. Instale pytesseract e pillow."

```
validar_arquivo(caminho_imagem)

imagem = Image.open(caminho_imagem)
texto_extraido = pytesseract.image_to_string(imagem, lang=idioma)

return texto_extraido
```

def simular_texto_ocr():
texto_simulado = """
Nota Fiscal: 123456
Fornecedor: Empresa Exemplo LTDA
CNPJ: 12.345.678/0001-90
Data de Emissão: 20/06/2026
Valor Total: R$ 1.250,00
Categoria: Serviços
"""

```
return texto_simulado
```

if **name** == "**main**":
print("Simulação de texto extraído por OCR:")
print(simular_texto_ocr())
