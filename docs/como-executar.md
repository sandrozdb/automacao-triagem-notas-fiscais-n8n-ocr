# ▶️ Como Executar o Projeto

## 📌 Visão Geral

Este documento explica como o projeto de Automação de Triagem de Notas Fiscais com n8n e OCR pode ser executado em ambiente local para fins de estudo, demonstração e validação do fluxo.

O projeto possui uma estrutura conceitual e prática, simulando a extração de informações de uma nota fiscal a partir de um texto obtido por OCR.

---

## 🧰 Pré-requisitos

Para executar ou simular o projeto, recomenda-se ter instalado:

* Python 3
* Git
* Editor de código, como Visual Studio Code
* MySQL ou outro banco de dados relacional
* n8n
* Navegador web

---

## 📁 Estrutura do Projeto

O repositório está organizado da seguinte forma:

* `README.md` — documentação principal do projeto
* `docs/` — documentação técnica e explicações do fluxo
* `workflow/` — modelo conceitual do fluxo no n8n
* `src/` — código Python para simulação do processamento
* `database/` — script SQL para criação da base de dados
* `examples/` — exemplo fictício de nota fiscal para testes

---

## 🐍 Executando o Script Python

O arquivo principal do projeto está localizado em:

`src/main.py`

Para executar o script, abra o terminal na pasta do projeto e utilize o comando:

`python src/main.py`

O script irá simular a leitura de uma nota fiscal e retornar dados estruturados, como:

* Número da nota fiscal
* CNPJ
* Data de emissão
* Valor total
* Status do processamento
* Data do processamento

---

## 🗄️ Executando o Banco de Dados

O script SQL está localizado em:

`database/schema.sql`

Esse arquivo cria uma base de dados chamada:

`triagem_notas_fiscais`

E também cria a tabela:

`notas_fiscais`

A tabela armazena informações como:

* Número da nota
* Fornecedor
* CNPJ
* Data de emissão
* Valor total
* Categoria
* Status de processamento
* Data de processamento

---

## 🔄 Fluxo Conceitual no n8n

O arquivo do fluxo está localizado em:

`workflow/fluxo-n8n.json`

Esse arquivo representa um modelo conceitual do fluxo de automação no n8n.

Etapas representadas:

1. Receber nota fiscal
2. Ler documento com OCR
3. Extrair informações
4. Tratar dados com Python
5. Validar informações
6. Salvar no banco de dados
7. Gerar registro de controle

---

## 🧪 Teste Simulado

O teste simulado utiliza os seguintes dados fictícios:

* Nota Fiscal: 123456
* Fornecedor: Empresa Exemplo LTDA
* CNPJ: 12.345.678/0001-90
* Data de Emissão: 20/06/2026
* Valor Total: R$ 1.250,00
* Categoria: Serviços

Após o processamento, o sistema deve organizar esses dados em formato estruturado para armazenamento e consulta.

---

## ✅ Resultado Esperado

Ao final da execução, espera-se que o sistema consiga:

* Ler dados simulados de uma nota fiscal
* Extrair informações importantes
* Organizar os dados em formato estruturado
* Simular o armazenamento em banco de dados
* Demonstrar o fluxo de automação documental

---

## 🚀 Observação

Este projeto é uma versão acadêmica e demonstrativa. Em um ambiente real, seria possível evoluir a solução com integração direta com e-mail, OCR real aplicado a PDFs, banco de dados em produção, APIs fiscais, dashboards e validações automáticas.
