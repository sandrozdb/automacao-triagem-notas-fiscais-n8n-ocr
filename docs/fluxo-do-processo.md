# 🔄 Fluxo do Processo — Automação de Triagem de Notas Fiscais

## 📌 Visão Geral

Este documento apresenta o fluxo do processo desenvolvido para a automação de triagem de notas fiscais utilizando n8n, OCR, Python e banco de dados.

O objetivo do fluxo é reduzir atividades manuais, organizar informações fiscais e automatizar etapas repetitivas do processo documental, tornando o processo mais eficiente, padronizado e menos sujeito a erros humanos.

---

## 🧾 Processo Manual — AS-IS

No processo manual, a triagem de notas fiscais depende da atuação humana em várias etapas. Esse modelo pode gerar atrasos, erros de digitação, retrabalho e dificuldade no controle das informações.

```text
┌──────────────────────────────┐
│ Receber nota fiscal          │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ Abrir documento manualmente  │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ Conferir dados da nota       │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ Digitar informações          │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ Organizar em planilha/sistema│
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ Gerar controle manual        │
└──────────────────────────────┘
```

---

## 🚀 Processo Automatizado — TO-BE

No processo automatizado, a solução utiliza OCR para leitura dos documentos, Python para tratamento dos dados, n8n para orquestração do fluxo e banco de dados para armazenamento estruturado.

```text
┌──────────────────────────────┐
│ Entrada da nota fiscal       │
│ PDF ou imagem                │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ Leitura com OCR              │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ Extração dos dados           │
│ CNPJ, valor, data, número    │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ Tratamento com Python        │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ Automação do fluxo no n8n    │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ Armazenamento no banco       │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│ Consulta e controle          │
└──────────────────────────────┘
```

---

## 📊 Dados Tratados

A automação pode processar informações como:

* Número da nota fiscal
* Data de emissão
* Nome do fornecedor
* CNPJ
* Valor total
* Categoria da nota
* Status de processamento
* Data de registro no sistema

---

## ✅ Benefícios Esperados

* Redução de erros manuais
* Aumento da produtividade
* Agilidade na triagem documental
* Padronização dos dados
* Melhor controle das informações fiscais
* Possibilidade de integração com sistemas financeiros
* Apoio à tomada de decisão

---

## 🔮 Melhorias Futuras

* Integração com Gmail ou e-mail corporativo
* Validação automática de CNPJ
* Integração com ERP
* Dashboard em Power BI
* Classificação automática por tipo de documento
* Uso de IA para interpretação de documentos fiscais
* Geração automática de relatórios
* Alertas para inconsistências nos dados
