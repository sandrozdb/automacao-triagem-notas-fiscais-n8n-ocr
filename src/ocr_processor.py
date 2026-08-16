"""Lê imagens de notas fiscais com Tesseract ou fornece dados de demonstração."""

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
    _, extensao = os.path.splitext(caminho_arquivo)
    if extensao.lower() not in {".png", ".jpg", ".jpeg"}:
        raise ValueError("Formato não suportado. Use PNG, JPG ou JPEG.")


def extrair_texto_imagem(caminho_imagem, idioma="por"):
    if pytesseract is None or Image is None:
        raise RuntimeError("Instale pytesseract e Pillow para utilizar o OCR.")
    validar_arquivo(caminho_imagem)
    with Image.open(caminho_imagem) as imagem:
        return pytesseract.image_to_string(imagem, lang=idioma)


def simular_texto_ocr():
    return """Nota Fiscal: 123456
Fornecedor: Empresa Exemplo LTDA
CNPJ: 12.345.678/0001-90
Data de Emissão: 20/06/2026
Valor Total: R$ 1.250,00
Categoria: Serviços
"""


if __name__ == "__main__":
    print(simular_texto_ocr())
