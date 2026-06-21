CREATE DATABASE IF NOT EXISTS triagem_notas_fiscais;

USE triagem_notas_fiscais;

CREATE TABLE IF NOT EXISTS notas_fiscais (
id INT AUTO_INCREMENT PRIMARY KEY,
numero_nota VARCHAR(50),
fornecedor VARCHAR(255),
cnpj VARCHAR(20),
data_emissao DATE,
valor_total DECIMAL(10, 2),
categoria VARCHAR(100),
status_processamento VARCHAR(50),
data_processamento TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO notas_fiscais (
numero_nota,
fornecedor,
cnpj,
data_emissao,
valor_total,
categoria,
status_processamento
) VALUES (
'123456',
'Empresa Exemplo LTDA',
'12.345.678/0001-90',
'2026-06-20',
1250.00,
'Serviços',
'Processado'
);

SELECT * FROM notas_fiscais;
