#coding: utf-8

from bd_big_table import BancoBigTable

def mostrar_ajuda():
    print('\nC (ou I) <chave> <col_1>=<val_1> ... <col_n>=<val_n> _ _ Insere um registro.')
    print('R <chave>  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ Recupera um registro.')
    print('S (ou B) <coluna>=<valor> _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ Busca registros.')
    print('L _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __ Lista todos registros.')
    print('U (ou A) <chave> <col_1>=<val_1> ... <col_n>=<val_n> _ _ Atualiza um registro.')
    print('D <chave>  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ Exclui um registro.')
    print('D <chave>  <col_1> ... <col_n> _ _ _ _ _ _ _ _ _ _ _ _ _ Exclui colunas do reg.')
    print('H (ou J) _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ Mostra esta ajuda.\n')

banco = BancoBigTable()
banco.criar_tabela('default')
print('\n=== Exemplo de CRUD com banco "Big Table" ===')
mostrar_ajuda()
while True:
    texto = input('>>> ')
    partes = texto.split()
    comando = partes[0].upper()

    # create ou inserir
    if comando == 'C' or comando == 'I':
        if len(partes) < 3:
            print('Dados obrigatórios não informados.')
            continue
        chave = partes[1]
        registro = {}
        for par in partes[2:]:
            coluna, valor = par.split('=')
            registro[coluna] = valor
        banco.inserir('default', chave, registro)
        print('Inserido: chave={0}, registro={1}'.format(chave, registro))

    # retrieve e recuperar
    elif comando == 'R':
        if len(partes) < 2:
            print('Dados obrigatórios não informados.')
            continue
        chave = partes[1]
        if chave == '':
            print('Chave inválida.')
            continue
        try:
            registro = banco.recuperar('default', chave)
            print('Recuperado: chave={0}, registro={1}'.format(chave, registro))
        except KeyError:
            print('Chave não encontrada.')

    # search e buscar
    elif comando == 'S' or comando == 'B':
        if len(partes) < 2:
            print('Dados obrigatórios não informados.')
            continue
        coluna, valor = partes[1].split('=')
        if chave == '':
            print('Chave inválida.')
            continue
        encontradas = banco.buscar('default', coluna, valor)
        if encontradas:
            for c in encontradas:
                registro = banco.recuperar('default', c)
                print('- chave={0}, registro={1}'.format(c, registro))
        else:
            print('Nenhum registro encontrado.')

    # list ou listar
    elif comando == 'L':
        chaves = banco.buscar('default')
        if chaves:
            for c in chaves:
                registro = banco.recuperar('default', c)
                print('- chave={0}, registro={1}'.format(c, registro))
        else:
            print('Nenhum registro encontrado.')

    # update ou atualizar
    elif comando == 'U' or comando == 'A':
        if len(partes) < 3:
            print('Dados obrigatórios não informados.')
            continue
        chave = partes[1]
        if chave == '':
            print('Chave inválida.')
            continue
        dados = {}
        for par in partes[2:]:
            coluna, valor = par.split('=')
            dados[coluna] = valor
        try:
            banco.atualizar('default', chave, dados)
            print('Atualizado: chave={0}, dados={1}'.format(chave, dados))
        except KeyError:
            print('Chave não encontrada.')

    # delete ou excluir
    elif comando == 'D' or comando == 'E':
        if len(partes) < 2:
            print('Dados obrigatórios não informados.')
            continue
        chave = partes[1]
        if chave == '':
            print('Chave inválida.')
            continue
        try:
            if len(partes) == 2:
                banco.excluir('default', chave)
                print('Excluído: chave={0}'.format(chave))
            else:
                colunas = []
                for par in partes[2:]:
                    colunas.append(par)
                banco.excluir('default', chave, colunas)
                print('Colunas excluídas: chave={0}, colunas={1}'.format(chave, colunas))
        except KeyError:
            print('Chave não encontrada.')

    # help ou ajuda
    elif comando == 'H' or comando == 'J':
        mostrar_ajuda()

    # quit ou fim
    elif comando == 'Q' or comando == 'F':
        print('FIM')
        break
    # comandos desconhecidos
    else:
        print('Comando desconhecido.')