#coding: utf-8

import redis

banco = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password='')
 
while True:
    texto = input('>>> ')
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
        banco.set(chave, valor)
        print('Inserido: chave={0}, valor={1}'.format(chave, valor))
    
    # retrieve e recuperar
    elif comando == 'R':
        if chave == '':
            print('Chave inválida.')
            continue
        valor = banco.get(chave)
        if valor:
            print('Recuperado: chave={0}, valor={1}'.format(chave, valor.decode('utf-8')))
        else:
            print('Chave não encontrada.')
    
    # listar
    elif comando == 'L':
        chaves = banco.keys()        
        if chaves:            
            for c in chaves:
                valor = banco.get(c)
                print('chave={0}, valor={1}'.format(c.decode('utf-8'), valor.decode('utf-8')))
        else:
            print('Nenhuma chave não encontrada.')    
    
    # update ou atualizar
    elif comando == 'U' or comando == 'A':
        if chave == '':
            print('Chave inválida.')
            continue
        valor_antigo = banco.get(chave)
        if valor_antigo:
            banco.set(chave, valor)
            print('Atualizado: chave={0}, valor={1}'.format(chave, valor))
        else:
            print('Chave não encontrada.')
    
    # delete ou excluir
    elif comando == 'D' or comando == 'E':
        if chave == '':
            print('Chave inválida.')
            continue
        valor = banco.get(chave)
        if valor:
            banco.delete(chave)
            print('Excluído: chave={0}'.format(chave))
        else:
            print('Chave não encontrada.')
    
    # quit ou fim
    elif comando == 'Q' or comando == 'F':
        print('FIM')
        break
    else:
        print('Comando desconhecido.')
