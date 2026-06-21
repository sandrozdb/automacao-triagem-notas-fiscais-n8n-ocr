# 📄 Automação de Triagem de Notas Fiscais com n8n e OCR

## 📌 Sobre o Projeto

Este projeto apresenta o desenvolvimento de uma solução de automação para triagem, leitura, extração e processamento de informações contidas em notas fiscais utilizando OCR, n8n, Python e banco de dados.

A proposta do sistema é automatizar etapas manuais do processo de conferência documental, reduzindo o tempo operacional, minimizando erros humanos e aumentando a eficiência no tratamento de documentos fiscais.

O projeto foi desenvolvido no contexto acadêmico da UniFECAF, aplicando conceitos de automação de processos, transformação digital, integração de sistemas, tratamento de dados e organização de informações.

---

## 🎯 Objetivos

* Automatizar a triagem de notas fiscais.
* Realizar leitura de documentos utilizando OCR.
* Extrair informações relevantes de arquivos PDF ou imagens.
* Organizar os dados extraídos de forma estruturada.
* Reduzir atividades manuais e repetitivas.
* Minimizar erros no processamento de documentos.
* Integrar ferramentas de automação com banco de dados.
* Demonstrar uma aplicação prática de RPA e transformação digital.

---

## 🧠 Problema Identificado

Em muitos processos administrativos e financeiros, a conferência de notas fiscais ainda é realizada manualmente. Esse processo pode gerar atrasos, retrabalho, erros de digitação e dificuldade no controle das informações.

A ausência de automação torna a operação menos eficiente, principalmente quando há grande volume de documentos a serem analisados.

---

## 💡 Solução Proposta

A solução proposta utiliza automação de processos para receber, interpretar, extrair e organizar dados de notas fiscais.

O fluxo combina OCR para leitura dos documentos, n8n para orquestração da automação, Python para tratamento dos dados e banco de dados para armazenamento das informações processadas.

---

## ⚙️ Tecnologias Utilizadas

* n8n
* OCR
* Python
* Banco de Dados
* SQL
* Automação de Processos
* RPA
* Integração de Sistemas
* Git e GitHub

---

## 🔄 Fluxo da Automação

```text
Recebimento da Nota Fiscal
            ↓
Leitura do Documento
            ↓
Processamento com OCR
            ↓
Extração dos Dados
            ↓
Tratamento das Informações
            ↓
Automação com n8n
            ↓
Armazenamento em Banco de Dados
            ↓
Consulta, Controle e Relatórios
```

---

## 🏗️ Arquitetura da Solução

```text
┌──────────────────────────────┐
│      Entrada da Nota Fiscal  │
│      PDF ou Imagem           │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│      OCR                     │
│      Leitura do Documento    │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│      Python                  │
│      Tratamento dos Dados    │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│      n8n                     │
│      Orquestração do Fluxo   │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│      Banco de Dados          │
│      Armazenamento           │
└───────────────┬──────────────┘
                ↓
┌──────────────────────────────┐
│      Relatórios e Controle   │
└──────────────────────────────┘
```

---

## 📊 Dados Extraídos

O sistema pode ser utilizado para extrair informações como:

* Número da nota fiscal
* Data de emissão
* Nome do fornecedor
* CNPJ
* Valor total
* Descrição dos itens
* Status da nota
* Categoria do documento

---

## ✅ Benefícios do Projeto

* Redução de erros manuais
* Aumento da produtividade
* Padronização do processamento documental
* Melhor organização das informações
* Agilidade na conferência de notas fiscais
* Apoio à tomada de decisão
* Maior controle operacional
* Possibilidade de expansão para outros documentos

---

## 📂 Estrutura Sugerida do Repositório

```text
automacao-triagem-notas-fiscais-n8n-ocr/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   ├── diagramas/
│   ├── prints/
│   └── relatorio-tecnico.pdf
│
├── workflow/
│   └── fluxo-n8n.json
│
├── src/
│   ├── main.py
│   ├── ocr_processor.py
│   └── database.py
│
├── database/
│   └── schema.sql
│
└── examples/
    └── nota-fiscal-exemplo.pdf
```

---

## 🧪 Etapas do Desenvolvimento

### 1. Mapeamento do Processo Manual

Foi analisado o processo atual de triagem de notas fiscais, identificando atividades repetitivas, pontos de erro e oportunidades de automação.

### 2. Definição do Fluxo Automatizado

Foi proposto um fluxo automatizado para leitura, extração, tratamento e armazenamento dos dados.

### 3. Implementação do OCR

O OCR foi utilizado para transformar informações presentes em imagens ou PDFs em texto editável e processável.

### 4. Tratamento dos Dados

Com Python, os dados extraídos podem ser tratados, organizados e preparados para armazenamento.

### 5. Automação com n8n

O n8n foi utilizado para orquestrar o fluxo, conectando etapas como entrada do documento, processamento, validação e saída dos dados.

### 6. Armazenamento das Informações

Os dados processados são direcionados para armazenamento estruturado, permitindo consulta e controle posterior.

---

## 🚀 Possíveis Melhorias Futuras

* Integração com e-mail corporativo
* Validação automática de CNPJ
* Integração com sistemas ERP
* Dashboard em Power BI
* Classificação automática por tipo de nota
* Alertas automáticos para notas inconsistentes
* Uso de IA para interpretação documental
* Auditoria automática de documentos fiscais

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados conhecimentos de:

* Automação de processos
* OCR
* RPA
* Python
* Banco de Dados
* Integração de sistemas
* Modelagem de fluxo
* Documentação técnica
* Transformação digital
* Análise de processos administrativos

---

## 👨‍💻 Autor

**Sandro Ferreira**

Estudante de Engenharia da Computação
Estudante de Inteligência Artificial e Automação Digital

📧 E-mail: [sandrozdb@gmail.com](mailto:sandrozdb@gmail.com)
💼 LinkedIn: https://linkedin.com/in/sandrozdb
🐙 GitHub: https://github.com/sandrozdb
