## Projeto: Microsserviço Backend com Flask e SQLite

Este é um projeto backend que utiliza Flask e SQLite, gerenciando rotas e operações CRUD através de métodos HTTP (GET, POST, PUT, DELETE). A aplicação pode ser executada facilmente em um contêiner Docker.

### Pré-requisitos

Antes de começar, você precisará ter os seguintes programas instalados na sua máquina:

- [Docker](https://www.docker.com/)
- [Postman](https://www.postman.com/) (opcional, para testar as rotas)

### Estrutura do Projeto

A estrutura do projeto é a seguinte:

microsservico/
│
├── backend/
│   ├── __init__.py
│   ├── models.py
│   ├── post_routes.py
│   └── usuario_routes.py
│
├── instance/
│   └── comunidade.db
│
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt


- **backend/**: Contém os arquivos principais de rotas e modelos da aplicação.
- **instance/**: Contém o banco de dados SQLite.
- **Dockerfile**: Arquivo para construir a imagem Docker.
- **main.py**: Arquivo principal que inicializa o servidor Flask e configura o banco de dados.
- **requirements.txt**: Lista de dependências Python.

### Instalação e Execução via Docker

Siga os passos abaixo para executar o projeto usando Docker.

#### Passo 1: Clonar o repositório

Clone este repositório em sua máquina:

```bash
git clone https://github.com/TatyDePaula/microsservico.git
cd microsservico-backend

Passo 2: Construir a imagem Docker

No diretório do projeto, construa a imagem Docker utilizando o Dockerfile. Execute o seguinte comando no terminal:

docker build -t microsservico .

Passo 3: Executar o contêiner
Após construir a imagem, execute o contêiner:
docker run -d -p 8000:8000 -v ${PWD}:/app microsservico

-p 8000:8000: Mapeia a porta 8000 do contêiner para a porta 8000 da sua máquina.
-v ${PWD}:/app: Monta o diretório atual no contêiner, permitindo que as alterações no código e banco de dados sejam refletidas instantaneamente.
Passo 4: Testar as rotas
Agora você pode testar as rotas utilizando o Postman ou outra ferramenta de requisições HTTP. A aplicação estará disponível em http://localhost:8000.

Exemplos de rotas:

GET: Listar usuários

GET http://localhost:8000/api/usuarios

POST: Criar um novo usuário

POST http://localhost:8000/api/usuarios

PUT http://localhost:8000/api/usuarios/<id>

DELETE http://localhost:8000/api/usuarios/<id>

Banco de Dados
O banco de dados SQLite comunidade.db será criado automaticamente na pasta instance/ quando o projeto for executado. Todas as operações CRUD são refletidas em tempo real no banco de dados.

Logs
Para monitorar os logs do contêiner, execute o seguinte comando:

bash
Copiar código
docker logs -f <CONTAINER_ID>
Substitua <CONTAINER_ID> pelo ID do contêiner em execução.

Considerações Finais
Este projeto está configurado para desenvolvimento e não deve ser utilizado diretamente em produção. Para ambientes de produção, recomenda-se utilizar um servidor WSGI (como Gunicorn) e configurar volumes persistentes adequadamente.