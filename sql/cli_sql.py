#coding: utf-8

import sqlite3

connection = sqlite3.connect('dados.sqlite')
cursor = connection.cursor()

print('\nExemplo de CRUD com SQLite')
while True:
    texto = input('>>> ')
    partes = texto.split()
    comando = partes[0].upper()

    # help
    if comando == 'H' or comando == 'J':
        print('= AJUDA =')
        print('Mostrar ajuda .......... H')
        print('Inserir um registro .... I nome preco estoque')
        print('Listar registros ....... L')
        print('Recuperar um registro .. R chave')
        print('Atualizar um registro .. A chave campo valor')
        print('Excluir um registro .... E chave')
        print('Sair ................... F')

    # create ou inserir
    elif comando == 'C' or comando == 'I':
        if len(partes) < 4:
            print('Todos os campos (nome, preço, estoque) são obrigatórios.')
            continue
        nome = partes[1]
        preco = partes[2]
        estoque = partes[3]
        stmt = 'INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)'
        cursor.execute(stmt, (nome, preco, estoque))
        connection.commit()
        novo_id = cursor.lastrowid
        print('Inserido: id={0}'.format(novo_id))

    # list e listar
    elif comando == 'L':
        stmt = 'SELECT id, nome, preco, estoque FROM produtos'
        cursor.execute(stmt)
        registros = cursor.fetchall()
        if registros:
            print('CHAVE, NOME, PREÇO, ESTOQUE')
            for r in registros:
                chave = r[0]
                nome = r[1]
                preco = r[2]
                estoque = r[3]
                print('{}, {}, {}, {}'.format(chave, nome, preco, estoque))
        else:
            print('Nenhum registro encontrado.')

    # retrieve e recuperar
    elif comando == 'R':
        if len(partes) < 2:
            print('Informe a chave do registro a ser recuperado.')
            continue
        chave = partes[1]
        stmt = 'SELECT id, nome, preco, estoque FROM produtos WHERE id = ?'
        cursor.execute(stmt, (chave,))
        registro = cursor.fetchone()
        if registro:
            chave = registro[0]
            nome = registro[1]
            preco = registro[2]
            estoque = registro[3]
            print('Recuperado: chave={}, nome={}, preço={}, estoque={}'.format(chave, nome, preco, estoque))
        else:
            print('Registro não encontrado.')

    # update ou atualizar
    elif comando == 'U' or comando == 'A':
        if len(partes) < 4:
            print('Informe a chave do regsitro, o campo e o novo valor.')
            continue
        chave = partes[1]
        campo = partes[2]
        valor = partes[3]
        stmt = 'UPDATE produtos SET {} = ? WHERE id = ?'.format(campo)
        cursor.execute(stmt, (valor, chave))
        connection.commit()
        print('Atualizado: chave={}, {}={}'.format(chave, campo, valor))

    # delete ou excluir
    elif comando == 'D' or comando == 'E':
        if len(partes) < 2:
            print('Informe a chave do registro a ser excluído.')
            continue
        chave = partes[1]
        stmt = 'DELETE FROM produtos WHERE id = ?'
        cursor.execute(stmt, (chave,))
        connection.commit()
        print('Excluído: chave={}'.format(chave))

    # quit ou fim
    elif comando == 'Q' or comando == 'F':
        print('\nFIM')
        break

    else:
        print('Comando desconhecido.')
