# bar-guide

Projeto Guia de Bares SP

-----------------------------------------------------------------

1. Instalação WSL (Ubuntu 22)
OBS: Caso o WSL já esteja instalado, pule para o próximo passo
    1.1 Abra o PowerShell como administrador e execute o seguinte comando:
        
        wsl --install -d Ubuntu-22.04

    1.2 Reinicie o computador e configure o nome e senha de usuário no primeiro login do Ubuntu via terminal 

    1.3 Atualize os pacotes com os seguintes comandos:

        sudo apt update && sudo apt upgrade -y




2. Instalação Docker no WSL

    2.1 Instale o Docker Desktop no Windows: https://www.docker.com/products/docker-desktop

    2.2 Nas configurações do Docker Desktop, ative a integração do Docker com o Ubuntu (No caso, Ubuntu 22.04)

        Settings > Resources >  WSL Integration

    2.3 No terminal WSL, teste o Docker:

        docker --version
        docker info
        docker run hello-world

3. Upload dos containers através do docker-compose.yml

    3.1 Acessar o diretório raíz do projeto no terminal WSL:

        cd /mnt/c/path-do-projeto-clonado/bar-guide -> docker-compose.yml está aqui

    3.2 Dentro desse diretório, execute o seguinte comando para subir os containers

        docker-compose up -d

        OBS: Esse comando deve ser executado sempre após reiniciar/ligar o pc (WSL); Docker Desktop(Windows) também deve estar rodando

    3.3 Rode o seguinte comando para verificar se os containers estão rodando

        docker ps

OBS: Caso você já possua um container do PostgreSQL, a base de dados não será criada e será necessário criar a base de dados manualmente; Esse passo deve ser feito apenas nesse caso

4. Criação da base de dados

    4.1 Comandos para instalação e conexão do client postgres:

        sudo apt install postgresql-client -y
        
        docker exec -it id-do-container psql -U guia_admin -d guia_bares (infos de user e dbname estão no arquivo .env)

    4.2 Dentro do PostgreSQL, crie a base de dados:

        CREATE DATABASE guia_bares;

    4.3 Comando para listar as bases de dados criadas no PostgreSQL (Comando deve ser executado ainda dentro do terminal do PostgreSQL)

        \l ou \list

    4.4 Conectando à uma base de dados:

        \c nome_da_base

5. Instalação do Python 3.11 no WSL

    5.1 Execute os seguintes comandos dentro do terminal WSL:

        sudo apt update
        sudo apt install software-properties-common -y
        sudo add-apt-repository ppa:deadsnakes/ppa -y
        sudo apt update
        sudo apt install python3.11 python3.11-venv python3.11-dev -y
        sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

    5.2 Valide a versão do Python

        python --version

6. Criação do ambiente virtual (venv)

    6.1 Acesse a pasta do backend:

        cd /mnt/c/path-do-projeto-clonado/bar-guide/apps/backend

    6.2 Crie o ambiente virtual Python:

        python -m venv venv

    6.3 Ative o ambiente:

        source venv/bin/activate

    6.4 Instale o pip no WSL (caso ainda não esteja instalado):

        sudo apt install python3-pip -y

    6.5 Crie o arquivo de dependências:

        Nesse ponto, o arquivo requirements.txt já está criado com todas as dependências, mas caso não apareça o arquivo dentro de /backend, só executar o comando abaixo e incluir as dependências dentro dele

        touch requirements.txt

        dependências:
                fastapi
                uvicorn[standard]
                sqlalchemy
                asyncpg
                geoalchemy2
                psycopg2-binary
                alembic
                python-dotenv
                pydantic
                redis

    6.6 Use o pip para instalar os pacotes, executando o requirements

        pip install -r requirements.txt