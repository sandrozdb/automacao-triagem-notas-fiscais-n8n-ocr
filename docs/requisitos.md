# 📋 Requisitos do Projeto — Automação de Triagem de Notas Fiscais

## 📌 Visão Geral

Este documento apresenta os principais requisitos funcionais e não funcionais do projeto de Automação de Triagem de Notas Fiscais com n8n e OCR.

Os requisitos foram definidos com base na necessidade de automatizar a leitura, extração, validação e armazenamento de informações contidas em notas fiscais.

---

## 🎯 Objetivo dos Requisitos

Definir as funcionalidades esperadas do sistema, os critérios de funcionamento e as características técnicas necessárias para que a solução seja eficiente, segura, organizada e escalável.

---

## ✅ Requisitos Funcionais

### RF01 — Receber notas fiscais

O sistema deve permitir o recebimento de notas fiscais em formato PDF ou imagem.

### RF02 — Realizar leitura via OCR

O sistema deve ser capaz de realizar a leitura do documento utilizando OCR para extrair texto de arquivos digitais.

### RF03 — Extrair informações principais

O sistema deve identificar e extrair informações relevantes da nota fiscal, como:

* Número da nota fiscal
* CNPJ
* Fornecedor
* Data de emissão
* Valor total
* Categoria do documento

### RF04 — Tratar os dados extraídos

O sistema deve tratar os dados extraídos, removendo inconsistências, espaços desnecessários e formatando as informações de maneira padronizada.

### RF05 — Validar informações obrigatórias

O sistema deve verificar se os campos obrigatórios foram encontrados corretamente antes de armazenar os dados.

### RF06 — Automatizar o fluxo com n8n

O sistema deve utilizar o n8n para organizar e executar as etapas do processo automatizado.

### RF07 — Armazenar os dados em banco de dados

O sistema deve registrar os dados extraídos em uma base de dados estruturada.

### RF08 — Registrar status do processamento

O sistema deve registrar se a nota fiscal foi processada com sucesso ou se apresentou alguma inconsistência.

### RF09 — Permitir consulta posterior

O sistema deve permitir que as informações armazenadas sejam consultadas posteriormente para controle, análise ou auditoria.

### RF10 — Possibilitar geração de relatórios

O sistema deve permitir futura integração com relatórios ou dashboards para acompanhamento dos dados processados.

---

## ⚙️ Requisitos Não Funcionais

### RNF01 — Eficiência

O sistema deve reduzir o tempo gasto no processo manual de triagem de notas fiscais.

### RNF02 — Confiabilidade

O sistema deve minimizar erros de digitação e falhas humanas no processamento das informações.

### RNF03 — Organização

Os dados processados devem ser armazenados de forma estruturada e padronizada.

### RNF04 — Escalabilidade

A solução deve permitir futura expansão para processamento de maior volume de documentos.

### RNF05 — Manutenibilidade

O projeto deve possuir uma estrutura organizada, facilitando futuras melhorias e manutenção.

### RNF06 — Segurança

A solução deve considerar boas práticas de segurança da informação para proteção de dados fiscais e empresariais.

### RNF07 — Integração

O sistema deve permitir integração futura com e-mail, ERP, APIs, banco de dados e dashboards.

### RNF08 — Usabilidade

O fluxo deve ser simples de compreender e operar, facilitando sua adoção em ambientes administrativos.

---

## 🧪 Regras de Validação

O sistema deve considerar uma nota fiscal válida quando:

* O número da nota for identificado
* O CNPJ for encontrado
* A data de emissão estiver presente
* O valor total for extraído
* O status do processamento for registrado

Caso algum dado obrigatório não seja identificado, a nota pode ser marcada como:

* Pendente
* Incompleta
* Necessita revisão manual

---

## 📊 Critérios de Sucesso

O projeto será considerado bem-sucedido quando conseguir demonstrar:

* Leitura automatizada de informações fiscais
* Extração de dados relevantes
* Organização dos dados em formato estruturado
* Redução de etapas manuais
* Possibilidade de integração com sistemas externos
* Documentação clara do processo e da arquitetura

---

## 🚀 Melhorias Futuras Relacionadas aos Requisitos

* Integração com Gmail
* Integração com Google Drive
* Integração com sistemas ERP
* Validação automática de CNPJ
* Dashboard em Power BI
* Classificação automática de notas fiscais
* Alertas para inconsistências
* Uso de Inteligência Artificial para interpretação documental
