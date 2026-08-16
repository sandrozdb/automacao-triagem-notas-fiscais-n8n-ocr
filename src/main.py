"""Executa o pipeline demonstrativo de triagem de notas fiscais."""

from data_extractor import extrair_dados_nota
from database import salvar_nota_fiscal
from ocr_processor import simular_texto_ocr
from validator import validar_dados_nota


def processar_nota_fiscal(texto_ocr, persistir=False):
    dados = extrair_dados_nota(texto_ocr)
    validacao = validar_dados_nota(dados)
    dados["status"] = validacao["status"]
    if persistir and validacao["valido"]:
        salvar_nota_fiscal(dados)
    return {"dados": dados, "validacao": validacao}


if __name__ == "__main__":
    resultado = processar_nota_fiscal(simular_texto_ocr())
    print("Dados extraídos:")
    for chave, valor in resultado["dados"].items():
        print(f"- {chave}: {valor}")
    print(f"Validação: {resultado['validacao']}")
