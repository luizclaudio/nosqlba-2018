#coding: utf-8

from bd_documento import BancoDocumentos

banco = BancoDocumentos()
banco.criar_colecao('default')
while True:
    texto = input('?> ')
    partes = texto.split()
    comando = partes[0].upper()
    # create ou inserir
    if comando == 'C' or comando == 'I':
        registro = {}
        for par in partes[1:]:
            chave, valor = par.split('=')
            registro[chave] = valor
        novo_indice = banco.inserir('default', registro)
        print('Inserido: índice={0}, registro={1}'.format(novo_indice, registro))
    # retrieve e recuperar
    elif comando == 'R':
        try:
            if len(partes) < 2:
                print('Índice inválido.')
                continue
            indice = partes[1]
            if indice == '':
                print('Índice inválido.')
                continue
            registro = banco.recuperar('default', int(indice))
            print('Recuperado: índice={0}, registro={1}'.format(indice, registro))
        except KeyError:
            print('Índice não encontrado.')
    # update ou atualizar
    elif comando == 'U' or comando == 'A':
        try:
            if len(partes) < 2:
                print('Índice inválido.')
                continue
            indice = partes[1]
            if indice == '':
                print('Índice inválido.')
                continue
            if len(partes) < 3:
                print('Dados chave e valor inválidos.')
                continue
            chave, valor = partes[2].split('=')
            banco.atualizar('default', int(indice), chave, valor)
            print('Atualizado: índice={0}, chave={1}, valor={2}'.format(indice, chave, valor))
        except KeyError:
            print('Índice não encontrado.')
    # delete ou excluir
    elif comando == 'D' or comando == 'E':
        try:
            if len(partes) < 2:
                print('Índice inválido.')
                continue
            indice = partes[1]
            if indice == '':
                print('Índice inválido.')
                continue
            banco.excluir('default', int(indice))
            print('Excluído: índice={0}'.format(indice))
        except KeyError:
            print('Índice não encontrado.')
    # quit ou fim
    elif comando == 'Q' or comando == 'F':
        print('FIM')
        break
    else:
        print('Comando desconhecido.')