# 🧾 Exemplo de Nota Fiscal para Testes

## 📌 Objetivo

Este arquivo apresenta um exemplo fictício de nota fiscal utilizado para demonstrar o funcionamento do processo de extração de dados via OCR.

O objetivo é mostrar como uma nota fiscal pode ser lida, interpretada e transformada em dados estruturados para posterior armazenamento em banco de dados.

---

## 📄 Dados Simulados da Nota Fiscal

**Nota Fiscal:** 123456

**Fornecedor:** Empresa Exemplo LTDA

**CNPJ:** 12.345.678/0001-90

**Data de Emissão:** 20/06/2026

**Valor Total:** R$ 1.250,00

**Categoria:** Serviços

---

## 📊 Dados Esperados Após o Processamento

| Campo           | Valor                |
| --------------- | -------------------- |
| Número da Nota  | 123456               |
| Fornecedor      | Empresa Exemplo LTDA |
| CNPJ            | 12.345.678/0001-90   |
| Data de Emissão | 20/06/2026           |
| Valor Total     | R$ 1.250,00          |
| Categoria       | Serviços             |
| Status          | Processado           |

---

## 🔄 Como esses dados seriam tratados

1. A nota fiscal é recebida em formato PDF ou imagem.
2. O OCR realiza a leitura do documento.
3. O texto extraído é processado.
4. O Python identifica campos como CNPJ, data, valor e número da nota.
5. O n8n organiza o fluxo automatizado.
6. Os dados são armazenados no banco de dados.
7. As informações ficam disponíveis para consulta e controle.

---

## ✅ Resultado Esperado

Após o processamento, a nota fiscal deixa de ser apenas um documento visual e passa a ser um conjunto de dados organizados, facilitando consultas, relatórios, auditorias e integrações com outros sistemas.
