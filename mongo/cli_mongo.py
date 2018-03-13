#coding: utf-8

import pymongo
from bson.objectid import ObjectId

URL = 'mongodb://127.0.0.1/'
client = pymongo.MongoClient(URL)
db = client['nosqlba2018']
colecao = db['minha_colecao']

print('\nExemplo de CRUD com MongoDB')
while True:
    texto = input('>>> ')
    partes = texto.split()
    comando = partes[0].upper()
    
    # create ou inserir
    if comando == 'C' or comando == 'I':
        documento = {}
        for par in partes[1:]:
            chave, valor = par.split('=')
            documento[chave] = valor
        novo_id = colecao.insert_one(documento).inserted_id
        print('Documento inserido: id = {}'.format(novo_id))
    
    # list ou listar
    elif comando == 'L':
        documentos = colecao.find()
        if documentos.count() > 0:
            for doc in documentos:
                print(doc)
        else:
            print('Nenhum documento encontrado.')

    # retrieve e recuperar
    elif comando == 'R':
        if len(partes) < 2:
            print('Id inválido.')
            continue
        doc_id = partes[1]
        documento = colecao.find_one({'_id': ObjectId(doc_id)})
        if documento:
            print(documento)
        else:
            print('Id não encontrado.')

    # search e buscar
    elif comando == 'S' or comando == 'B':
        if len(partes) < 2:
            print('Informe o par chave=valor para busca.')
            continue
        chave, valor = partes[1].split('=')
        documentos = colecao.find({chave: valor})
        if documentos.count():
            for doc in documentos:
                print(doc)
        else:
            print('Nenhum doucmento encontrado.')

    # update ou atualizar
    elif comando == 'U' or comando == 'A':
        if len(partes) < 3:
            print('Informe o Id e o(s) par(es) chave=valor .')
            continue
        doc_id = partes[1]
        documento = colecao.find_one({'_id': ObjectId(doc_id)})
        if documento:        
            dados = {}
            for par in partes[2:]:
                chave, valor = par.split('=')
                dados[chave] = valor
            colecao.update({"_id": ObjectId(doc_id)},{'$set':dados})
            print('Documento atualizado.')
        else:
            print('Id não encontrado.')

    # delete ou excluir
    elif comando == 'D' or comando == 'E':
        if len(partes) < 2:
            print('Informe o Id.')
            continue
        doc_id = partes[1]
        documento = colecao.find_one({'_id': ObjectId(doc_id)})
        if documento:                          
            resultado = colecao.delete_one({'_id': ObjectId(doc_id)})
            print('Documento excluído.')
        else:
            print('Id não encontrado.')
        
    # drop ou limpar
    elif comando == 'X':
        opcao = input('Todos os documentos serão apagados. Confirma (S/N)?')
        if opcao.upper() == 'S':            
            colecao.drop()
            print('Todos documentos foram apagados.') 
        
    # help ou ajuda
    elif comando == 'H' or comando == 'J':
        print('\nComandos disponíveis:')
        print('Ver ajuda ________________ H (ou J)')
        print('Inserir um doc. __________ I (ou C) <chave1>=<valor1> <chave2>=<valor2> ...')
        print('Listar todos docs. _______ L')
        print('Recuperar um doc. por Id _ R <id>')
        print('Buscar um doc. por valor _ B (ou S) chave=valor')
        print('Atualizar um doc. ________ A (ou U) <id> <chave1>=<valor1> <chave2>=<valor2> ...')
        print('Excluir um doc. __________ E (ou D) <id>')
        print('Limpar a coleção _________ X')
        print('Sair do programa _________ F (ou Q)')
        
    # quit ou fim
    elif comando == 'Q' or comando == 'F':
        client.close()
        print('\nProcessamento encerrado.\n')
        break
    else:
        print('Comando desconhecido.')
            
    


