#coding: utf-8

import pymongo
from bson.objectid import ObjectId

URL = 'mongodb://127.0.0.1/'
client = pymongo.MongoClient(URL)
db = client['nome_banco']
colecao = db['nome_colecao']

# -- INSERIR (CREATE) ------------------------------

documento = {'campo_texto':'um texto', 'campo_numerico':12345, 'outro_campo':'mais texto'}
novo_id = colecao.insert_one(documento).inserted_id
print(novo_id)


# -- RECUPERAR/BUSCAR (RETREIVE) ------------------------------

documento = colecao.find_one()
print(documento)
# ---
documento = colecao.find_one({'_id': ObjectId('595d3a9e69edb12221f407f9')})
print(documento)
# ---
lista_documentos = colecao.find({'campo_1': 'valor buscao'})
for documento in lista_documentos:
    print(documento)
# ---
lista_documentos = colecao.find({'data': {'$lt': '1800-01-01'}}).sort('local')
for documento in lista_documentos:
    print(documento)


# -- ATUALIZAR (UPDATE) ------------------------------

colecao.update({'campo_busca': 'valor para busca'}, {'$set':{'campo_atualizacao': 'novo valor'}})


# -- EXCLUIR (DELETE) ------------------------------

resultado = colecao.delete_one({'_id': ObjectId('595d3a9e69edb12221f407f9')})
# ---
resultado = colecao.delete_many({'campo_busca': 'valor_buscado'})
# ---
colecao.drop()

