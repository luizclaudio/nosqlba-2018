### Exemplos apresentados no minicurso *"Usando BDs NoSQL com Python"*, no evento *"NoSQL BA 2018"*, em 08/03/2018. ###

O objetivo dos programas aqui apresentados é tanto trabalhar com os conceitos dos bancos de dados NoSQL quanto apresentar código em Python que possa ser compreendido por pessoas iniciantes na linguagem e servir de fonte básica de estudo. Todos os programas devem ser executados com Python 3:

```python3 <nome do arquivo>```

O conteúdo se divide em:

1. **Pasta "bds_exemplo_python"**

    Cada uma das subpastas tem exemplos básicos dos cinco tipos de bancos NoSQL (chave-valor, orientado a documentos, colunar, "big table" e orientado a grafo).
    - **Arquivos "bd_..."**:
    Implementação do banco, propriamente dito.
    - **Arquivos "test_bd_..."**:. arquivo de testes para o banco.
    - **Arquivos "aplic_bd_..."**:   aplicações tipo linha de comando (CLI) utilizando o banco. Disponível para os bancos chave-valor,  orientado a documentos e "big table".

2. **Pasta "sql"**
    -  **"criar_db.py"**: arquivo que deve ser executado primeiramente para gerar o banco de dados, arquivo chamado **dados.sqlite"**.
    - **"cli_sql.py"**: uma aplicação tipo linha de comando (CLI) utilizando um banco relacional (SQLite), para servir como parâmetro de comparação.

3. **Pasta "mongo"**
    - **"exemplos_mongo.py"**: arquivo que serve como repositório de trechos de código para acessar e utilizar um banco em um servidor MongoDB.
    - **"cli_mongo.py"**: aplicação tipo linha de comando (CLI) utilizando o banco MongoDB. O exemplo busca acessar um servidor instalado na própria máquina (127.0.0.1). Caso seja utilizado um servidor em uma máquina remota, os parâmetros de conexão e controle de acesso precisarão ser alterados.

4. **Pasta "redis"**
    - **"exemplos_redis.py"**: arquivo que serve como repositório de trechos de código para acessar e utilizar um servidor Redis.
    - **"cli_mongo.py"**: aplicação tipo linha de comando (CLI) utilizando um servidor Redis. O exemplo busca acessar um servidor instalado na própria máquina (127.0.0.1). Caso seja utilizado um servidor em uma máquina remota, os parâmetros de conexão e controle de acesso precisarão ser alterados.

5. **Dockerfile**

    O arquivo "Dockerfile" contém os comandos para a criação de um container ("python3_redis_mongo") com todo o conteúdo necessário para executar os programas, inclusive um servidor Redis e um servidor MongoDB. O tamanho final é aproximandamente 670 MB. Siga os seguintes passos:

    - Crie o container:

        ```docker build . -t python3_redis_mongo```

    - Inicie o container (todos os arquivos ficarão disponíveis e atualizáveis no container em "/home/code"):

        ```docker run -i -t -v $(pwd)/:/home/code:rw python3_redis_mongo```

    - Inicie os bancos de dados (na ordem e quando achar melhor):

        ```service redis-server start```

        ```service mongodb start```

