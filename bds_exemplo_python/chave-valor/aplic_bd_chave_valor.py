#coding: utf-8

from bd_chave_valor import BancoChaveValor

banco = BancoChaveValor()
while True:
    texto = input('?> ')
    partes = texto.split()
    comando = partes[0].upper()
    chave = ''
    valor = ''
    if len(partes) > 1:
        chave = partes[1]
    if len(partes) > 2:
        valor= partes[2]
    # create ou inserir
    if comando == 'C' or comando == 'I':
        if chave == '':
            print('Chave inválida.')
            continue
        banco.inserir(chave, valor)
        print('Inserido: chave={0}, valor={1}'.format(chave, valor))
    # retrieve e recuperar
    elif comando == 'R':
        try:
            if chave == '':
                print('Chave inválida.')
                continue
            valor = banco.recuperar(chave)
            print('Recuperado: chave={0}, valor={1}'.format(chave, valor))
        except KeyError:
            print('Chave não encontrada.')
    # update ou atualizar
    elif comando == 'U' or comando == 'A':
        try:
            if chave == '':
                print('Chave inválida.')
                continue
            banco.atualizar(chave, valor)
            print('Atualizado: chave={0}, valor={1}'.format(chave, valor))
        except KeyError:
            print('Chave não encontrada.')
    # delete ou excluir
    elif comando == 'D' or comando == 'E':
        try:
            if chave == '':
                print('Chave inválida.')
                continue
            banco.excluir(chave)
            print('Excluído: chave={0}'.format(chave))
        except KeyError:
            print('Chave não encontrada.')
    # quit ou fim
    elif comando == 'Q' or comando == 'F':
        print('FIM')
        break
    else:
        print('Comando desconhecido.')