# Microsserviço Backend API Externa
=====================================

## Introdução
---------------

Este é um microsserviço backend que fornece informações sobre CEPs. Este README.md irá guiar você passo a passo para executar a aplicação.

## Requisitos
--------------

* Docker instalado na máquina local

## Passos para Executar a Aplicação
-----------------------------------

### 1. Construir a Imagem

Execute o comando `docker build -t minha-api-externa .` para construir a imagem da aplicação.

### 2. Verificar Vulnerabilidades de Segurança

Execute o comando `docker scout quickview` para verificar vulnerabilidades de segurança na imagem.

### 3. Executar o Container

Execute o comando `docker run -p 8080:8080 minha-api-externa` para executar um container a partir da imagem.

### 4. Acessar a API

Acesse a API através da porta 8080 do seu host, por exemplo, `http://localhost:8080`.

## Parar ou Remover o Container
--------------------------------

Para parar o container, execute o comando `docker stop meu-container`. Para remover o container, execute o comando `docker rm meu-container`.

## Observações
--------------

* Lembre-se de substituir `minha-api-externa` pelo nome real da sua imagem.
* Lembre-se de substituir `meu-container` pelo nome real do seu container.
